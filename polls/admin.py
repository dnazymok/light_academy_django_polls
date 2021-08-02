from django.contrib import admin

from .models import Test, Question


class ChoiceInline(admin.TabularInline):
    model = Question
    extra = 3


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_text', 'test_description', 'pub_date')
    inlines = [ChoiceInline]


admin.site.register(Test, TestAdmin)
