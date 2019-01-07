from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:pk>', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.BlogUpdateView.as_view(), name='post_update'),
]