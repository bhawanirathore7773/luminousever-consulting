from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True,autoretry_for=(Exception,),retry_backoff=True,max_retries=5)
def notify_new_lead(self, lead_id):
    from .models import Lead
    lead=Lead.objects.get(pk=lead_id)
    send_mail("New website enquiry",f"New lead from {lead.name} ({lead.email}).",settings.DEFAULT_FROM_EMAIL,[settings.DEFAULT_FROM_EMAIL])