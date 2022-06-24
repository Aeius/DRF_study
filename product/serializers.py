from django.utils import timezone
from rest_framework import serializers

from django.db.models import Avg

from product.models import Product as ProductModel
from product.models import Review as ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return obj.author.fullname

    class Meta:
        model = ReviewModel
        fields = ["author", "product", "content", "created", "rating", ]

class ProductInfoSerializer(serializers.ModelSerializer):
    # 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
    review = serializers.SerializerMethodField()
    def get_review(self, obj):
        # 해당 게시물에 달린 리뷰들을 전부 다 가져옴
        reviews = obj.review_set
        # 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
        return {
            "last_review": ReviewSerializer(reviews.last()).data,
            "average_rating": reviews.aggregate(avg=Avg("rating"))["avg"]
        }

    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = ProductModel
        fields = ["author", "title", "thumnail",
                  "description", "created", 
                  "exposure_end_date", "review" ]


class ProductSerializer(serializers.ModelSerializer):
    # 노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없도록
    def validate(self, data):
        end_date = data.get("exposure_end_date", "")
        # end_date 가 DatetiemField 이기 때문에! django.utils 의 timezone을 써야함!
        # end_date 잇고! 현재보다 end_date가 과거 일 경우 error 출력
        if  end_date and timezone.now() > end_date:
            raise serializers.ValidationError(
                detail= {"error": "노출 일자가 종료되었습니다."}
            )
        return data

    def create(self, validated_data):
        #상품 설명의 마지막에 "<등록 일자>에 등록된 상품입니다." 라는 문구를 추가해주세요
        # 우선 검증이 끝난 데이터들을 Model에 다 맞게 담고
        product = ProductModel(**validated_data)
        # 세이브를 먼저 한번해야 product.created가 생기게 하기 위함
        product.save()
        # product.created를 원하는 형식으로 조정한뒤 다시 save()
        product.description += f"\n\n{product.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
        product.save()

        return product       

    def update(self, instance, validated_data):
        # 수정하였을 때 상품 설명 마지막에 <등록일자>에 등록된 상품이 수정되도록
        # dict 형태인 validated_data를 풀어서 쓰기 위해 items()함수로 for문 돌리기
        for key, value in validated_data.items():
            # 상품설명만 바꿔야되기 때문에 key 가 description 인 경우에만한에서
            if key == "description":
                # value에 created 그대로 집어넣기
                value += f"\n\n{instance.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
            setattr(instance, key, value)
        instance.save() # save한번해야지 modified 값을 가져올 수 있다

        instance.description = f"{instance.modified.replace(microsecond=0, tzinfo=None)}에 수정 되었습니다. \n" + instance.description
        instance.save()                             
        return instance

    class Meta:
        model = ProductModel
        fields = ["author", "title", "thumnail",
                  "description", "created", "price",
                  "exposure_end_date", "modified", ]

        


        
