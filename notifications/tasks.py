from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_grade_notification(email, course, grade):
    subject = 'Grade Update'
    message = f'Your grade for {course} is {grade}.'
    send_mail(subject, message, 'admin@example.com', [email])
    return "Email sent successfully"
