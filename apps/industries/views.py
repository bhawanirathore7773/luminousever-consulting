from django.shortcuts import get_object_or_404,render
from .models import Industry
def listing(request): return render(request,"pages/listing.html",{"items":Industry.objects.filter(status=True).only("name","slug","summary"),"heading":"Industries"})
def detail(request,slug): return render(request,"pages/detail.html",{"item":get_object_or_404(Industry.objects.filter(status=True),slug=slug)})