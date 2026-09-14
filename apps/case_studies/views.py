from django.shortcuts import render
from .models import CaseStudy

def listing(request):
    items=CaseStudy.objects.filter(status=True).only("title","slug","summary","published_at").order_by("-published_at")
    return render(request,"pages/listing.html",{"items":items,"page_heading":"Transformation in practice","page_intro":"Selected perspectives on how SAP, integration and enterprise technology decisions can translate into clearer operating outcomes.","page_label":"CASE STUDIES"})