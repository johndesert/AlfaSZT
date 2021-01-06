from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostCreateForm, PostModifyForm
from django.urls import reverse_lazy

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
