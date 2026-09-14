from django.db import models
class Solution(models.Model):
    name=models.CharField(max_length=160); slug=models.SlugField(unique=True); summary=models.CharField(max_length=300); content=models.TextField(); status=models.BooleanField(default=True); published_at=models.DateTimeField(null=True,blank=True)
    class Meta: indexes=[models.Index(fields=["status","published_at"]),models.Index(fields=["slug"])]