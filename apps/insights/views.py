from django.contrib.postgres.search import SearchQuery,SearchRank,SearchVector
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,render
from .models import Insight

def listing(request):
    qs=Insight.objects.filter(status=True).only("title","slug","excerpt","category","published_at")
    query=request.GET.get("q","").strip()
    if query:
        vector=SearchVector("title",weight="A")+SearchVector("excerpt",weight="B")+SearchVector("content",weight="C")
        qs=Insight.objects.annotate(rank=SearchRank(vector,SearchQuery(query))).filter(status=True,rank__gt=0).order_by("-rank","-published_at").only("title","slug","excerpt","category","published_at")
    category=request.GET.get("category","").strip()
    if category: qs=qs.filter(category=category)
    page=Paginator(qs,9).get_page(request.GET.get("page"))
    return render(request,"pages/insights.html",{"items":page.object_list,"page_obj":page,"query":query,"category":category})

def detail(request,slug):
    return render(request,"pages/detail.html",{"item":get_object_or_404(Insight.objects.filter(status=True),slug=slug)})
