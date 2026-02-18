from django.db import models
from django.contrib.auth.models import User
from quiz.models import Question

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    is_premium = models.BooleanField(default=False)
    practice_timer_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class UserAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choice = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    points_awarded = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text} - {'Correct' if self.is_correct else 'Incorrect'}"