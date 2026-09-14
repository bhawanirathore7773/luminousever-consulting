from django.urls import path
from .views import assessment
app_name="assessments"
urlpatterns=[path("",assessment,name="assessment")]