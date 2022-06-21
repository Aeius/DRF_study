from datetime import timedelta
from django.utils import timezone
from blog.models import Article
from rest_framework.response import Response
from rest_framework.views import APIView
from DRF_study.permissions import RegistedMoreThan3MinsUser
from rest_framework import status

# Create your views here.


class ArticleView(APIView):
    permission_classes = [RegistedMoreThan3MinsUser]
    
    def get(self, request):
        articles = Article.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now()).order_by('-start_date')
        title_list = []
        for article in articles:
            title_list.append(article.title)

        return Response(title_list, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        title = request.data.get("title", "")
        category = request.data.get("category", "")
        content = request.data.get("content", "")
        end_date = timezone.now() + timedelta(days=5)
        if len(title) < 5:
            return Response({'error':'제목은 5자 이상입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(content) < 20:
            return Response({'error':'내용은 20자 이상입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if not category:
            return Response({'error':'카테고리를 지정해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        new_article = Article.objects.create(user=user, title=title,content=content, end_date=end_date)
        new_article.category.add(category)

        return Response({'success': '게시글 작성완료!',
                         'title': title,
                         'content': content,
                         'category': category},
                          status=status.HTTP_200_OK)