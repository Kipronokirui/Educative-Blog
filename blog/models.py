from django.db import models
from users.models import Profile
from autoslug import AutoSlugField
import uuid

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title', unique=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(default='avatar.jpg', upload_to='blogs', null=False, blank=False)
    slug = AutoSlugField(populate_from='title', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=False, default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    comment_id = models.UUIDField(default=uuid.uuid4, unique=True)
    
    def __str__(self):
        return self.comment

