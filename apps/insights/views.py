from django.shortcuts import get_object_or_404,render
from .models import Insight
def listing(request): return render(request,"pages/listing.html",{"items":Insight.objects.filter(status=True).only("title","slug","excerpt","category","published_at"),"heading":"Insights"})
def detail(request,slug): return render(request,"pages/detail.html",{"item":get_object_or_404(Insight.objects.filter(status=True),slug=slug)})