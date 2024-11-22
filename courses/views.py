from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course

class CourseListView(APIView):
    def get(self, request):
        cached_courses = cache.get('courses')
        if cached_courses is None:
            courses = Course.objects.all()
            cached_courses = list(courses.values())
            cache.set('courses', cached_courses, timeout=300)  # Cache for 5 minutes
        return Response(cached_courses)
