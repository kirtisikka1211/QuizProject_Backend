from django.db import models
from django.db.models.deletion import CASCADE

# create models for a quiz app
class Question(models.Model):
    id = models.AutoField(primary_key= True)
    question = models.TextField(null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    actual_suggestion = models.TextField(null=True)
    misleading_suggestion= models.TextField(null=True)

class User(models.Model):
    uid = models.CharField(max_length=200, unique=True)

class PromptedAnswers(models.Model):
    user_id = models.IntegerField(null=False)
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
    page = models.CharField(null=False, max_length=200, default="Null")
    time = models.TimeField(default='00:00:00')

class UnpromptedAnswers(models.Model):
    user_id = models.IntegerField(null=False)
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
    page = models.CharField(null=False, max_length=200, default="Null")
    time = models.TimeField(default='00:00:00')

class NoAssistanceAnswers(models.Model):
    user_id = models.IntegerField(null=False)
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
    page = models.CharField(null=False, max_length=200, default="Null")
    time = models.TimeField(default='00:00:00')
