from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AreaBeneficiariaViewSet,
    TipoIncidenciaViewSet,
    TipoEquipoRecursoViewSet,
    AtencionIncidenciaViewSet
)

router = DefaultRouter()
router.register(r'areas-beneficiarias', AreaBeneficiariaViewSet)
router.register(r'tipos-incidencia', TipoIncidenciaViewSet)
router.register(r'tipos-equipo-recurso', TipoEquipoRecursoViewSet)
router.register(r'atenciones-incidencias', AtencionIncidenciaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
