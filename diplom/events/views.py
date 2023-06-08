from datetime import datetime, timedelta

from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, \
    UpdateModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from diplom.permissions import IsAdminUserOrReadOnly
from diplom.tasks import soon_event_email
from events.models import Event, FavouriteEvents, Category
from events.serializers import EventSerializer, FavouriteEventsSerializer, \
    CategorySerializer


class EventViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   DestroyModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(['post', 'delete'], detail=True)
    def favourite(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:
                obj = FavouriteEvents.objects.create(event=self.get_object(),
                                                     user=request.user)
                soon_event_email.apply_async(
                    (self.request.user.id, obj.id),
                    eta=self.get_object().time - timedelta(
                        minutes=1) - timedelta(hours=3))
            except IntegrityError:
                return Response(
                    data='You already has this event in favourites',
                    status=status.HTTP_400_BAD_REQUEST)
            data = FavouriteEventsSerializer(obj).data
            return Response(data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            try:
                FavouriteEvents.objects.get(event=self.get_object(),
                                            user=request.user).delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except FavouriteEvents.DoesNotExist:
                return Response(data="You don't have this event in favourites",
                                status=status.HTTP_400_BAD_REQUEST)

    @action(['get'], detail=False)
    def favourited(self, request, *args, **kwargs):
        queryset = Event.objects.filter(favourited__user=request.user)
        data = self.serializer_class(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class CategoryViewSet(CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin,
                      ListModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
