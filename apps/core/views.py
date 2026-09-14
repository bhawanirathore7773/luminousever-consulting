from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
def home(request): return render(request,"pages/home.html")
def legal(request,page): return render(request,f"pages/{page}.html")
def health(request):
    with connection.cursor() as cursor: cursor.execute("SELECT 1")
    return JsonResponse({"status":"ok"})
def error_404(request,exception): return render(request,"errors/404.html",status=404)
def error_403(request,exception): return render(request,"errors/403.html",status=403)
def error_500(request): return render(request,"errors/500.html",status=500)
