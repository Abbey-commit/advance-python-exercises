from django.db import models
from django.contrib.auth.models import User
from riddles.models import Riddle

class Mood(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mood"
        verbose_name_plural = "Moods"

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Riddle, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    mood = models.ForeignKey(Mood, on_delete=models.SET_NULL, null=True)
    sentiment_score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s entry on {self.created_at}"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"