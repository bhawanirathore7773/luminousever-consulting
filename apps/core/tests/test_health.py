from django.test import TestCase
class HealthTest(TestCase):
    def test_health(self):
        response=self.client.get("/health/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json()["status"],"ok")
    def test_not_found_is_branded(self):
        response=self.client.get("/definitely-not-a-real-page/")
        self.assertEqual(response.status_code,404)
