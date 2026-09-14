from django.db import models
class CaseStudy(models.Model):
    title=models.CharField(max_length=200); slug=models.SlugField(unique=True); summary=models.CharField(max_length=320); content=models.TextField(); published_at=models.DateTimeField(null=True,blank=True); status=models.BooleanField(default=True)
    class Meta: indexes=[models.Index(fields=["status","published_at"]),models.Index(fields=["slug"])]