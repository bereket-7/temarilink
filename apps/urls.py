from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import StudentViewSet
from apps.academics.views import GradeViewSet
from apps.notifications.views import SMSMessageViewSet

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

class APIRoot(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        return Response({
            'students': reverse('student-list', request=request, format=format),
            'grades': reverse('grade-list', request=request, format=format),
            'sms': reverse('smsmessage-list', request=request, format=format),
            'token_obtain': reverse('token_obtain_pair', request=request, format=format),
            'token_refresh': reverse('token_refresh', request=request, format=format),
        })

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'sms', SMSMessageViewSet)

urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),
    path('', include(router.urls)),
]
