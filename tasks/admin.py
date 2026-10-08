from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "completed", "created_at")
    list_filter = ("completed", "created_at")
    search_fields = ("title", "description", "owner__username")
    raw_id_fields = ("owner",)          # autocomplete-style FK picker for large user tables
    readonly_fields = ("created_at", "updated_at")  # these are auto-managed
    date_hierarchy = "created_at"       # adds a date drill-down at the top of the list