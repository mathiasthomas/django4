from email import utils
from email.policy import default
from enum import auto
import imp
from statistics import mode
from django.db import models
from django.utils import timezone
#importing build in user model
from django.contrib.auth.models import User


# Create your models here.
#Post model
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED= 'PB','Published'

    title =models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250)
    author = models.ForeignKey(User, on_delete =models.CASCADE, related_name = 'blog_posts')
    body = models.TextField()
    publish =models.DateField(default = timezone.now)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True)
    status = models.CharField(max_length = 2,choices = Status.choices,default=Status.DRAFT)

    #ordering
    class Meta():
        ordering = ['publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
    def __str__(self):
        self.title
