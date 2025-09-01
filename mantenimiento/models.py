from django.db import models

class Mantenimiento(models.Model):
    area_beneficiario = models.CharField(max_length=150, verbose_name="Área / Beneficiario")
    tipo_mantenimiento = models.CharField(max_length=100, choices=[
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ], verbose_name="Tipo de Mantenimiento")
    equipo = models.CharField(max_length=150, verbose_name="Equipo")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    actividades = models.TextField(verbose_name="Actividades realizadas")

    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Plan de Mantenimiento"
        verbose_name_plural = "Planes de Mantenimiento"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.equipo} - {self.tipo_mantenimiento} ({self.area_beneficiario})"
