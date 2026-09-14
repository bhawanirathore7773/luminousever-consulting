from django.urls import path
from .views import listing
app_name="sap_expertise"
urlpatterns=[path("",listing,name="list")]