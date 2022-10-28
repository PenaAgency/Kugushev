from .models import HackerNews
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackerNews
        fields = ['id', 'url', 'title', 'created']


class PostSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
