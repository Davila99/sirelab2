from rest_framework import viewsets

from attention.models import AreaBeneficiaria, AtencionIncidencia, TipoEquipoRecurso, TipoIncidencia

from .serializers import (
    AtencionIncidenciaSerializer,
    AreaBeneficiariaSerializer,
    TipoIncidenciaSerializer,
    TipoEquipoRecursoSerializer
)

class AreaBeneficiariaViewSet(viewsets.ModelViewSet):
    queryset = AreaBeneficiaria.objects.all()
    serializer_class = AreaBeneficiariaSerializer

class TipoIncidenciaViewSet(viewsets.ModelViewSet):
    queryset = TipoIncidencia.objects.all()
    serializer_class = TipoIncidenciaSerializer

class TipoEquipoRecursoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipoRecurso.objects.all()
    serializer_class = TipoEquipoRecursoSerializer

class AtencionIncidenciaViewSet(viewsets.ModelViewSet):
    queryset = AtencionIncidencia.objects.all()
    serializer_class = AtencionIncidenciaSerializer
