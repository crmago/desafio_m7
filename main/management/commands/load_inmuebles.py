import csv
from django.core.management.base import BaseCommand
from main.services import crear_inmueble

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    archivo = open('data/inmuebles.csv', encoding="utf-8")
    reader = csv.reader(archivo, delimiter=',')
    next(reader)

    for fila in reader:
      crear_inmueble(nombre=fila[0], 
                    descripcion=fila[1], 
                    m2_construidos=fila[2], 
                    m2_totales=fila[3], 
                    num_estacionamientos=fila[4], 
                    num_habitaciones=fila[5], 
                    num_baños=fila[6], 
                    direccion=fila[7], 
                    tipo_inmueble=fila[8], 
                    precios=fila[9], 
                    comuna_cod=fila[10], 
                    propietario_rut=fila[11])