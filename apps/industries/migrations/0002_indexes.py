from django.db import migrations,models
class Migration(migrations.Migration):
    dependencies=[("industries","0001_initial")]
    operations=[migrations.AddIndex(model_name="industry",index=models.Index(fields=["status"],name="industries_status_idx")),migrations.AddIndex(model_name="industry",index=models.Index(fields=["slug"],name="industries_slug_idx"))]