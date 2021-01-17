from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, ContactMessage
from .forms import PostCreateForm, PostModifyForm, ContactMessageForm
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import PostSerializer

class BasicPageViews(ListView):
    model = Post
    template_name = 'home.html'
    ordering =['-time_created']

class DetailedViews(DetailView):
    model = Post
    template_name = 'detailed_post.html'

class CreatePostViews(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create_post.html'

class ModifyPostViews(UpdateView):
    model = Post
    form_class = PostModifyForm
    template_name = 'modify_post.html'

class DeletePostViews(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class CreateMessageViews(CreateView):
    model = ContactMessage
    form_class = ContactMessageForm
    template_name = 'contact.html'

class SerPostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer