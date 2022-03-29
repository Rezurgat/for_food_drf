from rest_framework import serializers

from .models import Post

class PostListSerializer(serializers.ModelSerializer):
    """Вывод списка постов"""
    class Meta:
        model = Post
        field = ('title', 'post')