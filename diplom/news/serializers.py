from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import serializers

from news.models import New, FavouriteNews

User = get_user_model()


class NewSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())

    class Meta:
        model = New
        fields = ('pk', 'title', 'text', 'image', 'author', 'created')


class FavouriteNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteNews
        fields = ('new', 'user')
