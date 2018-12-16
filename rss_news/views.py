from django.shortcuts import render
from .models import Post
import random


def index(reqests):
    number = random.randrange(0, 100)
    posts = Post.objects.all()

    context = {
        'value': "Hello world!",
        'number': str(number),
        'posts': posts
    }
    return render(reqests, "index.html", context)
