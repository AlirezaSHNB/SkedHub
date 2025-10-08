from rest_framework import viewsets
from .models import Venue, Event, EventSession
from .serializers import VenueSerializer, EventSerializer, EventSessionSerializer

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventSessionViewSet(viewsets.ModelViewSet):
    queryset = EventSession.objects.all()
    serializer_class = EventSessionSerializer
