from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AtencionIncidenciaViewSet, AreaBeneficiariaViewSet, TipoIncidenciaViewSet, TipoEquipoRecursoViewSet

router = DefaultRouter()
router.register(r'atencion-incidencias', AtencionIncidenciaViewSet, basename='atencion-incidencia')
router.register(r'areas-beneficiarias', AreaBeneficiariaViewSet, basename='area-beneficiaria')
router.register(r'tipos-incidencia', TipoIncidenciaViewSet, basename='tipo-incidencia')
router.register(r'tipos-equipo-recurso', TipoEquipoRecursoViewSet, basename='tipo-equipo-recurso')

urlpatterns = [
    path('', include(router.urls)),
]
