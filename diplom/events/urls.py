from rest_framework import routers

from events.views import EventViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'events', EventViewSet)

urlpatterns = router.urls
