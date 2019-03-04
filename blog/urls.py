from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='home'),
    # path('', views.BlogListView.as_view(), name='home'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.BlogUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='post_delete')
]