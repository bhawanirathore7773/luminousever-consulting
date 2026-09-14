import pytest
from apps.contact.models import Lead

@pytest.mark.django_db
def test_contact_submission(client):
    response=client.post("/contact/",{"name":"Test User","email":"test@example.com","company":"Example","phone":"","message":"Hello"})
    assert response.status_code==302
    assert Lead.objects.filter(email="test@example.com").exists()