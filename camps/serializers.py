from rest_framework import serializers

from camps.models import Camps, CampInhabitants


class CampsSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = Camps
        fields = '__all__'


class CampInhabitantsSerializer(serializers.ModelSerializer):

    camp = serializers.SerializerMethodField()

    class Meta:

        model = CampInhabitants
        fields = '__all__'

    def validate_camp(self, value):
        return Camps.objects.get(id=self.request.id)

    def get_camp(self, camp):
        return camp.id
