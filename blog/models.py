from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Our Post Model

#custom Manage

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status = 'published')

class Post(models.Model):
    STATUS_CHOICE = (('draft','Draft'),
                     ('published','Published'),
                     )
    POST_TAGS = (('Python','python'),('None','none'),('Golang','golang'),('c++','C++'), ('Generic','generic'),)

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_post', on_delete=models.CASCADE)
    post_tags = models.CharField(max_length=20, choices=POST_TAGS, default='python')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    photo = models.ImageField(upload_to='post', default='null.png')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')




    #the default manage
    objects = models.Manager()

    # custom made manager
    published = PublishedManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
# Create your models here.


def approved_comments(self):
    return self.comments.filter(approved_comment=True)