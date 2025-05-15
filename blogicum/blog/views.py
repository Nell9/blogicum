from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.utils import timezone

from blog.models import Post, Category, Location


def index(request):
    posts = Post.objects.all().filter(
        Q(is_published=True) &
        Q(pub_date__lte=timezone.now()) &
        Q(category__is_published=True)
    )[:5]
    return render(
        request,
        'blog/index.html',
        {
            'post_list': posts
        }
    )


def category_posts(request, category_slug):
    posts = Post.objects.all().filter(
        Q(is_published=True) &
        Q(category__slug=category_slug) &
        Q(pub_date__lte=timezone.now()) &
        Q(category__is_published=True)
    )
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return render(
        request,
        'blog/category.html',
        {
            'post_list': posts,
            'category': category.title
        }
    )


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )

    return render(request,
                  'blog/detail.html',
                  {'post': post}
                  )
