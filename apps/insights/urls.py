from django.urls import path
from .views import listing,detail
app_name="insights"
urlpatterns=[path("",listing,name="list"),path("<slug:slug>/",detail,name="detail")]