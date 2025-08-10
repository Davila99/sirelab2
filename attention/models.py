from django.db import models

class AreaBeneficiaria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoIncidencia(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class TipoEquipoRecurso(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Estado(models.TextChoices):
    PENDIENTE = 'PE', 'Pendiente'
    EN_PROGRESO = 'EP', 'En Progreso'
    RESUELTO = 'RE', 'Resuelto'
    CANCELADO = 'CA', 'Cancelado'

class AtencionIncidencia(models.Model):
    area_beneficiaria = models.ForeignKey(AreaBeneficiaria, on_delete=models.CASCADE)
    tipo_incidencia = models.ForeignKey(TipoIncidencia, on_delete=models.CASCADE)
    tipo_equipo_recurso = models.ForeignKey(TipoEquipoRecurso, on_delete=models.CASCADE)
    actividad_realizada = models.TextField()
    estado = models.CharField(max_length=2, choices=Estado.choices, default=Estado.PENDIENTE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.area_beneficiaria} - {self.tipo_incidencia} - {self.estado}"
