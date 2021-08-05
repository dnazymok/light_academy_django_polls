from django.contrib import admin

from .models import Test, Question, Testrun, TestrunQuestion


class ChoiceInline(admin.TabularInline):
    model = Test.questions.through
    extra = 3


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_text', 'test_description', 'pub_date')
    inlines = [ChoiceInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Testrun)
admin.site.register(TestrunQuestion)
