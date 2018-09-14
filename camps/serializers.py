from rest_framework import serializers

from camps.models import Camp


class CampsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Camp
        fields = '__all__'

