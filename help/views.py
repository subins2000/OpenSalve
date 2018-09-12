from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from help.models import Requests
from help.serializers import StatusRequestsSerializer, RequestsSerializer


class AddRequest(generics.CreateAPIView):
    serializer_class = RequestsSerializer


class ViewRequest(generics.RetrieveAPIView):
    """Get info about a help request
    """
    serializer_class = RequestsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request


class StatusRequest(generics.RetrieveUpdateAPIView):
    """Get/Set status of request
    get:
    Get status of request
    patch:
    Set status of request
    """
    serializer_class = StatusRequestsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request
