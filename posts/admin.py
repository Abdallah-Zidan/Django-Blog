from django.contrib import admin
from .models import Post, Tag, Category, Comment, Profanity
# # Register your models here.
class CustomPost(admin.ModelAdmin):
	fieldsets = (['write post', {'fields': ['title', 'body','image','user','status', 'tags']}],
		['like or dislike',{'fields':['likes']}],)
	list_display = ['title','image','date_published','slug_url','status',]
	list_filter =['date_published','title']
	
admin.site.register(Post,CustomPost)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profanity)
