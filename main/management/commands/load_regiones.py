from django.core.management.base import BaseCommand
import csv
from main.models import Region

class Command(BaseCommand):
  def handle(self,*args,**kwargs):
    archivo = open('data/comunas.csv', encoding='utf-8')
    reader = csv.reader(archivo, delimiter=';')
    next(reader)

    nombres_regiones = []
    
    for fila in reader:
      if fila[2] not in nombres_regiones:
        # si no tenemos el nombre de la region previamente guardada, la agregamos a la base de datos
        Region.objects.create(nombre=fila[2], cod=fila[3])
        # guardamos su nombre para no volver a agregarla
        nombres_regiones.append(fila[2])

    