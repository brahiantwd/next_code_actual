from django.db import models

class Barbero(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    barbero_asignado = models.ForeignKey(Barbero, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Barbero Habitual")
    historial_cortes = models.TextField(blank=True, null=True, help_text="Notas sobre cortes anteriores, gustos del cliente, etc.")
    proxima_cita = models.DateTimeField(blank=True, null=True, verbose_name="Fecha y Hora de la Próxima Cita")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Servicio(models.Model):
    PK_idServicio = models.AutoField(primary_key=True)
    UK_servicios_nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duracion = models.IntegerField(help_text="Duración en minutos", null=True, blank=True)
    
    # CAMPOS NUEVOS
    fecha = models.DateField(null=True, blank=True)
    barbero = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.UK_servicios_nombre