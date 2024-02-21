from django.shortcuts import render
from .models import (
    Question,
    User,
    PromptedAnswers,
    UnpromptedAnswers,
    NoAssistanceAnswers,
    FeedbackForm,
)
from .serializers import (
    QuestionSerializer,
    UserSerializer,
    PromptedAnswersSerializer,
    UnpromptedAnswersSerializer,
    NoAssistanceAnswersSerializer,
    FeedbackAnswersSerializer,
)
from rest_framework import viewsets


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
    serializer_class = UnpromptedAnswersSerializer


class NoAssistanceAnswersViewSet(viewsets.ModelViewSet):
    queryset = NoAssistanceAnswers.objects.all()
    serializer_class = NoAssistanceAnswersSerializer

class FeedbackFormViewSet(viewsets.ModelViewSet):
    queryset = FeedbackForm.objects.all()
    serializer_class = FeedbackAnswersSerializer
