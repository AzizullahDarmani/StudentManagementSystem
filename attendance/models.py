from django.db import models
from students.models import Student
from courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()


    # def __str__(self):
    #     return self.course