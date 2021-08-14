from django.contrib import admin

from .models import Test, Question, Testrun, TestrunQuestion


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_text', 'test_description', 'pub_date')


class TestrunQuestionInline(admin.TabularInline):
    model = TestrunQuestion


class TestrunAdmin(admin.ModelAdmin):
    inlines = [TestrunQuestionInline]


admin.site.register(Test, TestAdmin)
admin.site.register(Question)
admin.site.register(Testrun, TestrunAdmin)
admin.site.register(TestrunQuestion)
