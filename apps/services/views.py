from django.core.cache import cache
from django.shortcuts import get_object_or_404,render
from .models import Service
from apps.core.cache import site_key
def listing(request):
    key=site_key("services","list")
    items=cache.get(key)
    if items is None:
        items=list(Service.objects.filter(status=True).only("name","slug","summary").order_by("name"))
        cache.set(key,items,3600)
    return render(request,"pages/listing.html",{"items":items,"page_heading":"SAP services","page_intro":"Focused consulting capabilities across SAP transformation, integration and enterprise technology."})
def detail(request,slug):
    return render(request,"pages/detail.html",{"item":get_object_or_404(Service.objects.filter(status=True),slug=slug)})
