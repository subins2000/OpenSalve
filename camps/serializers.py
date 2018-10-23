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

    camp = serializers.HiddenField(
        default=''
    )

    class Meta:

        model = CampInhabitants
        fields = '__all__'

    def validate_camp(self, camp):
        self.camp = serializers.HiddenField(
            default=self.context.get('camp_id')
        )
