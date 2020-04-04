from django.shortcuts import render
from .models import Category, Post

# Create your views here.

def post(request):
	catagories = Category.objects.all()
	posts = Post.objects.all()
	return render(request,'post.html',{
			'catagories': catagories,
			'posts' : posts
		})