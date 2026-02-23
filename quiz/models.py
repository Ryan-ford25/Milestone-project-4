from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255)

    points = models.IntegerField(default=10)
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], default='easy')

    choice_1 = models.CharField(max_length=255)
    choice_2 = models.CharField(max_length=255)
    choice_3 = models.CharField(max_length=255)
    choice_4 = models.CharField(max_length=255)

    correct_choice = models.IntegerField()

    is_premium = models.BooleanField(default=False)


    def __str__(self):
        return self.question_text
