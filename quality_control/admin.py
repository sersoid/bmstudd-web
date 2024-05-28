from django.contrib import admin

from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "project", "task", "status"]
    list_filter = ["status"]
    search_fields = ["title", "description"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "project",
                    "task",
                    "status"
                )
            }
        ),
        (
            "Дополнительная информация",
            {
                "fields": (
                    "priority",
                ),
                "classes": (
                    "collapse",
                )
            }
        ),
    )

    def change_status_to_fixed(self, request, queryset):
        queryset.update(status="fixed")
    
    change_status_to_fixed.short_description = "Изменить статус на \"Исправлен\""

    actions = [change_status_to_fixed]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "project", "task", "priority"]
    list_filter = ["priority"]
    search_fields = ["title", "description"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "description",
                    "project",
                    "task",
                    "status"
                )
            }
        ),
        (
            "Дополнительная информация",
            {
                "fields": (
                    "priority",
                ),
                "classes": (
                    "collapse",
                )
            }
        ),
    )
