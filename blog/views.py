from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #Returns a rendered template from the request


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #gets object or returns a 404 page not found error
    return render(request, 'blog/post_detail.html', {'post': post})


# Creates a new post form
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): # if all fields are set and no incorrect values
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # saves changes
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# Allows the user to edit a blog post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) # Gets requested blog or shows a page not found error
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})