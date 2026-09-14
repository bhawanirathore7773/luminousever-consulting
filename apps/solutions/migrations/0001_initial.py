from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True; dependencies=[]
    operations=[migrations.CreateModel(name="Solution",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("name",models.CharField(max_length=160)),("slug",models.SlugField(unique=True)),("summary",models.CharField(max_length=300)),("content",models.TextField()),("status",models.BooleanField(default=True)),("published_at",models.DateTimeField(blank=True,null=True))])]