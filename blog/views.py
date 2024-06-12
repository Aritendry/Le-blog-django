from django.shortcuts import render , get_object_or_404
from blog.models import Blog
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def view_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/view_blog.html', context={'blogs': blogs})