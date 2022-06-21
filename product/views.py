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


class ProductAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        product_serializer = serializers.BaseSerializer(data=request.user)
        if product_serializer.is_vaild():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        product_serlizer = serializers.BaseSerializer(request.data, data=request.user, partial=True)
        product_serlizer.is_valid(raise_exception=True)
        product_serlizer.save()
        return Response(product_serlizer.data, status=status.HTTP_200_OK)