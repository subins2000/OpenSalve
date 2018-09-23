from rest_framework import serializers

from accounts.models import User
from help.models import Requests, Comments


class RequestsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = '__all__'


class RequestsStatusSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = ('status',)


class RequestComments(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    user = serializers.SerializerMethodField()

    class Meta:

        model = Comments
        fields = '__all__'

    def get_user(self, comment):
        try:
            return User.objects.get(pk=comment.user).username
        except User.DoesNotExist:
            return None
