from django.test import TestCase
from .models import AssessmentSubmission
class AssessmentTests(TestCase):
    def test_incomplete_submission_rejected(self):
        r=self.client.post("/assessment/submit/",{"name":"Test","email":"test@example.com","answers":"{}"})
        self.assertEqual(r.status_code,400)
        self.assertEqual(AssessmentSubmission.objects.count(),0)
    def test_score_is_server_calculated(self):
        answers='{"erp":4,"integration":4,"data":4,"cloud":4,"ux":4,"governance":4,"change":4,"operations":4}'
        r=self.client.post("/assessment/submit/",{"name":"Test","email":"test@example.com","answers":answers,"score":0})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["percentage"],100)
        self.assertEqual(AssessmentSubmission.objects.get().score,32)
