from rest_framework import serializers
from .models import Venue, Event, EventSession

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


class EventSessionSerializer(serializers.ModelSerializer):
    venue = VenueSerializer()

    class Meta:
        model = EventSession
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    sessions = EventSessionSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'