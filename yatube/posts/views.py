# posts/views.py

from django.shortcuts import render, get_object_or_404

from .models import Post, Group

#Количество выводимых сообщений
QUANTITY = 10

# Стартовая страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:QUANTITY]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

# Страница сообщений группы
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:QUANTITY]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)