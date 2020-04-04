from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = ( 
   ('draft', 'Draft'), 
   ('published', 'Published'), 
) 

class Category(models.Model):
	title 			= models.CharField(max_length = 250,verbose_name="Category Title" ,help_text="be unique")
	slug  			= models.SlugField(max_length = 250, null = True, blank = True)
	published_at 	= models.DateTimeField(auto_now_add = True) 
	updated 		= models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ('-published_at', ) 

	def __str__(self):
		return self.title 

class Post(models.Model):
	author 			= models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_users", related_query_name="post_user")
	category 		= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", related_query_name="categories")
	#Catagory.objects.filter(categories__title="electronics")
	title 			= models.CharField(max_length = 250)
	slug  			= models.SlugField(max_length = 250, null = True, blank = True)
	views 			= models.PositiveIntegerField() 
	likes           = models.PositiveIntegerField()
	image 			= models.ImageField('Picture',upload_to ='uploads/') # need Pillow Lib
	body  			= models.TextField()
	published_at 	= models.DateTimeField(auto_now_add = True) 
	updated 		= models.DateTimeField(auto_now = True)
	active          = models.BooleanField()
	status 			= models.CharField(max_length = 10, choices = STATUS_CHOICES, default ='draft')

	class Meta:
		ordering = ('-published_at', ) 

	def __str__(self):
		return self.title 

	@property
	def common(self):
		return '{} and {}'.format(self.title, self.slug)

	@property
	def view_plus_like(self):
		return self.views+self.likes


class Comment(models.Model):
	post 			= models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts', related_query_name="post")
	author 			= models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_users", related_query_name="comment_user")
	published_at 	= models.DateTimeField(auto_now_add = True) 
	updated 		= models.DateTimeField(auto_now = True)
	status 			= models.BooleanField()