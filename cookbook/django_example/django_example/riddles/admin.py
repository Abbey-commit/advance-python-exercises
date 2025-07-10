from django.contrib import admin
from .models import Riddle, Option


class OptionInline(admin.TabularInline):
    model = Option
    extra = 2 # Show 2 empty option fields by default
    fields = ('text', 'is_correct')
    min_num = 2 # require at least 2 options
    max_num = 4 # Limit to 4 options
    verbose_name = "Rresponse Option"
    verbose_name_plural = "Response Options"

class RiddleAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('text', 'created_at', 'option_count',)
    list_filter = ('created_at',)
    search_fields = ('text',)
    fields = ('text',)
    verbose_name = "Reflective Prompt"
    verbose_name_plural = "Reflective Prompts"

    def option_count(self, obj):
        return obj.option_set.count()
    option_count.short_description = "Number of Options"


admin.site.register(Riddle, RiddleAdmin)
admin.site.unregister(Option) # Remove standalone Option admin to avoid confusion