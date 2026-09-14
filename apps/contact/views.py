from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import ContactForm
def contact(request):
    return render(request,"pages/contact.html",{"form":ContactForm()})
@require_POST
def submit(request):
    form=ContactForm(request.POST)
    if not form.is_valid(): return JsonResponse({"errors":form.errors},status=400)
    lead=form.save()
    try:
        from .tasks import notify_new_lead
        notify_new_lead.delay(lead.pk)
    except Exception:
        pass
    return JsonResponse({"success":True})
