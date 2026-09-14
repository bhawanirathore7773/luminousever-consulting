from django.contrib import admin
from .models import AssessmentSubmission
@admin.register(AssessmentSubmission)
class AssessmentSubmissionAdmin(admin.ModelAdmin):
    list_display=("name","company","email","score","maturity","created_at")
    list_filter=("maturity","created_at")
    search_fields=("name","company","email")
    readonly_fields=("created_at",)