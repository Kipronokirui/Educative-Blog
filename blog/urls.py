from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('blog/<str:slug>/', views.details, name='details'),
    path('category/<str:slug>/', views.categoryPosts, name='categoryPosts'),
    path('comment/<str:slug>/', views.create_comment, name='create_comment')
]