import imp
from tkinter import N
from tkinter.messagebox import NO
from blog.models import Article
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework import permissions
from DRF_study.permissions import RegistedMoreThan3MinsUser

# Create your views here.


class ArticleView(APIView):
    # permission_classes = [permissions.AllowAny]
    permission_classes = [RegistedMoreThan3MinsUser]
    
    def get(self, request):
        user = request.user
        articles = Article.objects.filter(author=user)
        title_list = []
        for article in articles:
            title_list.append(article.title)

        return Response(title_list)

    def post(self, request):
        user = request.user
        title = request.data.get("title", "")
        category = request.data.get("category", "")
        content = request.data.get("content", "")
        if len(title) < 5:
            return Response({'error':'제목은 5자 이상입니다.'})
        if len(content) < 20:
            return Response({'error':'내용은 20자 이상입니다.'})
        if not category:
            return Response({'error':'카테고리를 지정해주세요.'})
        
        
        new_article = Article.objects.create(user=user, title=title,content=content)
        new_article.category.add(category)

        return Response({'success': '게시글 작성완료!',
                         'title': title,
                         'content': content,
                         'category': category})