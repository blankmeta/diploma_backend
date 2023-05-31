from django.contrib import admin

from news.models import New, FavouriteNews


@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created')


@admin.register(FavouriteNews)
class FavouriteNewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'new')
