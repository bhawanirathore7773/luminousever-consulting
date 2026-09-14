from django.shortcuts import get_object_or_404,render
from .models import Solution
def listing(request): return render(request,"pages/listing.html",{"items":Solution.objects.filter(status=True).only("name","slug","summary"),"heading":"SAP Solutions"})
def detail(request,slug): return render(request,"pages/detail.html",{"item":get_object_or_404(Solution.objects.filter(status=True),slug=slug)})