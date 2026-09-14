from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[migrations.CreateModel(name="Lead",fields=[
        ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
        ("name",models.CharField(max_length=160)),("email",models.EmailField(max_length=254)),("company",models.CharField(blank=True,max_length=200)),("phone",models.CharField(blank=True,max_length=40)),("message",models.TextField()),("source",models.CharField(blank=True,max_length=100)),("status",models.CharField(choices=[("new","New"),("processing","Processing"),("qualified","Qualified"),("closed","Closed")],default="new",max_length=20)),("created_at",models.DateTimeField(auto_now_add=True)),("updated_at",models.DateTimeField(auto_now=True))],options={"ordering":["-created_at"]})]