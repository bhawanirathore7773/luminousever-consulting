from django.db import models
from django.urls import reverse
class Insight(models.Model):
    title=models.CharField(max_length=220)
    slug=models.SlugField(unique=True)
    excerpt=models.CharField(max_length=320)
    content=models.TextField()
    category=models.CharField(max_length=100,blank=True)
    published_at=models.DateTimeField()
    status=models.BooleanField(default=False)
    class Meta:
        indexes=[models.Index(fields=["status","published_at"]),models.Index(fields=["category"]),models.Index(fields=["slug"])]
        ordering=["-published_at"]
    def __str__(self): return self.title
    def get_absolute_url(self): return reverse("insights:detail",kwargs={"slug":self.slug})