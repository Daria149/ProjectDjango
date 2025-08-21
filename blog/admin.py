from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "publication_attribute", "views_quantity")
    list_filter = ("title", "created_at", "publication_attribute", "views_quantity")
    search_fields = (
        "title",
        "content",
    )