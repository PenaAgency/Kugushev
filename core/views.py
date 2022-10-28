from .models import HackerNews
from .serializers import NewsSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework.response import Response


class HackerNewsList(generics.ListAPIView, LimitOffsetPagination):

    queryset = HackerNews.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'

    def get_paginated_response(self, data):
        return Response(data)
