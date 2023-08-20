from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request, 'blog/blog.html', context)

def details(request, slug):
    post = Post.objects.get(slug=slug)
    latest = Post.objects.exclude(slug__exact=post.slug)[:5]
    categorys = Category.objects.all()
    context = {"post":post, 'categorys':categorys, 'latest':latest}
    return render(request, 'blog/blogDetails.html', context)

def categoryPosts(request, slug):
    context = {}
    return render(request, 'blog/categoryPosts.html', context)
