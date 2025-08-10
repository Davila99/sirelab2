
from rest_framework import serializers
from activitie.models import EventoSoporteTecnico, TipoActividad


class TipoActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActividad
        fields = ['id', 'nombre']

class EventoSoporteTecnicoSerializer(serializers.ModelSerializer):
    tipo_actividad = TipoActividadSerializer(read_only=True)
    tipo_actividad_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoActividad.objects.all(), source='tipo_actividad', write_only=True
    )

    class Meta:
        model = EventoSoporteTecnico
        fields = ['id', 'tipo_actividad', 'tipo_actividad_id', 'nombre_evento', 'fecha', 'descripcion_asistencia']
