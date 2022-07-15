from rest_framework import serializers

from .models import User as UserModel
from .models import UserProfile as UserProfileModel
from .models import Hobbies as HobbiesModel


class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        user_list = []
        for user_profile in obj.userprofile_set.all():
            user_list.append(user_profile.user.username)

        return user_list

    class Meta:
        model = HobbiesModel
        fields = ["name", "same_hobby_users"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = UserProfileModel
        fields = ["discription", "birthday", "hobby"]

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        # 패스워드 암호화를 위해서 패스워드만 분리
        password = validated_data.pop("password", "")
        # 유저 모델에 나머지 데이터 세팅
        user = UserModel(**validated_data)
        # 패스워드 암호화하여 유저모델에 세팅
        user.set_password(password)
        # 유저 정보 DB에 저장
        user.save()
        return user

    userprofile = UserProfileSerializer(read_only=True)
    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username","password", "fullname", "email", "userprofile", ]
        extra_kwargs = {
                  "password": {"write_only": True}
        }