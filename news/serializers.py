from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:

        model = News
        fields = '__all__'
