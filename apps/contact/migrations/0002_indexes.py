from django.db import migrations,models
class Migration(migrations.Migration):
    dependencies=[("contact","0001_initial")]
    operations=[migrations.AddIndex(model_name="lead",index=models.Index(fields=["status","created_at"],name="contact_lead_status_created"),),migrations.AddIndex(model_name="lead",index=models.Index(fields=["created_at"],name="contact_lead_created") )]