from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
]