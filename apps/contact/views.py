from apps.core.security import rate_limit
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import ContactForm
def contact(request): return render(request,"pages/contact.html",{"form":ContactForm()})
@require_POST
def submit(request):
    if not rate_limit(request,"contact",limit=5,window=300): return JsonResponse({"error":"Too many requests. Please try again later."},status=429)

    form=ContactForm(request.POST)
    if not form.is_valid(): return JsonResponse({"errors":form.errors},status=400)
    lead=form.save()
    queued=False
    try:
        from .tasks import notify_new_lead
        notify_new_lead.delay(lead.pk); queued=True
    except Exception: pass
    return JsonResponse({"success":True,"notification_queued":queued})
