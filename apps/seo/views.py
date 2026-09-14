from django.http import HttpResponse
def robots(request):
    return HttpResponse("User-agent: *\nAllow: /\nSitemap: /seo/sitemap.xml\n",content_type="text/plain")
