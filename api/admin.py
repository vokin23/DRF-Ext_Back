from django.contrib import admin
from .models import Works, Workers


class WorkersAdmin(admin.ModelAdmin):
    readonly_fields = ('salary',)  # Указываем поле salary как только для чтения


admin.site.register(Works)
admin.site.register(Workers, WorkersAdmin)
