from django.shortcuts import render, get_object_or_404
from users_app.models import User
from .models import Post


def posts(request):
    # prefetch_related precarica le relazioni direttamente con una query sql
    users = User.objects.prefetch_related('posts')

    return render(request, 'posts.html', {'users': users})


def single_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'single_post.html', {'post': post})
