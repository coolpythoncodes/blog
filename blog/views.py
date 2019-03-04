from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import BlogPost
from .forms import CommentForm

# Create your views here.


def post_list(request):
    post_list = BlogPost.published.all() # retrieves only published posts
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,"home.html",{"posts":posts})


def post_detail(request,post):
    post = get_object_or_404(BlogPost, slug=post)
    # retrieves all comments in a particular blog post
    comments = post.comments.all()
    new_comment = None
      
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the new comment
            new_comment.post = post 
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(
        request, 
        "post_detail.html", 
        {
            "post": post, 
            "comment_form": comment_form, 
            "new_comment": new_comment,
            "comments": comments, 
            
        }
        )


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



