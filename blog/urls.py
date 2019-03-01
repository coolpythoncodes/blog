from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    #path('post/<int:pk>', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/new', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.BlogUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='post_delete')
]