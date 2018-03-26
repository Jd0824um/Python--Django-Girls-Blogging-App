from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts}) #Returns a rendered template from the request


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) #gets object or returns a 404 page not found error
    return render(request, 'blog/post_detail.html', {'post': post})
