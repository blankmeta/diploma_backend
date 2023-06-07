import os

from dadata import Dadata
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    title = models.CharField(max_length=1024)
    description = models.CharField(max_length=5096, null=True)
    address = models.CharField(max_length=2048)
    geo_lat = models.FloatField(null=True)
    geo_lon = models.FloatField(null=True)
    image = models.ImageField(null=True, upload_to='events/images/')
    time = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def _get_address_data(raw_address):
        token = os.getenv('DADATA_TOKEN',
                          default='93337b525d173268376ef9820e3c8261e1db7281')
        secret = os.getenv('DADATA_SECRET',
                           default='ac3eb6269a755f78e587835418b53e6fadb3bc25')
        dadata = Dadata(token, secret)
        return dadata.clean('address', raw_address)

    def _set_address(self, info):
        self.address = info.get('result')

    def _set_coordinates(self, info):
        self.geo_lat = info.get('geo_lat')
        self.geo_lon = info.get('geo_lon')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        address_info = self._get_address_data(self.address)
        self._set_address(address_info)
        self._set_coordinates(address_info)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        ordering = ('created',)


class FavouriteEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favourite_events')
    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='favourited')

    def __str__(self):
        return f'{self.user} | {self.event}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event'],
                                    name='favourite event unique validator')
        ]
