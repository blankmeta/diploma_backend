from django.contrib import admin

from events.models import Event, FavouriteEvents, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'address', 'geo_lat', 'geo_lon',
                    'category', 'time', 'author', 'created')


@admin.register(FavouriteEvents)
class FavouriteEventsAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
