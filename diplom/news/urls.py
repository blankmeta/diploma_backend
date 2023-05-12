from rest_framework import routers

from news.views import NewViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'news', NewViewSet)

urlpatterns = router.urls
