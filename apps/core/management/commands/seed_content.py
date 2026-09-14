from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils import timezone
from apps.services.models import Service
from apps.solutions.models import Solution
from apps.industries.models import Industry
from apps.case_studies.models import CaseStudy
from apps.insights.models import Insight
from apps.services.seed_data import SERVICES
from apps.solutions.seed_data import SOLUTIONS
from apps.industries.seed_data import INDUSTRIES
from apps.case_studies.seed_data import CASE_STUDIES
from apps.insights.seed_data import INSIGHTS

class Command(BaseCommand):
    help="Seed the initial public content without overwriting existing records."
    def handle(self,*args,**kwargs):
        for name,slug,summary in SERVICES: Service.objects.get_or_create(slug=slug,defaults={"name":name,"summary":summary,"content":summary})
        for name,slug,summary in SOLUTIONS: Solution.objects.get_or_create(slug=slug,defaults={"name":name,"summary":summary,"content":summary,"published_at":timezone.now()})
        for name,slug,summary in INDUSTRIES: Industry.objects.get_or_create(slug=slug,defaults={"name":name,"summary":summary,"content":summary})
        for title,slug,summary in CASE_STUDIES: CaseStudy.objects.get_or_create(slug=slug,defaults={"title":title,"summary":summary,"content":summary,"published_at":timezone.now()})
        for title,slug,excerpt,category in INSIGHTS: Insight.objects.get_or_create(slug=slug,defaults={"title":title,"excerpt":excerpt,"content":excerpt,"category":category,"published_at":timezone.now(),"status":True})
        self.stdout.write(self.style.SUCCESS("Initial content seeded."))