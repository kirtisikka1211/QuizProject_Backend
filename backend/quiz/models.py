from django.db import models
from django.db.models.deletion import CASCADE


from django.db import models

class User(models.Model):
    roll_no = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=200,null=True)
    age = models.IntegerField(null=True)  # Assuming age is stored as an integer
    degree = models.CharField(max_length=200,null=True)  # Corrected field name to lowercase
    uni = models.CharField(max_length=200,null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2,null=True)  # CGPA can have decimal values
    

    





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
    date = models.DateField(default="0001-01-01")
    


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
    date = models.DateField(default="0001-01-01")


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
    date = models.DateField(default="0001-01-01")

# class FeedbackForm(models.Model):



