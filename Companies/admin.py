from django.contrib import admin

from Companies.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display: tuple = (
        "id",
        "name",
    )
    list_filter: tuple = ("founded", "region")
    fieldsets: tuple = (
        ("Overview", {"fields": ("id", "name")}),
        (
            "Company details",
            {"fields": (
                    "founded",
                    "size",
                    "locality",
                    "region",
                    "country",
                    "industry"
                )
            },
        ),
        ("Social", {"fields": ("website", "linkedin_url")}),
    )
    search_fields: tuple = ("name", "id")
    ordering: tuple = ("name", "founded", "id", "locality", "region", "country")
    list_per_page: int = 20

admin.site.register(Company, CompanyAdmin)
