from django.shortcuts import render
from .models import CaseStudy
def listing(request): return render(request,"pages/listing.html",{"items":CaseStudy.objects.filter(status=True).only("title","slug","summary","published_at"),"heading":"Case Studies"})