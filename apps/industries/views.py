from django.shortcuts import get_object_or_404,render
from .models import Industry

def listing(request):
    items=Industry.objects.filter(status=True).only("name","slug","summary").order_by("name")
    return render(request,"pages/listing.html",{"items":items,"page_heading":"Industry-focused transformation","page_intro":"SAP and enterprise technology priorities shaped around the operating realities of manufacturing, services, consumer and industrial organizations.","page_label":"INDUSTRIES"})

def detail(request,slug):
    return render(request,"pages/detail.html",{"item":get_object_or_404(Industry.objects.filter(status=True),slug=slug)})