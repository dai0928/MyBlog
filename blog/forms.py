from django import forms
from .models import CreateBlogModel


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = CreateBlogModel
        fields = ('blog_title', 'text', 'user')
