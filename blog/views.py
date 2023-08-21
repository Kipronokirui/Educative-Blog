from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment

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
    category = Category.objects.get(slug=slug)
    category_posts = Post.objects.filter(category=category)
    context = {"category_posts":category_posts, "category":category}
    return render(request, 'blog/categoryPosts.html', context)

def create_comment(request, slug):
    post = Post.objects.get(slug=slug)
    profile = request.user.profile
    if request.method == 'POST':
        data = request.POST
        comment = data["comment"]
        posted_comment = Comment.objects.create(
            author = profile,
            post=post,
            comment = comment,
        )
        # print(f"The posted data is {comment}")
        
        url = reverse('details', args=[slug])
        return HttpResponseRedirect(url)
