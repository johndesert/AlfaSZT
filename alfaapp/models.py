from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse('detailed-post', args=(str(self.pk)))
        return reverse('home')

class ContactMessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    topic = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')