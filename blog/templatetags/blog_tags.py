from django import template
from django.db.models import Count
from ..models import BlogPost

register = template.Library()

# custom tag to get the most recent published post
@register.inclusion_tag('recent_post.html')
def show_recent_post(count=3):
    recent_post = BlogPost.published.all()[:count]  # Retrieves recent blog post according to the value of count
        
    return {
        'recent_post': recent_post,
        
    }


# custom tag to get the most commented post
@register.simple_tag
def most_commented(count=5):
    return BlogPost.published.annotate(
        total_comments = Count('comments')
    ).order_by('-total_comments')[:count]
    