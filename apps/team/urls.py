from django.urls import path
from django.shortcuts import render
app_name="team"
urlpatterns=[path("",lambda request: render(request,"pages/team.html"),name="list")]