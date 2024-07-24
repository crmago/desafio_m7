from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
  def handle(self, *args, **kwargs):

    #crear_user('1234567-8', 'Pedro', 'Picapiedras', 'ppiedra@gmail.com', '12345', '12345', 'Av. Rocadura 45')
    #editar_user('1234567-8', 'Pedro', 'Picapiedras', 'pedro@gmail.com', '54321', 'Av. Piedradura 45')
    #crear_inmueble('Bella casa de piedra', 'Amoblada con dinosaurios', 120, 250, 1, 3, 1, 'Av. Rocosa 331', 'casa', 500_000, '05606', '1234567-8')

    inmuebles = obtener_inmuebles_comunas()
    import pdb; pdb.set_trace()