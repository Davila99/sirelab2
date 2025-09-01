from django.db import models


class AreaBeneficiaria(models.Model):
    nombre = models.CharField(max_length=150, unique=True, verbose_name="Área / Beneficiario")

    class Meta:
        verbose_name = "Área Beneficiaria"
        verbose_name_plural = "Áreas Beneficiarias"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class TipoMantenimiento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Tipo de Mantenimiento")

    class Meta:
        verbose_name = "Tipo de Mantenimiento"
        verbose_name_plural = "Tipos de Mantenimiento"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    nombre = models.CharField(max_length=150, unique=True, verbose_name="Equipo")

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Mantenimiento(models.Model):
    area_beneficiario = models.ForeignKey(AreaBeneficiaria, on_delete=models.CASCADE, verbose_name="Área / Beneficiario")
    tipo_mantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.CASCADE, verbose_name="Tipo de Mantenimiento")
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, verbose_name="Equipo")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    actividades = models.TextField(verbose_name="Actividades realizadas")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Plan de Mantenimiento"
        verbose_name_plural = "Planes de Mantenimiento"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.equipo} - {self.tipo_mantenimiento} ({self.area_beneficiario})"
