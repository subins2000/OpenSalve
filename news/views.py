from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

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


class NewsInfo(generics.RetrieveUpdateAPIView):
    """Get info about a help request
    """
    serializer_class = NewsSerializer

    lookup_url_kwarg = 'id'

    permission_classes = (
        IsAdmin,
    )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        news = News.objects.filter(id=id)
        return news

    def delete(self, request, *args, **kwargs):
        id = self.kwargs.get(self.lookup_url_kwarg)
        try:
            news = News.objects.get(id=id).delete()
            return Response(
                None,
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                None,
                status=status.HTTP_404_NOT_FOUND
            )
