from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404

from .models import BlogPost

# Create your views here.


class BlogListView(ListView):
    queryset = BlogPost.published.all()  # retrieves only published posts
    model = BlogPost
    template_name = "home.html"

def post_detail(request):
    post = get_object_or_404(BlogPost,status="published")
    return render(request,"post_detail.html",{"post":post})

# class BlogDetailView(DetailView):
#     model = BlogPost
#     template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = BlogPost
    fields = "__all__"
    template_name = "post_new.html"


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'body']
    template_name = "post_update.html"


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')
