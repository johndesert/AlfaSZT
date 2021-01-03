from django.urls import path
#from . import views
from .views import BasicPageViews, DetailedViews

urlpatterns = [
    #path('', views.home, name="home"),
    path('', BasicPageViews.as_view(), name="home"),
    path('post/<int:pk>', DetailedViews.as_view(), name="detailed-post"),
]
