from django.shortcuts import render, get_object_or_404

from .models import Post, Group

'''Количество выводимых сообщений.'''
QUANTITY_POSTS = 10


def index(request):
    '''Стартовая страница.'''

    posts = Post.objects.all()[:QUANTITY_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    '''Страница сообщений группы.'''

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_group.all()[:QUANTITY_POSTS]
    title = group.title
    description = group.description
    context = {
        'title': title,
        'description': description,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
