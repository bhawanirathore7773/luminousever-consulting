from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.services.models import Service
from apps.solutions.models import Solution
from apps.industries.models import Industry
from apps.insights.models import Insight
class StaticSitemap(Sitemap):
    priority=.8
    changefreq="weekly"
    def items(self): return ["home","services:list","solutions:list","industries:list","sap_expertise:list","case_studies:list","insights:list","team:list","assessments:assessment","contact:contact","privacy","terms","refund","cookies"]
    def location(self,item): return reverse(item)
class ModelSitemap(Sitemap):
    def __init__(self,model): self.model=model
    def items(self): return self.model.objects.filter(status=True)
    def lastmod(self,obj): return getattr(obj,"updated_at",None) or getattr(obj,"published_at",None)
service_sitemap=ModelSitemap(Service)
solution_sitemap=ModelSitemap(Solution)
industry_sitemap=ModelSitemap(Industry)
insight_sitemap=ModelSitemap(Insight)