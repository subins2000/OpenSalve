from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from collectioncentres.models import CollectionCentre
from collectioncentres.serializers import *
from help.permissions import IsVolunteer


class CollectionCentre(generics.ListCreateAPIView):
    """Get/Add collection centre
    get:
    Get all collection centres
    post:
    Add a collection centre
    """

    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsVolunteer,
    )

    serializer_class = CollectionCentreSerializer
    queryset = CollectionCentre.objects.all()


class CollectionCentreView(generics.RetrieveAPIView):
    """Get info about a collection centre
    """
    serializer_class = CollectionCentreSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        collection_centre = CollectionCentre.objects.filter(id=id)
        return collection_centre


class CollectionCentreStockView(generics.ListCreateAPIView):
    """Get info about stock in a collection centre
    get:
    Get information about stock in collection centre
    post:
    Add information about stock item needed
    """
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsVolunteer,
    )

    serializer_class = CollectionCentreStockSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        stock = CollectionCentreStock.objects.filter(centre=id)
        return stock
