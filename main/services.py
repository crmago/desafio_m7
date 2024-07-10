from django.contrib.auth.models import User
from main.models import UserProfile
from django.db.utils import IntegrityError



def crear_inmueble(*args):
  pass

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


  