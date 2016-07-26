from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect


from .forms import PostForm, RegisterForm
from .models import Post


def post_list(request):
    posts = Post.objects.filter(public_post=1).order_by('-published_date')
    context = {'posts': posts }
    return render(request, 'myapp/post_list.html', context)

def user_post_list(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author__username=username).order_by('-published_date')
    if username!=request.user.username : posts=posts.filter(public_post=1)
    context = {'posts': posts, 'author': user}
    return render(request, 'myapp/user_post_list.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('user_post_list',
                username=request.user.username)
    else:
        form = PostForm()
    context = {'form': form, 'create': True}
    return render(request, 'myapp/form.html', context)


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)     # create form object
        if form.is_valid():
            register = form.save(commit=False)
            register.save()
            form.save_m2m()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("post_list")
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'myapp/register.html', context)
# Create your views here.
