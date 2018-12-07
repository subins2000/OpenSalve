from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from accounts.models import User
from news.models import News


class NewsSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:

        model = News
        fields = '__all__'

    def validate_user(self, value):
        return self.context['request'].user

    def get_user(self, news):
        return self.context['request'].user.username
