from rest_framework import serializers
from .models import User, Category, Post, Comment

from rest_framework import serializers
from .models import User, Category, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'is_active', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# POST SERIALIZER - two ways to choose the fields
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # ---
        # CUSTOMISED WAY: list exactly the fields you want
        # fields = ['id', 'title', 'content', 'author',
        #           'category', 'is_published', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'