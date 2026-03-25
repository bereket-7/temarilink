from rest_framework import viewsets
from apps.students.models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['school', 'grade', 'section']
    search_fields = ['full_name']
    ordering_fields = ['full_name', 'created_at']
