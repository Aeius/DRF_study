from rest_framework import serializers
from user.models import *
from blog.models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user", "article", "comment"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "discription"]

class ArticleSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True, source="comment_set")
    def get_category(self, obj):
         return obj.category.name
    class Meta:
        model = Article
        fields = ["user", "title", "category", "content", "comment"]
        read_only_fields = ["category"]

