from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.

class UserProfile(models.Model):
  # User: username(rut), email, fist_name, last_name, password
  roles = (('arrendador','Arrendador'),('arrendatario','Arrendatario'),('admin','Admin'))
  user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
  direccion = models.CharField(max_length=255)
  telefono = models.CharField(max_length=255, null=True)

  def __str__(self) -> str:
    return f'{self.user}'



class Region(models.Model):
  cod = models.CharField(max_length=2, primary_key=True)
  nombre = models.CharField(max_length=255)

  def __str__(self) -> str:
    return f'{self.nombre} ({self.cod})'


class Comuna(models.Model):
  cod = models.CharField(max_length=5, primary_key=True)
  nombre = models.CharField(max_length=255)
  region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='comunas')

  def __str__(self) -> str:
    return f'{self.nombre} ({self.cod})'


class Inmueble(models.Model):

  tipos =(('casa','Casa'),('departamento','Departamento'),('bodega','Bodega'))

  nombre = models.CharField(max_length=50)
  descripcion = models.TextField(max_length=1500)
  m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
  m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
  num_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
  num_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=1)
  num_baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
  direccion = models.CharField(max_length=255)
  tipo_inmueble = models.CharField(max_length=255, choices=tipos)
  precios = models.IntegerField(validators=[MinValueValidator(1000)], null=True)
  precios_ufs = models.FloatField(validators=[MinValueValidator(1.0)], null=True)
  # llaves foraneas
  comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
  propietario = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='inmuebles')


class Solicitud(models.Model):

  estados = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada','Aprobada'))

  inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
  arrendador = models.ForeignKey(User, related_name='solicitudes', on_delete=models.CASCADE)
  fecha = models.DateTimeField(auto_now_add=True)
  estado = models.CharField(max_length=50, choices=estados)