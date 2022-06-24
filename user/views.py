from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, authenticate, logout
from rest_framework import status

from .serializers import UserSerializer
from .models import User as UserModel

# Create your views here.

class UserAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    
    # 요청을 보낼 method의 이름으로 함수명을 지어 오버라이딩 해서 사용해야함
    # 회원 정보 출력
    def get(self, request):
        user = request.user
        #serializer에 queryset을 인자로 줄 경우(ManyToMany관계일 때) many=True 옵션을 줘야한다.
        serialized_user_data = UserSerializer(user).data
        return Response(serialized_user_data, status=status.HTTP_200_OK)

    # 로그인
    def post(self, request):
        # username = request.data.get('username', '')
        # password = request.data.get('password', '')
        # user = authenticate(request, username=username, password=password)
        user = authenticate(request, **request.data)
        if not user:
            return Response({'error': '아이디와 패스워드를 확인해주세요!'})
        login(request, user)
        return Response({'success': '로그인 성공!'}, status=status.HTTP_200_OK)
        
    # 로그아웃
    def delete(self, request):
        logout(request)
        return Response({'success': '로그아웃 성공!'}, status=status.HTTP_200_OK)


class UserSignAPIView(APIView):
    # 회원 가입
    def post(self, request):
        userSerializer = UserSerializer(data=request.data)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_200_OK)

    # 회원 수정
    def put(self, request):
        userSerializer = UserSerializer(request.user, data=request.data, partial=True)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        return Response(userSerializer.data, status=status.HTTP_200_OK)

    # 회원 탈퇴
    def delete(self, request):
        UserModel.objects.get(id=request.user.id).delete()
        return Response({"success": "회원탈퇴 성공!"}, status=status.HTTP_200_OK)       