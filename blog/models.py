from datetime import timedelta
from tkinter import CASCADE
from tracemalloc import start
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
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    content = models.TextField("글내용")
    start_date = models.DateTimeField("시작날짜", auto_now_add=True)
    end_date = models.DateTimeField("끝날짜")
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)
    comment = models.TextField("댓글내용")
    def __str__(self):
        return (f"{self.user} / {self.article} / {self.comment}")