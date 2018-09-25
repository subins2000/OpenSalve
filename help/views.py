from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from help.models import Requests, Comments
from help.permissions import IsVolunteer
from help.serializers import RequestsStatusSerializer, RequestsSerializer
from help.serializers import RequestCommentsRead, RequestCommentsWrite


class RequestAdd(generics.CreateAPIView):
    serializer_class = RequestsSerializer


class RequestView(generics.RetrieveAPIView):
    """Get info about a help request
    """
    serializer_class = RequestsSerializer

    lookup_url_kwarg = 'id'

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request


class RequestStatus(generics.RetrieveUpdateAPIView):
    """Get/Set status of request
    get:
    Get status of request
    patch:
    Set status of request
    """
    serializer_class = RequestsStatusSerializer

    lookup_url_kwarg = 'id'

    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsVolunteer,
    )

    def get_queryset(self):
        id = self.kwargs.get(self.lookup_url_kwarg)
        request = Requests.objects.filter(id=id)
        return request


class RequestComments(generics.ListCreateAPIView):
    """Get/Add comments of/to request
    get:
    Get all comments of request
    post:
    Add a comment to request
    """

    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    queryset = Comments.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RequestCommentsWrite

        return RequestCommentsRead
