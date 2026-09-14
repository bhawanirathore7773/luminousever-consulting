from django.db import migrations,models
class Migration(migrations.Migration):
    dependencies=[("insights","0001_initial")]
    operations=[migrations.AddIndex(model_name="insight",index=models.Index(fields=["status","published_at"],name="insight_status_pub")),migrations.AddIndex(model_name="insight",index=models.Index(fields=["category"],name="insight_category_idx")),migrations.AddIndex(model_name="insight",index=models.Index(fields=["slug"],name="insight_slug_idx"))]