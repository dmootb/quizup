
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from web.core.utils.data import Creator
from web.core.models import Question, Answer

class CreatorTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = APIClient()
        cls.creator = Creator()
        cls.question = Creator.create_question("What is the capital of France?", "Geography")
    def test_create_question(self):
        self.assertIsInstance(self.question, Question)
        self.assertEqual(self.question.text, "What is the capital of France?")
        self.assertEqual(self.question.category, "Geography")

    def test_create_answer_with_correct_params(self):
        answer_text = "This is the answer text"
        is_correct = True

        answer = self.creator.create_answer(self.question, answer_text, is_correct)

        self.assertIsInstance(answer, Answer)
        self.assertEqual(answer.question, self.question)
        self.assertEqual(answer.text, answer_text)
        self.assertEqual(answer.is_correct, is_correct)


    def test_create_answer_with_incorrect_params(self):
        with self.assertRaises(TypeError):
            Creator.create_answer(None, "This is the answer text", True)

        with self.assertRaises(TypeError):
            Creator.create_answer(self.question, None, True)

        with self.assertRaises(TypeError):
            Creator.create_answer(self.question, "This is the answer text", None)