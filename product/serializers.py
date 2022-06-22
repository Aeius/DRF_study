from django.db import IntegrityError
from rest_framework import serializers

from product.models import Product as ProductModel

class ProductInfoSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = ProductModel
        fields = ["author", "title", "thumnail",
                  "discription", "add_date", 
                  "exposure_start_date", "exposure_end_date", ]


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ["author", "title", "thumnail",
                  "discription", "add_date", 
                  "exposure_start_date", "exposure_end_date", ]
