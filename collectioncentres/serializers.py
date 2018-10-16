from rest_framework import serializers

from collectioncentres.models import CollectionCentre, CollectionCentreStock


class CollectionCentreSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = CollectionCentre
        fields = '__all__'


class CollectionCentreStockSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = CollectionCentreStock
        fields = '__all__'
