from django import forms
from models import Post
from datetime import date, datetime

class PostForm(forms.ModelForm):
    class Meta:
        model = Post

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['text'].required = True