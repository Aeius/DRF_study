from rest_framework.response import Response
from rest_framework.views import APIView
from DRF_study.permissions import RegistedMoreThan3MinsUser
from rest_framework import status
from .models import Article as ArticleModel

from DRF_study.serializers import ArticleSerializer

# Create your views here.


class ArticleView(APIView):
    permission_classes = [RegistedMoreThan3MinsUser]
    # 전체 글 조회
    def get(self, request):
        return Response(ArticleSerializer(ArticleModel.objects.all(), many=True).data, status=status.HTTP_200_OK)

    # 글 쓰기
    def post(self, request):
        user = request.user
        request.data["user"] = user.id
        article_serializer = ArticleSerializer(data=request.data)
        article_serializer.is_valid(raise_exception=True)
        article_serializer.save()

        return Response(article_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        return 