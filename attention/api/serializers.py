from rest_framework import serializers

from attention.models import AreaBeneficiaria, AtencionIncidencia, TipoEquipoRecurso, TipoIncidencia

class AreaBeneficiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaBeneficiaria
        fields = ['id', 'nombre']

class TipoIncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoIncidencia
        fields = ['id', 'descripcion']

class TipoEquipoRecursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEquipoRecurso
        fields = ['id', 'descripcion']

class AtencionIncidenciaSerializer(serializers.ModelSerializer):
    area_beneficiaria = AreaBeneficiariaSerializer(read_only=True)
    area_beneficiaria_id = serializers.PrimaryKeyRelatedField(
        queryset=AreaBeneficiaria.objects.all(), source='area_beneficiaria', write_only=True
    )
    
    tipo_incidencia = TipoIncidenciaSerializer(read_only=True)
    tipo_incidencia_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoIncidencia.objects.all(), source='tipo_incidencia', write_only=True
    )
    
    tipo_equipo_recurso = TipoEquipoRecursoSerializer(read_only=True)
    tipo_equipo_recurso_id = serializers.PrimaryKeyRelatedField(
        queryset=TipoEquipoRecurso.objects.all(), source='tipo_equipo_recurso', write_only=True
    )
    
    class Meta:
        model = AtencionIncidencia
        fields = [
            'id',
            'area_beneficiaria',
            'area_beneficiaria_id',
            'tipo_incidencia',
            'tipo_incidencia_id',
            'tipo_equipo_recurso',
            'tipo_equipo_recurso_id',
            'actividad_realizada',
            'estado',
            'fecha_creacion',
        ]
