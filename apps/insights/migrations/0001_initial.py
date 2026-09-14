from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True; dependencies=[]
    operations=[migrations.CreateModel(name="Insight",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("title",models.CharField(max_length=220)),("slug",models.SlugField(unique=True)),("excerpt",models.CharField(max_length=320)),("content",models.TextField()),("category",models.CharField(blank=True,max_length=100)),("published_at",models.DateTimeField()),("status",models.BooleanField(default=False))])]