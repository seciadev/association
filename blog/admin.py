from django.contrib import admin
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','created_date')
	list_filter = ('created_date', 'author')
	
# Register the post class with the associated model
#admin.site.register(Post, PostAdmin)