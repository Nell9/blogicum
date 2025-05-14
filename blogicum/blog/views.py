from django.http import Http404
from django.shortcuts import render
from django.db.models import Q

from blog.models import Post, Category, Location


def index(request):
    posts = Post.objects.all()[:5]
    return render(request, 'blog/index.html', {'post_list': posts})


def category_posts(request, category_slug):
    posts = Post.objects.all().filter(
        Q(is_published=True) & Q(category__slug=category_slug)
    )
    return render(request, 'blog/category.html', {'post_list': posts})

def post_detail(request, post_id):
    pass
