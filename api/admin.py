from django.contrib import admin
from .models import Works, Workers, DismissedWorkers


class WorkersAdmin(admin.ModelAdmin):
    readonly_fields = ('salary',)  # Предполагается, что 'salary' и 'full_name' являются атрибутами вашей модели Workers


class DismissedWorkersAdmin(admin.ModelAdmin):
    readonly_fields = ('datetime_birday', 'dolznost', 'full_name')  # Предполагается, что 'datetime_birday' и 'dolznost' являются атрибутами вашей модели DismissedWorkers


admin.site.register(Works)
admin.site.register(Workers, WorkersAdmin)
admin.site.register(DismissedWorkers, DismissedWorkersAdmin)
