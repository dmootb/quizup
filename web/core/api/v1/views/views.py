# web/core/views.py
from rest_framework import viewsets
from web.core.models import Question
from web.core.api.v1.serializers.serializers import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
