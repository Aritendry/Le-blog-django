
from django.contrib import admin
from django.urls import path

from blog.views import index , view_blog , create_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('blog/',view_blog,name='view_blog'),
    path('create_blog/',create_blog,name='create_blog'),
]
