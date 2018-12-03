from rest_framework import serializers

from accounts.models import User
from help.models import Requests, Comments


class RequestsSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = '__all__'

    def validate_source(self, source):
        sources = [
            None,
            'me',
            'fb',
            'wa',
            'insta',
            'call',
        ]

        if (source not in sources):
            raise serializers.ValidationError('Invalid source value')

        return source


class RequestsStatusSerializer(serializers.ModelSerializer):

    class Meta:

        model = Requests
        fields = ('status',)

    def validate_status(self, status):
        if (status not in ['pending', 'inprogress', 'resolved']):
            raise serializers.ValidationError('Invalid status value')
        return status


class RequestCommentsRead(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:

        model = Comments
        fields = '__all__'

    def get_user(self, comment):
        try:
            return User.objects.get(pk=comment.user).username
        except User.DoesNotExist:
            return None


class RequestCommentsWrite(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:

        model = Comments
        fields = '__all__'
