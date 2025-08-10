from django.db import models

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class EventoSoporteTecnico(models.Model):
    tipo_actividad = models.ForeignKey(TipoActividad, on_delete=models.CASCADE, related_name='eventos')
    nombre_evento = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion_asistencia = models.TextField()

    def __str__(self):
        return f"{self.nombre_evento} ({self.fecha})"
