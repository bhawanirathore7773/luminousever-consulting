from django.contrib import admin
from .models import CaseStudy
@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display=("title","status","published_at")
    list_filter=("status",)
    search_fields=("title","summary","content")
    prepopulated_fields={"slug":("title",)}