from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'time_created']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : "Write here the body of the post"}),
            'time_created': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder' : "YYYY-MM-DD hh:mm:ss"}),

        }

class PostModifyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : "Write here the body of the post"}),

        }