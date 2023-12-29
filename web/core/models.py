from django.core.exceptions import ValidationError
from django.db import models

class Question(models.Model):
    # The text of the question
    text = models.TextField()

class Answer(models.Model):
    # The question to which this answer belongs
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    
    # The text of the answer
    text = models.CharField(max_length=255)

    # Indicates whether this answer is correct or not
    is_correct = models.BooleanField(default=False)

    def clean(self):
        # Check if the question already has four answers
        if self.question.answers.count() >= 4:
            raise ValidationError('A question can have at most four answers.')
    
    class Meta:
        # Adding a unique constraint to ensure only one correct answer per question
        constraints = [
            models.UniqueConstraint(fields=['question'], condition=models.Q(is_correct=True), name='unique_correct_answer'),
        ]
