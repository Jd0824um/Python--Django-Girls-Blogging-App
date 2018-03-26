from django import forms #Imports django forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta: #Tells django which model should be used to create this form
        model = Post
        fields = ('title', 'text',)
