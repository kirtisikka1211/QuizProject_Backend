# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PromptedAnswersViewSet(viewsets.ModelViewSet):
    queryset = PromptedAnswers.objects.all()
    serializer_class = PromptedAnswersSerializer

class UnpromptedAnswersViewSet(viewsets.ModelViewSet):
    queryset = UnpromptedAnswers.objects.all()
    print(queryset)
    users= User.objects.all()
    for user in users:
        for entries in queryset:
            if (user.uid == entries.user_id):
                 print(user.id)
                 entries.uid_no= int(user.id)
                 queryset.update(uid_no=entries.uid_no)
                 serializer_class = UnpromptedAnswersSerializer
    serializer_class = UnpromptedAnswersSerializer

class NoAssistanceAnswersViewSet(viewsets.ModelViewSet):
    queryset = NoAssistanceAnswers.objects.all()
    serializer_class = NoAssistanceAnswersSerializer