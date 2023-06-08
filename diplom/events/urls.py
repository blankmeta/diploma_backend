from rest_framework import routers

from events.views import EventViewSet, CategoryViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'events', EventViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
