from django.urls import path
from django.shortcuts import render
def home(request): return render(request,"pages/home.html")
def legal(request,page): return render(request,f"pages/{page}.html")
urlpatterns=[path("",home,name="home"),path("privacy/",lambda r: legal(r,"privacy"),name="privacy"),path("terms/",lambda r: legal(r,"terms"),name="terms"),path("refund/",lambda r: legal(r,"refund"),name="refund"),path("cookies/",lambda r: legal(r,"cookies"),name="cookies")]