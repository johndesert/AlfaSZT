from django import forms
from .models import Post, ContactMessage

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : "Write here the body of the post"}),
        }

class PostModifyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : "Write here the body of the post"}),

        }
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'topic', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.Textarea(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : "Write here the body of the post"}),
        }