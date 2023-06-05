from datetime import timedelta, datetime

from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (CreateModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from diplom.tasks import soon_event_email
from news.models import New, FavouriteNews
from news.serializers import NewSerializer, FavouriteNewsSerializer


class NewViewSet(CreateModelMixin,
                 RetrieveModelMixin,
                 UpdateModelMixin,
                 DestroyModelMixin,
                 ListModelMixin,
                 GenericViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer

    @action(['post', 'delete'], detail=True)
    def favourite(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                obj = FavouriteNews.objects.create(new=self.get_object(),
                                                   user=request.user)
                soon_event_email.apply_async(
                    (self.request.user.id, 123),
                    eta=datetime.now() + timedelta(minutes=1))
            except IntegrityError as e:
                return Response(data='You already has this new in favourites',
                                status=status.HTTP_400_BAD_REQUEST)
            data = FavouriteNewsSerializer(obj).data
            return Response(data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            try:
                FavouriteNews.objects.get(new=self.get_object(),
                                          user=request.user).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except FavouriteNews.DoesNotExist:
                return Response(data="You don't have this new in favourites",
                                status=status.HTTP_400_BAD_REQUEST)

    @action(['get'], detail=False)
    def favourited(self, request, *args, **kwargs):
        queryset = New.objects.filter(favourited__user=request.user)
        data = self.serializer_class(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
