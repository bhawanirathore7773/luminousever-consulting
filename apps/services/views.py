from django.shortcuts import get_object_or_404,render
from .models import Service
def listing(request): return render(request,"pages/listing.html",{"items":Service.objects.filter(status=True).only("name","slug","summary"),"heading":"SAP Services"})
def detail(request,slug): return render(request,"pages/detail.html",{"item":get_object_or_404(Service.objects.filter(status=True),slug=slug)})