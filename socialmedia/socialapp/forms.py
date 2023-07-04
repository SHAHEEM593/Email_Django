from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'caption', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Upload'))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','text']