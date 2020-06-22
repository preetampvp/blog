from django.urls import path

from .views import home, post

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('entry/<slug:slug>', post, name='post'),
]
