from django.contrib import admin
from activitie.models import EventoSoporteTecnico, TipoActividad

@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)
    ordering = ("id",)

@admin.register(EventoSoporteTecnico)
class EventoSoporteTecnicoAdmin(admin.ModelAdmin):
    list_display = ("nombre_evento", "tipo_actividad", "fecha")
    search_fields = ("nombre_evento", "descripcion_asistencia")
    list_filter = ("tipo_actividad", "fecha")
    date_hierarchy = "fecha"
    ordering = ("-fecha",)
