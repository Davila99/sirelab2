from django.contrib import admin
from .models import AreaBeneficiaria, AtencionIncidencia, TipoEquipoRecurso, TipoIncidencia

# ------------------------------
# Admin para AtencionIncidencia
# ------------------------------
@admin.register(AtencionIncidencia)
class AtencionIncidenciaAdmin(admin.ModelAdmin):
    list_display = ("area_beneficiaria", "tipo_incidencia", "tipo_equipo_recurso", "estado", "fecha_creacion")
    search_fields = (
        "area_beneficiaria__nombre",
        "tipo_incidencia__descripcion",
        "tipo_equipo_recurso__descripcion",
        "actividad_realizada",
    )
    list_filter = ("estado", "area_beneficiaria", "tipo_incidencia", "tipo_equipo_recurso", "fecha_creacion")
    date_hierarchy = "fecha_creacion"

# ------------------------------
# Admin para AreaBeneficiaria
# ------------------------------
@admin.register(AreaBeneficiaria)
class AreaBeneficiariaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)

# ------------------------------
# Admin para TipoIncidencia
# ------------------------------
@admin.register(TipoIncidencia)
class TipoIncidenciaAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)

# ------------------------------
# Admin para TipoEquipoRecurso
# ------------------------------
@admin.register(TipoEquipoRecurso)
class TipoEquipoRecursoAdmin(admin.ModelAdmin):
    list_display = ("id", "descripcion")
    search_fields = ("descripcion",)
