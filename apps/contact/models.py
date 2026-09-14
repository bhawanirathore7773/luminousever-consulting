from django.db import models

class Lead(models.Model):
    STATUS_CHOICES=[("new","New"),("processing","Processing"),("qualified","Qualified"),("closed","Closed")]
    name=models.CharField(max_length=160)
    email=models.EmailField()
    company=models.CharField(max_length=200, blank=True)
    phone=models.CharField(max_length=40, blank=True)
    message=models.TextField()
    source=models.CharField(max_length=100, blank=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        indexes=[models.Index(fields=["status","created_at"]),models.Index(fields=["created_at"])]
        ordering=["-created_at"]
    def __str__(self):
        return f"{self.name} — {self.email}"
