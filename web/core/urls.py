# web/core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.v1.views.views import QuestionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
]