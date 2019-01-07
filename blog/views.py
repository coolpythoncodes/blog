from django.views.generic import DetailView,ListView
from django.views.generic.edit import CreateView

from .models import BlogPost

# Create your views here.

class BlogListView(ListView):
    model = BlogPost
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = BlogPost
    fields = "__all__"
    template_name = "post_new.html"