from rest_framework import serializers

from camps.models import Camps


class CampsSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = Camps
        fields = '__all__'
