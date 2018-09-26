from rest_framework import serializers

from camps.models import Camp


class CampsSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = Camp
        fields = '__all__'
