from django.contrib import admin

from .models import Test, Question, Testrun, TestrunQuestion


class ChoiceInline(admin.TabularInline):
    model = Test.questions.through
    extra = 3


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_text', 'test_description', 'pub_date')
    inlines = [ChoiceInline]


class TestrunQuestionInline(admin.TabularInline):
    model = TestrunQuestion


class TestrunAdmin(admin.ModelAdmin):
    inlines = [TestrunQuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Testrun, TestrunAdmin)
admin.site.register(TestrunQuestion)
