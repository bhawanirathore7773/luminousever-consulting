from django.http import JsonResponse
from django.shortcuts import render
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
def assessment(request):
    return render(request,"pages/assessment.html",{"questions":QUESTIONS})
def submit(request):
    if request.method!="POST": return JsonResponse({"error":"Method not allowed"},status=405)
    form=AssessmentLeadForm(request.POST)
    if not form.is_valid(): return JsonResponse({"errors":form.errors},status=400)
    import json
    try: answers=json.loads(request.POST.get("answers","{}"))
    except ValueError: return JsonResponse({"error":"Invalid assessment data"},status=400)
    score=sum(max(0,min(4,int(v))) for v in answers.values() if str(v).isdigit())
    maximum=len(QUESTIONS)*4
    pct=round(score/maximum*100) if maximum else 0
    maturity="Emerging" if pct<40 else "Developing" if pct<70 else "Advanced"
    obj=AssessmentSubmission.objects.create(**form.cleaned_data,score=score,maturity=maturity,answers=answers)
    return JsonResponse({"success":True,"score":score,"percentage":pct,"maturity":maturity,"id":obj.pk})
