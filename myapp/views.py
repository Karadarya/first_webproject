from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post



def post_list(request):
    return render(request, 'myapp/post_list.html', {})

def user_post_list(request, username):
    return render(request, 'myapp/user_post_list.html', {})
# Create your views here.
