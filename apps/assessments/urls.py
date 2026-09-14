from django.urls import path
from .views import assessment,submit
app_name="assessments"
urlpatterns=[path("",assessment,name="assessment"),path("submit/",submit,name="submit")]