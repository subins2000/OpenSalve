from rest_framework import serializers

from help.models import Requests, Comments


class RequestsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = '__all__'


class StatusRequestsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = ('status',)

class RequestComments(serializers.ModelSerializer):

    class Meta:

        model = Comments
        fields = '__all__'
