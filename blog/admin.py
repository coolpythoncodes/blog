from django.contrib import admin
from .models import BlogPost, Comment

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date','status')

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post')
    ordering = ('-created',)



