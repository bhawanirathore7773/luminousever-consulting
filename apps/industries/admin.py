from django.contrib import admin
from .models import Industry
@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display=("name","slug","status")
    list_filter=("status",)
    search_fields=("name","summary","content")
    prepopulated_fields={"slug":("name",)}