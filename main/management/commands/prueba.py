from typing import Any
from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
    
    crear_user('3456789-9', 'Bruce', 'Wayne', 'batman@gmail.com', '09876', '09876', 'Av.Arhkam 234')
    #crear_user('2345678-9', 'Pablo', 'Marmol', 'marmolp@gmail.com', '67890', '67890', 'Av.piedradura 789')
    #editar_user('1234567-8', 'Pedro', 'Picapiedras', 'pedrop@gmail.com', '54321', 'Av.Piedradura 45')
    #editar_user('1234567-8', 'Pedro', 'Picapiedras', 'picapiedra@gmail.com', '12354', 'Av.Piedradura 45')
    #editar_user('2345678-9', 'Pablo', 'Marmol', 'pablomarmol@gmail.com', '97680', 'Av.Rocadura 567')
    #crear_inmueble('Ático Panorámico',"Ático con terraza panorámica y vistas nocturnas",100,120,0,1,1,"Calle Panorámica 789","departamento",70000,13109,32109876-5)
    