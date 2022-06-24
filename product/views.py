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
        products = ProductModel.objects.filter(
            Q(exposure_end_date__gte=today, is_active=True) 
            | Q(author=request.user)
        )
        serialized_data = ProductInfoSerializer(products, many=True).data

        return Response(serialized_data, status.HTTP_200_OK)

    # 상품 등록
    def post(self, request):
        request.data["author"] = request.user.id
        product_serializer = ProductSerializer(data=request.data)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 상품 수정
    def put(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error" : "없는 상품 입니다."},
                                    status=status.HTTP_400_BAD_REQUEST)

        # request.data['user'].pop() #바꾸고 싶지 않은 데이터는 제외하기
        product_serlizer = ProductSerializer(product, data=request.data, partial=True)
        product_serlizer.is_valid(raise_exception=True)
        product_serlizer.save()
        return Response(product_serlizer.data, status=status.HTTP_200_OK)