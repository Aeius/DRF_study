from functools import partial
import imp
from logging import raiseExceptions
from os import stat
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework import serializers

from product.models import Product
from product.serializers import ProductSerializer


class ProductAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = (FileUploadParser, )

    def post(self, request):
        product_serializer = ProductSerializer(data=request.data, files=request.FILES)
        if product_serializer.is_vaild():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # request.data['user'].pop() #바꾸고 싶지 않은 데이터는 제외하기
        product_serlizer = ProductSerializer(request.data, data=request.user, partial=True)
        product_serlizer.is_valid(raise_exception=True)
        product_serlizer.save()
        return Response(product_serlizer.data, status=status.HTTP_200_OK)