from curses import noecho
from turtle import window_height
from django.db import models
from user.models import User as UserModel


# 작성자, 제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일

# 상품 <작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부>
class Product(models.Model):
    author = models.ForeignKey(UserModel, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50, blank=False, null=False)
    thumnail = models.FileField("이미지", upload_to="product/thumnail",)
    description = models.TextField("설명")
    created = models.DateTimeField("등록일자", auto_now_add=True)
    exposure_end_date = models.DateTimeField("끝일자")
    price = models.IntegerField("가격")
    modified = models.DateTimeField("수정일자", auto_now=True)
    is_active = models.BooleanField("활성화여부", default=True)


# 리뷰 <작성자, 상품, 내용, 평점, 작성일>
class Review(models.Model):
    author = models.ForeignKey(UserModel,verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.SET_NULL, null=True)
    content = models.TextField("내용", default="")
    created = models.DateTimeField("작성일", auto_now_add=True)
    rating = models.IntegerField("평점")