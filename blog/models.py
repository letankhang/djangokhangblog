from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
import uuid


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = create_slug(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    # def get_url_value_search(self):
    #     return 'This is test test test'
        # full_path = self.request.get_full_path
        # value_search = full_path.split('q=')
        # return  value_search[1]

def create_slug(selftitle):
    from datetime import datetime
    time = str(datetime.now())
    time = "".join(time.split("."))
    return slugify(str(time[17:]) + str(selftitle))
