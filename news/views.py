from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from news.models import News
from news.permissions import IsAdmin
from news.serializers import NewsSerializer


class NewsView(generics.ListCreateAPIView):
    """Get/Add news
    get:
    Get all news
    post:
    Add a news
    """

    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsAdmin,
    )

    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
