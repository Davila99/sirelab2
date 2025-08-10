from rest_framework import viewsets
from .models import TipoActividad, EventoSoporteTecnico
from .serializers import TipoActividadSerializer, EventoSoporteTecnicoSerializer

class TipoActividadViewSet(viewsets.ModelViewSet):
    queryset = TipoActividad.objects.all()
    serializer_class = TipoActividadSerializer

class EventoSoporteTecnicoViewSet(viewsets.ModelViewSet):
    queryset = EventoSoporteTecnico.objects.all()
    serializer_class = EventoSoporteTecnicoSerializer
