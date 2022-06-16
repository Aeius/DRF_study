import imp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, authenticate, logout
from user.models import User

# Create your views here.

class UserAPIView(APIView):
    permissions_classes = [permissions.AllowAny]
    
    # 요청을 보낼 method의 이름으로 함수명을 지어 오버라이딩 해서 사용해야함
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)

        if not user:
            return Response({'error': '아이디와 패스워드를 확인해주세요!'})
        login(request, user)
        return Response({'success': '로그인 성공!'})
    
    def delete(self, request):
        logout(request)
        return Response({'success': '로그아웃 성공!'})
            