from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        allow_blank=False,
        label="Email Address",
        max_length=100,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'name')

        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserSerializerBasic(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'name')
