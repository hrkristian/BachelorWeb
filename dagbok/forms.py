from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def clean_slug(self):
        return self.cleaned_data['slug'].lower()
