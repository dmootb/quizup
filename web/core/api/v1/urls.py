from django.urls import include, re_path
from rest_framework.routers import SimpleRouter
from web.core.api.v1.views.core import QuestionViewSet

router = SimpleRouter()
router.register(r"question", QuestionViewSet, basename="api/core/v1/question")
print(router.urls)
urlpatterns = [
    re_path(r"^", include(router.urls)),
]
