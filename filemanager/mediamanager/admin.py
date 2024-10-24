from django.contrib import admin
from .models import Media
# Register your models here.

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'format', 'size', 'duration_secs')