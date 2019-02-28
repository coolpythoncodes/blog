from django.db import models
from django.urls import reverse

# Create your models here.


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="Publish")


class BlogPost(models.Model):
    POST_STATUS_CHOICES = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft'),
    )
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=POST_STATUS_CHOICES, default='Draft')

    objects = models.Manager()
    published = PublishedPostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    class Meta:
        ordering = ('-date',)  # show posts from latest published to the first published


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)  # show comments from latest  to the first

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.post)
