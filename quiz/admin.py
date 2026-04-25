from django.contrib import admin

from .models import Bitik, Natija, Savol, Sinf


@admin.register(Sinf)
class SinfAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'created_at']
    search_fields = ['nom']


@admin.register(Savol)
class SavolAdmin(admin.ModelAdmin):
    list_display = ['id', 'sinf', 'savol', 'tjavob']
    list_filter = ['sinf']
    search_fields = ['savol']


@admin.register(Natija)
class NatijaAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'sinf', 'tjavob', 'jamisavol', 'foiz_display', 'date']
    list_filter = ['sinf', 'date']
    search_fields = ['user__username']
    readonly_fields = ['date']

    @admin.display(description="Foiz")
    def foiz_display(self, obj):
        return f"{obj.foiz}%"


@admin.register(Bitik)
class BitikAdmin(admin.ModelAdmin):
    list_display = ['id', 'muallif', 'matn']
    search_fields = ['muallif', 'matn']
