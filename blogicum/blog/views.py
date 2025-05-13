from django.http import Http404
from django.shortcuts import render


posts_by_ids = {post['id']: post for post in posts}


def index(request):
    return render(request, 'blog/index.html', {'posts': posts[::-1]})


def category_posts(request, category_slug):
    posts_by_category = [post for post in posts
                         if post['category'] == category_slug]
    return render(request, 'blog/category.html', {
        'posts_by_category': posts_by_category,
        'category': category_slug
    })


def post_detail(request, post_id):
    if not posts_by_ids.get(post_id):
        raise Http404(f'Страница {post_id} не найдена :(')
    return render(
        request,
        'blog/detail.html',
        {'post': posts_by_ids.get(post_id)}
    )
