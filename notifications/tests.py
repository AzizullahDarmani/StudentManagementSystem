from django.test import TestCase
from notifications.tasks import send_grade_notification

class NotificationTaskTests(TestCase):
    def test_send_grade_notification(self):
        result = send_grade_notification("test@example.com", "Math", "A")
        self.assertEqual(result, "Email sent successfully")
