from django.db import models
from django.urls import reverse

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7,choices=POST_STATUS_CHOICES,default='Draft')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])

    class Meta:
        ordering = ('-date',) # show posts from latest published to the first published


