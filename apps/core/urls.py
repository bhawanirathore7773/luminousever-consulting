from django.urls import path
from .views import health,home,legal
from . import views
urlpatterns=[path("",home,name="home"),path("health/",health,name="health"),path("privacy/",lambda r: legal(r,"privacy"),name="privacy"),path("terms/",lambda r: legal(r,"terms"),name="terms"),path("refund/",lambda r: legal(r,"refund"),name="refund"),path("cookies/",lambda r: legal(r,"cookies"),name="cookies")]