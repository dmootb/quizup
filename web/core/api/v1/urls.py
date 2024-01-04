from django.urls import include, re_path
from rest_framework.routers import SimpleRouter
from web.core.api.v1.views.core import QuestionViewSet

router = SimpleRouter()
router.register(r'questions', QuestionViewSet, basename="api/core/v1/questions")

urlpatterns = [
    re_path(r"^", include(router.urls)),
]
