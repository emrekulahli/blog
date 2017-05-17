from django import forms
from .models import Post
from .models import Comment
from captcha.fields import ReCaptchaField


class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = [

            'content',
        ]