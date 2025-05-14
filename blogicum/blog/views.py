from django.http import Http404
from django.shortcuts import render


def index(request):
    render(request,'blog/index', )


def category_posts(request, category_slug):
    pass


def post_detail(request, post_id):
    pass
