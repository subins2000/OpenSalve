from rest_framework import serializers

from collectioncentres.models import CollectionCentre


class CollectionCentreSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = CollectionCentre
        fields = '__all__'
