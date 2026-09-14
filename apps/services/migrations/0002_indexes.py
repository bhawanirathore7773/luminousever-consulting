from django.db import migrations,models
class Migration(migrations.Migration):
    dependencies=[("services","0001_initial")]
    operations=[migrations.AddIndex(model_name="service",index=models.Index(fields=["status"],name="services_status_idx")),migrations.AddIndex(model_name="service",index=models.Index(fields=["slug"],name="services_slug_idx"))]