from django.contrib import admin
from .models import(Story, Question, Option)
# Register your models here.



class OptionInline(admin.TabularInline):
    model = Option
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date",]
    search_fields = ["question_text"]
    filter_horizontal = ()

    fieldsets = [
        ('Story',               {'fields': ['story']}),
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [OptionInline]


class StoryAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "pub_date",]
    search_fields = ["title", "author", "pub_date"]
    filter_horizontal = ()

admin.site.register(Story, StoryAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Option)
