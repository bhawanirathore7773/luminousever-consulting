from django.http import HttpResponse
from django.shortcuts import render
def robots(request):
    return HttpResponse("User-agent: *\nAllow: /\nSitemap: /sitemap.xml\n",content_type="text/plain")
def sitemap(request):
    return render(request,"seo/sitemap.xml",content_type="application/xml")
