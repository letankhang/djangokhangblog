from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        from datetime import datetime

        slugify_string = slugify(self.title)
        time = datetime.now()
        time = "".join(str(time).split(".", ))

        self.slug = slugify_string + time[17:]
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

