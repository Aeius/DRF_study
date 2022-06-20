from tkinter import N
from tkinter.messagebox import NO
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
        title_list = []
        for article in articles:
            title_list.append(article.title)

        return Response(title_list)

    def post(self, request):
        title = request.data.get("title", "")
        category = request.data.get("category", "")
        content = request.data.get("content", "")
        
        if len(title) < 5:
            return Response({'error':'제목은 5자 이상입니다.'})
        if len(content) < 20:
            return Response({'error':'내용은 20자 이상입니다.'})
        if not category:
            return Response({'error':'카테고리를 지정해주세요.'})
        
        return Response({'success': '게시글 작성완료!',
                         'title': title,
                         'content': content,
                         'category': category})