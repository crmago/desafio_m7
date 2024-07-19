from django.contrib.auth.models import User
from main.models import UserProfile, Inmueble, Comuna
from django.db.utils import IntegrityError
from django.db.models import Q
from django.db import connection




def crear_inmueble(nombre, descripcion, m2_construidos, m2_totales, num_estacionamientos, num_habitaciones, num_baños, direccion, tipo_inmueble, precios, comuna_cod, propietario_rut):
    try:
        comuna = Comuna.objects.get(cod=comuna_cod)
        propietario = User.objects.get(username=propietario_rut)
        
        Inmueble.objects.create(
            nombre=nombre, 
            descripcion=descripcion, 
            m2_construidos=m2_construidos, 
            m2_totales=m2_totales, 
            num_estacionamientos=num_estacionamientos, 
            num_habitaciones=num_habitaciones, 
            num_baños=num_baños, 
            direccion=direccion, 
            tipo_inmueble=tipo_inmueble, 
            precios=precios, 
            comuna=comuna, 
            propietario=propietario
        )
    except Comuna.DoesNotExist:
        print(f'Error: Comuna con código {comuna_cod} no existe.')
    except User.DoesNotExist:
        print(f'Error: Usuario con RUT {propietario_rut} no existe.')

def editar_inmueble(*args):
  pass

def eliminar_inmueble(inmueble_id):
  pass

def crear_user(username, first_name, last_name, email, password, pass_confirm, direccion, telefono=None) -> list[bool, str]:
  # 1. validamos que los password coincidan
  if password != pass_confirm:
    return False, 'Las contraseñas no coinciden'
  # 2. creamos el objeto user
  try:
    user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
    user.save()
  except IntegrityError:
    # se le da feedback al usuario
    return False, 'RUT Duplicado'
  # 3. creamos el userprofile
  UserProfile.objects.create(user=user, direccion=direccion, telefono=telefono)
  # 4. si todo sale bien retornamos true
  return True, None

def editar_user(username, first_name, last_name, email, password, direccion, telefono=None) -> list[bool, str]:
  # 1. Nos traemos el 'user' y modificamos sus datos
  user = User.objects.get(username=username)
  user.first_name = first_name
  user.last_name = last_name
  user.email = email
  user.set_password(password)
  user.save()
  # 2. Nos traemos el 'userprofile' y modificamos sus datos
  userprofile = UserProfile.objects.get(user=user)
  userprofile.direccion = direccion
  userprofile.telefono = telefono
  userprofile.save()


def editar_user_sin_password(username, first_name, last_name, email, direccion, telefono=None)-> list[bool, str]:
  # 1. Nos traemos el 'user' y modificamos sus datos
  user = User.objects.get(username=username)
  user.first_name = first_name
  user.last_name = last_name
  user.email = email
  user.save()
  # 2. Nos traemos el 'userprofile' y modificamos sus datos
  userprofile = UserProfile.objects.get(user=user)
  userprofile.direccion = direccion
  userprofile.telefono = telefono
  userprofile.save()


def obtener_inmuebles_comunas(filtro):
  if filtro is None:
    return Inmueble.objects.all().order_by('comuna')
  # si llegamos acá, significa que SI hay un filtro
  # select * from main_inmueble where nombre like '%Elegante%' or descripcion like '%Elegante%';
  return Inmueble.objects.filter(Q(nombre__icontains=filtro) | Q(descripcion__icontains=filtro)).order_by('comuna')


def obtener_inmuebles_region(filtro):
  consulta = '''
  select I.nombre, I.descripcion, R.nombre from main_inmueble as I
  join main_comuna as C on I.comuna_id = C.cod
  join main_region as R on C.region_id = R.cod
  order by R.cod
'''
  if filtro is not None:
    consulta = f'''
  select I.nombre, I.descripcion, R.nombre from main_inmueble as I
  join main_comuna as C on I.comuna_id = C.cod
  join main_region as R on C.region_id = R.cod where I.nombre like '%{filtro}%' or I.descripcion like '%{filtro}%'
  order by R.cod
'''
  cursor = connection.cursor()
  cursor.execute(consulta)
  registros = cursor.fetchall() # esto es un LAZY LOADING
  return registros