from django.core.cache import cache
from django.shortcuts import get_object_or_404,render
from .models import Solution
from apps.core.cache import site_key
def listing(request):
    key=site_key("solutions","list");items=cache.get(key)
    if items is None:
        items=list(Solution.objects.filter(status=True).only("name","slug","summary").order_by("name"));cache.set(key,items,3600)
    return render(request,"pages/listing.html",{"items":items,"page_heading":"Transformation solutions","page_intro":"Business-led solutions for modern ERP, integration, cloud, finance and supply chain."})
def detail(request,slug): return render(request,"pages/detail.html",{"item":get_object_or_404(Solution.objects.filter(status=True),slug=slug)})
