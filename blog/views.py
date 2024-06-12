from django.shortcuts import render , get_object_or_404 , HttpResponse , redirect
from blog.models import Blog
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def view_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/view_blog.html', context={'blogs': blogs})

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        author = request.POST.get('author')

        if title and summary and author : 
            slug = title.lower().replace(' ','-')
            blog = Blog(title=title, summary=summary, author=author, slug=slug)
            blog.save()
            return redirect('view_blog')
        else:
            return HttpResponse('Veuillez remplir tous les champs')
    else:
        return render(request, 'blog/create_blog.html')
        