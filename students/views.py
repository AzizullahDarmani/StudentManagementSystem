from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from users.permissions import IsAdmin

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdmin]



import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student

logger = logging.getLogger(__name__)

class StudentListView(APIView):
    def get(self, request):
        logger.info("Fetching student list")
        students = Student.objects.all()
        return Response({'students': list(students.values())})
