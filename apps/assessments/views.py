from apps.core.security import rate_limit
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .forms import AssessmentLeadForm
from .models import AssessmentSubmission

QUESTIONS=[
("erp","How well aligned is your current ERP landscape with your business strategy?"),
("integration","How reliable and observable are your SAP and third-party integrations?"),
("data","How confident are you in the quality and accessibility of enterprise data?"),
("cloud","How clear is your cloud and SAP platform direction?"),
("ux","How effectively do users experience and adopt SAP workflows?"),
("governance","How mature are your SAP architecture, security and governance practices?"),
("change","How prepared is the organization for major SAP transformation?"),
("operations","How proactive and measurable is SAP application management?")
]
def assessment(request): return render(request,"pages/assessment.html",{"questions":QUESTIONS})
@require_POST
def submit(request):
    if not rate_limit(request,"assessment",limit=5,window=300): return JsonResponse({"error":"Too many requests. Please try again later."},status=429)

    form=AssessmentLeadForm(request.POST)
    if not form.is_valid(): return JsonResponse({"errors":form.errors},status=400)
    try: raw=json.loads(request.POST.get("answers","{}"))
    except (TypeError,ValueError): return JsonResponse({"error":"Invalid assessment data"},status=400)
    if not isinstance(raw,dict) or set(raw)!={key for key,_ in QUESTIONS}: return JsonResponse({"error":"Please complete every question."},status=400)
    try: answers={key:max(0,min(4,int(raw[key]))) for key,_ in QUESTIONS}
    except (TypeError,ValueError): return JsonResponse({"error":"Invalid answer values."},status=400)
    score=sum(answers.values()); pct=round(score/(len(QUESTIONS)*4)*100)
    maturity="Emerging" if pct<40 else "Developing" if pct<70 else "Advanced"
    obj=AssessmentSubmission.objects.create(**form.cleaned_data,score=score,maturity=maturity,answers=answers)
    return JsonResponse({"success":True,"score":score,"percentage":pct,"maturity":maturity,"id":obj.pk})
