from django.db import models

# Create your models here.

DIFFICULTY_REWARDS = {
    'easy': {'points': 5},
    'medium': {'points': 10},
    'hard': {'points': 20},
}

class Question(models.Model):
    question_text = models.CharField(max_length=255)

    points = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])

    choice_1 = models.CharField(max_length=255)
    choice_2 = models.CharField(max_length=255)
    choice_3 = models.CharField(max_length=255)
    choice_4 = models.CharField(max_length=255)

    correct_choice = models.IntegerField()

    is_premium = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        rewards = DIFFICULTY_REWARDS[self.difficulty]
        self.points = rewards['points']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question_text
