from django.db import models
class Service(models.Model):
    name=models.CharField(max_length=160); slug=models.SlugField(unique=True); summary=models.CharField(max_length=300); content=models.TextField(); status=models.BooleanField(default=True); created_at=models.DateTimeField(auto_now_add=True); updated_at=models.DateTimeField(auto_now=True)
    class Meta: indexes=[models.Index(fields=["status"]),models.Index(fields=["slug"])]
    def __str__(self): return self.name