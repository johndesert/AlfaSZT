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

def contact(request):
    if request.method == "POST":
        contact_user_email = request.POST['contact-user-email']
        contact_user_phone = request.POST['contact-user-phone']
        contact_user_name = request.POST['contact-user-name']
        contact_user_message = request.POST['contact-user-message']
        message_confirm = "we will contact you soon"
        return render(request, 'contact.html', {'message_confirm': message_confirm, 'contact_user_name':contact_user_name})
    else:
        return render(request, 'contact.html')