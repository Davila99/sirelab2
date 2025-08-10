from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoActividadViewSet, EventoSoporteTecnicoViewSet

router = DefaultRouter()
router.register(r'tipos-actividad', TipoActividadViewSet)
router.register(r'eventos-soporte', EventoSoporteTecnicoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
