from django.db import migrations,models
class Migration(migrations.Migration):
    dependencies=[("solutions","0001_initial")]
    operations=[migrations.AddIndex(model_name="solution",index=models.Index(fields=["status","published_at"],name="solutions_status_pub")),migrations.AddIndex(model_name="solution",index=models.Index(fields=["slug"],name="solutions_slug_idx"))]