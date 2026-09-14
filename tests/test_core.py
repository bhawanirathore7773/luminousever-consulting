import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home(client):
    response=client.get(reverse("home"))
    assert response.status_code==200
    assert "Luminousever" in response.content.decode()

@pytest.mark.django_db
def test_health(client):
    response=client.get("/health/")
    assert response.status_code==200
    assert response.json()["status"]=="ok"