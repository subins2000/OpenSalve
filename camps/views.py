from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from camps.models import Camp
from camps.serializers import CampsSerializer
from help.permissions import IsVolunteer


class Camp(generics.ListCreateAPIView):
    """Get/Add request
    get:
    Get all camps
    post:
    Add a camp
    """

    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsVolunteer,
    )

    serializer_class = CampsSerializer
    queryset = Camp.objects.all()


class ViewCamp(generics.RetrieveAPIView):
    """Get info about a camp
    """
    serializer_class = CampsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        camp = Camp.objects.filter(id=id)
        return camp
