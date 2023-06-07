from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import serializers

from events.models import Event, FavouriteEvents
from news.models import New, FavouriteNews

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Event
        fields = ('pk', 'title', 'description', 'address', 'image', 'author',
                  'created', 'geo_lat', 'geo_lon', 'time')
        read_only_fields = ('created', 'author', 'geo_lat', 'geo_lon')


class FavouriteEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteEvents
        fields = ('event', 'user')
