from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from camps.models import Camps, CampInhabitants
from camps.serializers import CampsSerializer, CampInhabitantsSerializer
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
    queryset = Camps.objects.all()


class CampView(generics.RetrieveAPIView):
    """Get info about a camp
    """
    serializer_class = CampsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        camp = Camps.objects.filter(id=id)
        return camp


class CampInhabitantsView(generics.ListCreateAPIView):
    """Get/Add inhabitant
    get:
    Get all inhabitants in camp
    post:
    Add a inhabitant to camp
    """

    serializer_class = CampInhabitantsSerializer
    lookup_url_kwarg = 'id'

    def perform_create(self, serializer):
        id = self.kwargs.get(self.lookup_url_kwarg)
        serializer.save(camp=Camps.objects.get(id=id))

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        camp = CampInhabitants.objects.filter(camp=id)
        return camp
