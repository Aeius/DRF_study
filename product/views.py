from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q
from DRF_study.permissions import RegistedMoreThan3MinsUser

from product.serializers import ProductSerializer
from product.serializers import ProductInfoSerializer
from product.models import Product as ProductModel


class ProductAPIView(APIView):
    permission_classes = [RegistedMoreThan3MinsUser]

    # 상품 목록 출력
    def get(self, request):
        today = datetime.now()
        # 오늘기준으로 노출시작날짜가 이전, 노출종료날짜가 이후 or 로그인된 유저
        products = ProductModel.objects.filter(
            Q(exposure_end_date__gte=today, is_active=True) 
            | Q(author=request.user)
        )
        # serializer에 queryset을 주기 때문에 many=True를 줘야함
        serialized_data = ProductInfoSerializer(products, many=True).data

        return Response(serialized_data, status.HTTP_200_OK)

    # 상품 등록
    def post(self, request):
        # 현재 접속중인 유저의 데이터의 id request.data의 author에 저장
        request.data["author"] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 상품 수정
    def put(self, request, product_id):
        # product/<product_id> 헤더에서 id값을 받아오고 그 상품의 object를 get으로 얻어옴
        try:
            product = ProductModel.objects.get(id=product_id)
        # 해당 상품이 없을 수 도 있기 때문에 try except 문 사용
        except ProductModel.DoesNotExist:
            return Response({"error" : "없는 상품 입니다."},
                                    status=status.HTTP_400_BAD_REQUEST)

        # request.data['user'].pop() #바꾸고 싶지 않은 데이터는 제외하기
        product_serlizer = ProductSerializer(product, data=request.data, partial=True)
        product_serlizer.is_valid(raise_exception=True)
        product_serlizer.save()
        return Response(product_serlizer.data, status=status.HTTP_200_OK)