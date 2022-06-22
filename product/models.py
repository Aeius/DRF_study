from datetime import timedelta
from operator import mod
from statistics import mode
from django.db import models
from user.models import User as UserModel


# 작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일
class Product(models.Model):
    author = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50, blank=False, null=False)
    thumnail = models.FileField("이미지", upload_to="product/")
    discription = models.TextField("설명")
    add_date = models.DateTimeField("등록일자", auto_now_add=True)
    exposure_start_date = models.DateTimeField("시작일자")
    exposure_end_date = models.DateTimeField("끝일자")