from django.urls import path, include
from rest_framework import routers

from news.views import NewViewSet

router = routers.SimpleRouter()
router.register(r'news', NewViewSet)

urlpatterns = [
    path('auth/', include('users.urls')),
    path('', include(router.urls))
]
