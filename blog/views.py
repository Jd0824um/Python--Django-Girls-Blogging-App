from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {}) #Returns a rendered template from the request
