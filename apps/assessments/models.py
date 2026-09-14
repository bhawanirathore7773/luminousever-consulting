from django.db import models
class AssessmentSubmission(models.Model):
    name=models.CharField(max_length=160)
    email=models.EmailField()
    company=models.CharField(max_length=200,blank=True)
    score=models.PositiveSmallIntegerField()
    maturity=models.CharField(max_length=40)
    answers=models.JSONField(default=dict)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=["-created_at"]
        indexes=[models.Index(fields=["created_at"]),models.Index(fields=["maturity","created_at"])]
    def __str__(self): return f"{self.company or self.name} — {self.maturity}"