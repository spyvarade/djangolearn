from django.contrib import admin
from .models import (
		Category,
		Post,
		Comment
	)

# Register your models here.

def change_status(modeladmin,request,queryset):
	queryset.update(
			active=True
		)

change_status.short_description = "Change Status"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	actions =[change_status]
	list_display = ['title','common','view_plus_like','views','likes','published_at','updated','status','active']
	ordering = ['updated']
	list_editable = ['views','likes','active','status']
	list_filter = ['active','status']
	search_fields = ['title']
	date_hierarchy = 'updated'
	#detail view k liye
	
	save_as = True
	save_on_top =True
	
	# fields = (
	# 		('author','category'),
	# 		('title','slug'),
	# 		'views',
	# 		'likes',
	# 		'image',
	# 		'body',
	# 		'active',
	# 		'status',
	# 	)
	
	fieldsets =(
			(None,{
				'fields':(
						('author','category'),
						('title','slug'),
					)
				}),
			('OTHER',{
					'classes': ('collapse',),
					'fields':(
						   'views',
							'likes',
							'image',
							'body',
							'active',
							'status',
						)				
				})
			
		)


admin.site.register(Category)

# admin.site.register(Post,PostAdmin)
admin.site.register(Comment)



#Admin Register
#ListView
#DetilView(fiels and fieldset)