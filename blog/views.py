from django.views.generic import ListView

from .models import BlogPost

# Create your views here.

class BlogListView(ListView):
    model = BlogPost
    template_name = "home.html"