from django.db import models
from django.contrib.auth.models import User
from quiz.models import Question
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    practice_timer_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} Profile"

class UserAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='attempts')
    selected_choice = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
    points_awarded = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'question')  # Ensure one attempt per user per question
        ordering = ['-timestamp']  # Order attempts by most recent first

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text} - {'Correct' if self.is_correct else 'Incorrect'}"