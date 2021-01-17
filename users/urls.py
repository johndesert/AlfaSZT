from django.urls import path
from .views import UserSignupViews

urlpatterns = [
    path('register/', UserSignupViews.as_view(), name='signup')
]
