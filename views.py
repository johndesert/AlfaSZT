from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
#def home(request):
#    return render(request, 'home.html', {})

class BasicPageViews(ListView):
    model = Post
    template_name = 'home.html'

class DetailedViews(DetailView):
    model = Post
    template_name = 'detailed_post.html'