from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from help.serializers import RequestsSerializer


class AddRequest(generics.CreateAPIView):
    serializer_class = RequestsSerializer
