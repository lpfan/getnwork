from django.contrib.auth.models import User
from django.db import models


class ApplicationMenuItem(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField()
    author = User()

    post = models.ForeignKey("Post")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)

    tags = models.ManyToManyField(Tag, null=True, blank=True)
    main_menu_item = models.ForeignKey(ApplicationMenuItem)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
