from django.contrib import admin

from .models import TestimonyModel

class TestimonyAdmin(admin.ModelAdmin):
    list_display = (str, "is_visible")
    date_hierarchy = "created_at"
    list_filter = ["author", "is_visible"]
    search_fields = ["content"]
    search_help_text = "Rechercher dans les témoignages"


    actions = ["make_published", "make_no_published"]

    @admin.action(description="Publier les témoignages selectionnés")
    def make_published(self, request, queryset):
        queryset.update(is_visible=True)



    @admin.action(description="Ne pas publier les témoignages selectionnés")
    def make_no_published(self, request, queryset):
        queryset.update(is_visible=False)



admin.site.register(TestimonyModel, TestimonyAdmin)
