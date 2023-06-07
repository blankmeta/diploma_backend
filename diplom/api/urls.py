from django.urls import path, include
from rest_framework import routers

from events.views import EventViewSet
from news.views import NewViewSet

router = routers.SimpleRouter()
router.register(r'news', NewViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('auth/', include('users.urls')),
    path('', include(router.urls))
]
