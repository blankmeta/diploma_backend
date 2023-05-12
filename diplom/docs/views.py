from rest_framework.permissions import AllowAny
from drf_yasg2.views import get_schema_view as get_schema_view_2_0
from drf_yasg2 import openapi


TITLE = 'diplom_backend'
DEFAULT_VERSION = '0.0.1'
PERMISSION_CLASSES = (AllowAny, )

schema_view_v2 = get_schema_view_2_0(
    openapi.Info(
        title=TITLE,
        default_version=DEFAULT_VERSION,
    ),
    public=True,
    permission_classes=PERMISSION_CLASSES,
)
