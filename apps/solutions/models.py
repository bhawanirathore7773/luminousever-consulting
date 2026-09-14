from django.db import models
from django.urls import reverse
class Solution(models.Model):
    name=models.CharField(max_length=160)
    slug=models.SlugField(unique=True)
    summary=models.CharField(max_length=300)
    content=models.TextField()
    status=models.BooleanField(default=True)
    published_at=models.DateTimeField(null=True,blank=True)
    class Meta:
        indexes=[models.Index(fields=["status","published_at"]),models.Index(fields=["slug"])]
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse("solutions:detail",kwargs={"slug":self.slug})