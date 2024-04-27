from django.contrib import admin
from .models import MiniProjectsModal


# Register your models here.
@admin.register(MiniProjectsModal)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    search_fields = ("title", "keywords")
