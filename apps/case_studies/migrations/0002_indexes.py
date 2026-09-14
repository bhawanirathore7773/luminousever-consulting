from django.db import migrations,models
class Migration(migrations.Migration):
    dependencies=[("case_studies","0001_initial")]
    operations=[migrations.AddIndex(model_name="casestudy",index=models.Index(fields=["status","published_at"],name="case_status_pub")),migrations.AddIndex(model_name="casestudy",index=models.Index(fields=["slug"],name="case_slug_idx"))]