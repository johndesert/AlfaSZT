from django.urls import path, include

from .views import BasicPageViews, DetailedViews, CreatePostViews, ModifyPostViews, DeletePostViews, SerPostView, CreateMessageViews


urlpatterns = [
    path('', BasicPageViews.as_view(), name="home"),
    path('post/<int:pk>', DetailedViews.as_view(), name="detailed-post"),
    path('createpost/', CreatePostViews.as_view(), name="create-post"),
    path('post/modifypost/<int:pk>', ModifyPostViews.as_view(), name="modify-post"),
    path('post/<int:pk>/deletepost', DeletePostViews.as_view(), name="delete-post"),
    path('contact.html', CreateMessageViews.as_view(), name="contact"),
    ]
