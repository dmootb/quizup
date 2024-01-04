"""
This module contains utility functions for working with data in the web application.
"""

from web.core.models import Question, Answer

class Creator:
    @classmethod
    
    def create_question(cls, question_text, category):
        """
        Creates a new question in the database.

        Args:
            question_text (str): The text of the question.
            category (str): The category of the question.

        Returns:
            Question: The created question.
        """
        return Question.objects.create(text=question_text, category=category)

    @classmethod
    def create_answer(cls, question, answer_text, is_correct):
        """
        Creates a new answer in the database.

        Args:
            question (Question): The question to which the answer belongs.
            answer_text (str): The text of the answer.
            is_correct (bool): A boolean indicating whether the answer is correct.

        Returns:
            Answer: The created answer.
        """
        return Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)
