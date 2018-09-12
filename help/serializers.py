from rest_framework import serializers

from help.models import Requests


class RequestsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = '__all__'


class StatusRequestsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = ('status',)
