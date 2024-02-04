from django.contrib import admin
from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "question",
        "op1",
        "op2",
        "op3",
        "op4",
        "ans",
        "actual_suggestion",
        "misleading_suggestion",
    )


admin.site.register(Question, QuestionAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ("roll_no", "name", "email")


admin.site.register(User, UserAdmin)


class PromptedAnswersAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "page", "time")


admin.site.register(PromptedAnswers, PromptedAnswersAdmin)


class UnpromptedAnswersAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "page", "time")


admin.site.register(UnpromptedAnswers, UnpromptedAnswersAdmin)


class NoAssistanceAnswersAdmin(admin.ModelAdmin):
    list_display = ("user", "action", "page", "time")


admin.site.register(NoAssistanceAnswers, NoAssistanceAnswersAdmin)
