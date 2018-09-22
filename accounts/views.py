from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.permissions import IsEditable
from accounts.serializers import UsersSerializer
from accounts.serializers import UsersSerializerBasic


class UsersRegister(CreateAPIView):
    """post: Register a user
    """

    queryset = User.objects.all()
    serializer_class = UsersSerializer


class UsersLogin(APIView):
    """Login user
    """

    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        token, created = Token.objects.get_or_create(user=request.user)

        user = Users.objects.get(username=request.user.username)

        content = {
            'name': user.name,
            'token': str(token),
            'username': user.username,
        }

        return Response(content)


class UserInfo(RetrieveUpdateAPIView):
    """Info of user
    get:
    Get info of user
    patch:
    Update info of user
    """

    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, IsEditable)

    lookup_field = 'username'

    def get_queryset(self):
        username = self.kwargs[self.lookup_field]
        user = Users.objects.filter(username=username)
        return user

    def get_serializer_class(self):
        user = Users.objects.get(username=self.request.user.username)

        if user.role == 'admin':
            return UsersSerializer
        else:
            return UsersSerializerBasic
