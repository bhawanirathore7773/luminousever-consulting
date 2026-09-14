from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
@shared_task(bind=True,autoretry_for=(Exception,),retry_backoff=True,max_retries=4)
def notify_new_lead(self,lead_id):
    from .models import Lead
    lead=Lead.objects.get(pk=lead_id)
    if not settings.LEAD_NOTIFICATION_EMAIL: return
    send_mail(f"New website enquiry — {lead.name}",f"Company: {lead.company}\nEmail: {lead.email}\nPhone: {lead.phone}\n\n{lead.message}",settings.DEFAULT_FROM_EMAIL,[settings.LEAD_NOTIFICATION_EMAIL],fail_silently=False)
