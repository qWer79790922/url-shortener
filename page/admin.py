from django.contrib import admin
from .models import ShortURL

@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ['short_code', 'original_url', 'is_protected', 'created_at']
    search_fields = ['short_code', 'original_url']
    list_filter = ['is_protected', 'created_at']