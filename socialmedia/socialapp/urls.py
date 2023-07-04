from django.urls import path
from . import views
from .views import send_email
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name = 'home'),
    path('upload/', views.upload_post, name='upload_post'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/update/', views.update_post, name='update_post'),
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/add_comment/', views.add_comment, name='add_comment'),
    path('send-email/', send_email, name='send_email'),
    path('email-sent/', TemplateView.as_view(template_name='welcome_email_sent.html'), name='email_sent'),
    path('post/<int:pk>/view_comments/', views.view_comments, name='view_comments'),]