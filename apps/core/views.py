from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, "pages/home.html", {"page_title":"Luminousever Consulting | SAP Transformation & Advisory"})

def health(request):
    return JsonResponse({"status":"ok"})

def error_404(request, exception):
    return render(request, "errors/404.html", status=404)

def error_403(request, exception):
    return render(request, "errors/403.html", status=403)

def error_500(request):
    return render(request, "errors/500.html", status=500)
