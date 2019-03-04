from django import template
from ..models import BlogPost

register = template.Library()



@register.inclusion_tag('recent_post.html')
def show_recent_post(count=3):
    recent_post = BlogPost.published.all()[:count] # Retrieves recent blog post according to the value of count
        
    return {
        'recent_post': recent_post,
        
    }