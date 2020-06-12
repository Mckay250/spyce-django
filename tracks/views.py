from rest_framework import viewsets, status
from .models import Track
from .serializers import TrackSerializer
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'tags', 'key']
    ordering_fields = ['title', 'bpm', 'mp3_price', 'date']
    authentication_classes =  [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | HasAPIKey]

    # def create(self, request, *args, **kwargs):
    #     return Response([], status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)



class SearchViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'tags', 'key']
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | HasAPIKey]
    paginator = None

    def create(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response([], status=status.HTTP_400_BAD_REQUEST)
