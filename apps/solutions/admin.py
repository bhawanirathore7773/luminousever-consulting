from django.contrib import admin
from .models import Solution
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display=("name","slug","status","published_at")
    list_filter=("status",)
    search_fields=("name","summary","content")
    prepopulated_fields={"slug":("name",)}