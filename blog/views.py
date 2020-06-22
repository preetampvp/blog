from django.shortcuts import render
from .models import Blog, BLOG_STATE_CHOICES


def home(request):
    blogs = Blog.objects.filter(state=BLOG_STATE_CHOICES[1][0])
    context = {
        'blogs': blogs,
        'hero_image_url': 'https://images.unsplash.com/photo-1476085259528-8b1839cff31c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
        'show_heading': True
    }
    return render(request, "blog/home.html", context)


def post(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'hero_image_url': 'https://images.unsplash.com/photo-1476085259528-8b1839cff31c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
        'blog': blog
    }
    return render(request, "blog/post.html", context)
