from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import StaticSitemap,service_sitemap,solution_sitemap,industry_sitemap,insight_sitemap
from .views import robots
sitemaps={"static":StaticSitemap,"services":service_sitemap,"solutions":solution_sitemap,"industries":industry_sitemap,"insights":insight_sitemap}
urlpatterns=[path("robots.txt",robots,name="robots"),path("sitemap.xml",sitemap,{"sitemaps":sitemaps},name="sitemap")]