from django.db import models

class Riddle(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Reflective Prompt"
        verbose_name_plural = "Reflective Prompts"