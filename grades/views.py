from notifications.tasks import send_grade_notification
from .models import Grade
from rest_framework.views import APIView
from rest_framework.response import Response

class GradeCreateView(APIView):
    def post(self, request):
        grade = Grade.objects.create(**request.data)
        send_grade_notification.delay(
            email=grade.student.email,
            course=grade.course.name,
            grade=grade.grade
        )
        return Response({"message": "Grade added and notification sent."})
