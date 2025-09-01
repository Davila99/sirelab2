from django.contrib import admin
from .models import Mantenimiento, AreaBeneficiaria, TipoMantenimiento, Equipo


@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ("area_beneficiario", "tipo_mantenimiento", "equipo", "cantidad", "fecha_registro")
    search_fields = (
        "area_beneficiario__nombre",
        "tipo_mantenimiento__nombre",
        "equipo__nombre",
    )
    list_filter = ("tipo_mantenimiento", "area_beneficiario", "equipo", "fecha_registro")
    date_hierarchy = "fecha_registro"


@admin.register(AreaBeneficiaria)
class AreaBeneficiariaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(TipoMantenimiento)
class TipoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
