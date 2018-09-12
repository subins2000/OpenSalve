from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from help.models import Requests
from help.serializers import RequestsSerializer


class AddRequest(generics.CreateAPIView):
    serializer_class = RequestsSerializer


class ViewRequest(generics.RetrieveAPIView):
    """Get info about a help request
    """

    queryset = Requests.objects.all()
    serializer_class = RequestsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request
