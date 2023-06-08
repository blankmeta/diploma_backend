# import datetime
from datetime import datetime

import pytz
from django.contrib.auth import get_user_model
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from events.models import Event, FavouriteEvents, Category

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    icon = Base64ImageField()

    class Meta:
        model = Category
        fields = ('name', 'icon')


class EventSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())
    image = Base64ImageField()

    def validate_time(self, value):
        if value < datetime.now().replace(tzinfo=pytz.utc):
            raise serializers.ValidationError('Time must be in future.')
        return value

    class Meta:
        model = Event
        fields = ('pk', 'title', 'description', 'address', 'image', 'author',
                  'created', 'geo_lat', 'geo_lon', 'time', 'category')
        read_only_fields = ('created', 'author', 'geo_lat', 'geo_lon')


class FavouriteEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteEvents
        fields = ('event', 'user')
