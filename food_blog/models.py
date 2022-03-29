from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey #для создания вложенности будущих категорий


"""Создание модели категорий"""
class Category(MPTTModel):
    title = models.CharField(max_length=100) #name
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)#null=True, blank=True для необязательных полей

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100) #name
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class Post(models.Model):
    post_author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='new_folder')
    post = models.TextField()
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
    when_create = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    slug = models.SlugField(max_length=200, default=0, unique = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_recipe(self):
        return self.recipe.all()

    def get_comments(self):
        return self.comment.all()

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    serve = models.CharField(max_length=100)
    prep_time = models.PositiveIntegerField(default=0)
    cooking_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    cooking_steps = RichTextField()
    post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True)

class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='')
    website = models.CharField(max_length=100, blank=True, null=True)
    comment_message = models.TextField(max_length=256)
    when_create = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)






