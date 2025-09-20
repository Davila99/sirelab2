from rest_framework import viewsets
from attention.models import AreaBeneficiaria, TipoIncidencia, TipoEquipoRecurso, AtencionIncidencia
from .serializers import (
    AreaBeneficiariaSerializer,
    TipoIncidenciaSerializer,
    TipoEquipoRecursoSerializer,
    AtencionIncidenciaSerializer
)

# ViewSet para AreaBeneficiaria
class AreaBeneficiariaViewSet(viewsets.ModelViewSet):
    queryset = AreaBeneficiaria.objects.all()
    serializer_class = AreaBeneficiariaSerializer
    filterset_fields = ['nombre']

# ViewSet para TipoIncidencia
class TipoIncidenciaViewSet(viewsets.ModelViewSet):
    queryset = TipoIncidencia.objects.all()
    serializer_class = TipoIncidenciaSerializer
    filterset_fields = ['descripcion']

# ViewSet para TipoEquipoRecurso
class TipoEquipoRecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipoRecurso.objects.all()
    serializer_class = TipoEquipoRecursoSerializer
    filterset_fields = ['nombre', 'descripcion']

# ViewSet para AtencionIncidencia
class AtencionIncidenciaViewSet(viewsets.ModelViewSet):
    queryset = AtencionIncidencia.objects.all()
    serializer_class = AtencionIncidenciaSerializer
    filterset_fields = ['estado', 'area_beneficiaria', 'tipo_incidencia', 'tipo_equipo_recurso']