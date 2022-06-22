from rest_framework import serializers

from product.models import Product
from DRF_study.serializers import UserSerializer

class ProductSerializer(serializers.ModellSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = [
        "user": {'write_only': True}
        "title": {
            'error_messages': {
                'required' : "에러 메세지",
                'invalid' : "알맞은 형식의 이메일을 입력해주세요"
            },
            'required' : True
        }
        ]