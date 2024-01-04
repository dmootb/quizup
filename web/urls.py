from django.urls import re_path, include
from web.core.api.v1 import urls as apicore_v1_urls


urlpatterns = [
    re_path(r"^api/v1/core/", include(apicore_v1_urls)),
]
