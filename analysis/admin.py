from django.contrib import admin
from .models import Performance

class PerformanceAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Performance._meta.get_fields()]

admin.site.register(Performance, PerformanceAdmin)
