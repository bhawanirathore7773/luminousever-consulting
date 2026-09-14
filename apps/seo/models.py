from django.db import models
class SEOPage(models.Model):
    path=models.CharField(max_length=255,unique=True)
    title=models.CharField(max_length=70)
    description=models.CharField(max_length=170)
    canonical=models.URLField(blank=True)
    noindex=models.BooleanField(default=False)
    og_image=models.URLField(blank=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: indexes=[models.Index(fields=["path"]),models.Index(fields=["noindex"])]
