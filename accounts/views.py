from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from accounts.models import Users
from accounts.serializers import UsersSerializer


class UsersRegister(CreateAPIView):

    queryset = Users.objects.all()
    serializer_class = UsersSerializer
