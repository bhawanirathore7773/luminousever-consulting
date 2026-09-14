from django.urls import path
from .views import listing
app_name="case_studies"
urlpatterns=[path("",listing,name="list")]