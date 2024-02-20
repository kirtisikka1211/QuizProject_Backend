from django.db import models
from django.db.models.deletion import CASCADE


class User(models.Model):
    roll_no = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)


class Question(models.Model):
    question = models.TextField(null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    actual_suggestion = models.TextField(null=True)
    misleading_suggestion = models.TextField(null=True)


class PromptedAnswers(models.Model):
    user = models.CharField(max_length=200, null=True)
    action = models.CharField(
        choices=[
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("Start", "Start"),
            ("End", "End"),
            ("Prompt", "Prompt"),
            ("Continue", "Continue"),
        ],
        default="Null",
        max_length=10,
    )
    page = models.CharField(max_length=200, default="Null")
    time = models.TimeField(default="00:00:00")
    date= models.DateField(auto_now_add=True)


class UnpromptedAnswers(models.Model):
    user = models.CharField(max_length=200, null=True)
    action = models.CharField(
        choices=[
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("Start", "Start"),
            ("End", "End"),
            ("Prompt", "Prompt"),
            ("Continue", "Continue"),
        ],
        default="Null",
        max_length=10,
    )
    page = models.CharField(max_length=200, default="Null")
    time = models.TimeField(default="00:00:00")
    date= models.DateField(auto_now_add=True)


class NoAssistanceAnswers(models.Model):
    user = models.CharField(max_length=200, null=True)
    action = models.CharField(
        choices=[
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
            ("Start", "Start"),
            ("End", "End"),
            ("Continue", "Continue"),
        ],
        default="Null",
        max_length=10,
    )
    page = models.CharField(max_length=200, default="Null")
    time = models.TimeField(default="00:00:00")
    date= models.DateField(auto_now_add=True)
