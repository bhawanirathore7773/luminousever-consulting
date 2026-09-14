from django.contrib import admin
from .models import Insight
@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display=("title","category","status","published_at")
    list_filter=("status","category")
    search_fields=("title","excerpt","content")
    prepopulated_fields={"slug":("title",)}