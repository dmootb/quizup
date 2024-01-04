# web/core/tests/api/v1/views/test_views.py

from typing import ClassVar, Optional, Type
from django.test import TestCase
from django.urls import reverse
from rest_framework import status, viewsets
from rest_framework.test import APIClient
from web.core.api.v1.views.core import QuestionViewSet
from web.core.utils.data import Creator

class QuestionViewSetTests(TestCase):
    named_view_base: ClassVar[str] = "api/v1/core/questions/"
    namespace: ClassVar[Optional[str]] = None
    viewset: ClassVar[Type[viewsets.ModelViewSet]] = QuestionViewSet

    @classmethod
    def setUpClass(cls) -> None:
        import django
        django.setup()
        cls.client = APIClient()
        cls.creator = Creator()

    def test_get_questions_with_answers(self):
        # Create a sample question with answers
        question = self.creator.create_question(question_text="Sample Question", category="General")
        self.creator.create_answer(question, answer_text="Option 1", is_correct=True)
        self.creator.create_answer(question, answer_text="Option 2", is_correct=False)
        self.creator.create_answer(question, answer_text="Option 3", is_correct=False)
        self.creator.create_answer(question, answer_text="Option 4", is_correct=False)

        # Get the list of questions with answers
        url = reverse(self.named_view_base, current_app=self.namespace)
        print(url)  # Assuming you have a 'question-list' URL in your QuestionViewSet
        response = self.client.get(url)
        print(response)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data), 1)  # Assuming you expect one question in the response
        # self.assertEqual(len(response.data[0]['answers']), 4)  # Assuming you expect four answers for each question
        # Add more assertions as needed
