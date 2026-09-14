from django.urls import path
from .views import robots,sitemap
app_name="seo"
urlpatterns=[path("robots.txt",robots,name="robots"),path("sitemap.xml",sitemap,name="sitemap")]
