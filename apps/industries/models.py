from django.db import models
class Industry(models.Model):
    name=models.CharField(max_length=160); slug=models.SlugField(unique=True); summary=models.CharField(max_length=300); content=models.TextField(); status=models.BooleanField(default=True)
    class Meta: indexes=[models.Index(fields=["status"]),models.Index(fields=["slug"])]