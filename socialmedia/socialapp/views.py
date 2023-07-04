from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm
from . models import Post,Like, Comment,User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.

def home(request):
    return render(request,'home.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def send_email(request):
    subject = 'Welcome to My Website'
    template = 'welcome_email.html'
    context = {'username': 'John Doe'}
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['demo@gmail.com']

    html_message = render_to_string(template, context)
    plain_message = strip_tags(html_message)

    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message)
    
    return redirect('email_sent')





def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'upload_post.html', {'form': form})

def view_posts(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'view_posts.html', {'posts': posts})



def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'update_post.html', {'form': form, 'post': post})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('view_posts')


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    try:
        like = Like.objects.get(user=user, post=post)
        post.likes_count -= 1
        like.delete()
    except Like.DoesNotExist:
        like = Like(user=user, post=post)
        like.save()
        post.likes_count += 1
    post.save()
    return redirect('post_detail', pk=pk)




# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = post
#             comment.save()
#             return redirect('view_posts', pk=pk)
#     else:
#         form = CommentForm()
#     return render(request, 'add_comment.html', {'form': form})

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('view_posts', pk=post_pk)

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('view_posts')
    else:
        form = CommentForm()
    return render(request, 'view_comments.html', {'form': form})



def view_comments(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    return render(request, 'view_comments.html', {'post': post, 'comments': comments})


