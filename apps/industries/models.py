from django.db import models
from django.urls import reverse
class Industry(models.Model):
    name=models.CharField(max_length=160)
    slug=models.SlugField(unique=True)
    summary=models.CharField(max_length=300)
    content=models.TextField()
    status=models.BooleanField(default=True)
    class Meta:
        indexes=[models.Index(fields=["status"]),models.Index(fields=["slug"])]
    def __str__(self): return self.name
    def get_absolute_url(self): return reverse("industries:detail",kwargs={"slug":self.slug})