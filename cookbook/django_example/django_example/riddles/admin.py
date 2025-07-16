from django.contrib import admin
from .models import Riddle

class RiddleAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('text',)
    fields = ('text',)
    verbose_name = "Reflective Prompt"
    verbose_name_plural = "Reflective Prompts"

admin.site.register(Riddle, RiddleAdmin)