from django.db import models
from measurements.models import Measurement

class Adenda(models.Model):
    paciente = models.ForeignKey(Measurement, on_delete=models.CASCADE, default=None)
    fechaConsulta = models.CharField(max_length=50, default=None)
    lugarConsulta = models.CharField(max_length=50, default=None)
    tipoConsulta = models.CharField(max_length=50, default=None)
    motivoConsulta = models.CharField(max_length=50, default=None)
    enfermedad = models.CharField(max_length=50, default=None)

    def __str__(self):
        return '%s %s' % (self.fechaConsulta, self.lugarConsulta)