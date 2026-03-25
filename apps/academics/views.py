from rest_framework import viewsets
from apps.academics.models import Grade
from apps.academics.services import process_grade_notification
from .serializers import GradeSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filterset_fields = ['student', 'subject', 'term']
    search_fields = ['student__full_name', 'subject__name']
    ordering_fields = ['score', 'created_at']

    def perform_create(self, serializer):
        grade = serializer.save()
        # Trigger business logic (notification) after successful creation
        process_grade_notification(grade)
