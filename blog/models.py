from tkinter import CASCADE
from unicodedata import category
from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField("카테고리명",max_length=20)
    discription = models.TextField("설명")
    def __str__(self):
        return self.name


class Article(models.Model):
    #글 작성자, 글 제목, 카테고리, 글 내용
    author = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField()