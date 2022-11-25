from django.db import models

# Create your models here.
class Integrante (models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=250)
    edad=models.IntegerField()
    ocupacion=models.CharField(max_length=250)
    diadenacimiento=models.DateField()
    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.edad+" "+self.ocupacion+" "+self.diadenacimiento


