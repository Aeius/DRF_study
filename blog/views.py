from blog.models import Article
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.


class ArticleView(APIView):
    permissions_classes = [permissions.AllowAny]

    def get(self, request):
        user = request.user
        articles = Article.objects.filter(author=user)
        return Response({"titles":articles})