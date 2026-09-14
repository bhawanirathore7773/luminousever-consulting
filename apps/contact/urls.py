from django.urls import path
from .views import contact,submit
app_name="contact"
urlpatterns=[path("",contact,name="contact"),path("submit/",submit,name="submit")]