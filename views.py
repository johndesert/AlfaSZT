from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostCreateForm, PostModifyForm

class BasicPageViews(ListView):
    model = Post
    template_name = 'home.html'

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