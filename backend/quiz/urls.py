from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router
router = DefaultRouter()

# Register the ItemViewSet with the router
router.register(r'questions', QuestionViewSet)
router.register(r'users', UserViewSet)
router.register(r'prompted', PromptedAnswersViewSet)
router.register(r'unprompted', UnpromptedAnswersViewSet)
router.register(r'noassistance', NoAssistanceAnswersViewSet)

# Define your API URL patterns
urlpatterns = [
    # Include the default router's generated URL patterns
    path('api/', include(router.urls)),
]
