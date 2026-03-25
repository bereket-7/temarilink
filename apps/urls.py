from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentViewSet
from apps.academics.views import GradeViewSet
from apps.notifications.views import SMSMessageViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'sms', SMSMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
