from rest_framework import serializers
from user.models import *
from blog.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "article", "comment"]

class ArticleSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, source="comment_set")
    class Meta:
        model = Article
        fields = ["user", "title", "category", "content", "comment"]

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ["name"]

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = UserProfile
        fields = ["discription", "birthday", "hobby"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    article = ArticleSerializer(many=True, source="article_set")
    class Meta:
        # serializer에 사용될 model, field지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "email", "userprofile", "article"]