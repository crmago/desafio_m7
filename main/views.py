from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from main.services import editar_user_sin_password, crear_user
from main.models import Comuna, Inmueble, Region, UserProfile


# Create your views here.
@login_required
def home(req):
    datos = req.GET
    region_cod = datos.get('region_cod', '')
    comuna_cod = datos.get('comuna_cod', '')
    palabra = datos.get('palabra', '')

    inmuebles = filtrar_inmuebles(region_cod, comuna_cod, palabra)
    comunas = Comuna.objects.all()
    regiones = Region.objects.all()
    context = {
        'comunas': comunas,
        'regiones': regiones,
        'inmuebles': inmuebles
    }
    return render(req, 'home.html', context)

def filtrar_inmuebles(region_cod, comuna_cod, palabra):
    # Caso 1: comuna_cod != ''
    if comuna_cod:
        inmuebles = Inmueble.objects.filter(comuna__cod=comuna_cod)
        # También podemos aplicar el filtro por palabra si está presente
        if palabra:
            inmuebles = inmuebles.filter(nombre__icontains=palabra)
        return inmuebles

    # Caso 2: comuna_cod == '' y region_cod != ''
    if region_cod:
        inmuebles = Inmueble.objects.filter(comuna__region__cod=region_cod)
        # También podemos aplicar el filtro por palabra si está presente
        if palabra:
            inmuebles = inmuebles.filter(nombre__icontains=palabra)
        return inmuebles

    # Caso 3: comuna_cod == '' y region_cod == ''
    inmuebles = Inmueble.objects.all()
    # Aplicar el filtro por palabra si está presente
    if palabra:
        inmuebles = inmuebles.filter(nombre__icontains=palabra)
    return inmuebles


@login_required
def profile(req):
  user = req.user
  mis_inmuebles = None

  if user.user_profile.rol == 'arrendador':
    mis_inmuebles = user.inmuebles.all()
  elif user.user_profile.rol == 'arrendatario':
    pass

  context = {
    'mis_inmuebles': mis_inmuebles
  }
  return render(req, 'profile.html', context)

@login_required
def edit_user(req):
  # 1. Obtengo el usuario actual
  current_user = req.user
  # llamo a la función para editar el usuario
  if req.POST['telefono'] != '':
    # trailing whitespaces .strip()
    editar_user_sin_password(
      current_user.username,
      req.POST['first_name'],
      req.POST['last_name'],
      req.POST['email'],
      req.POST['direccion'],
      req.POST['rol'],
      req.POST['telefono'])
  else:
    editar_user_sin_password(
      current_user.username,
      req.POST['first_name'],
      req.POST['last_name'],
      req.POST['email'],
      req.POST['direccion'],
      req.POST['rol'])
  messages.success(req, "Ha actualizado sus datos con éxito")
  return redirect('/')

def change_password(req):
  # 1. Recibo los datos del formulario
  password = req.POST['password']
  pass_repeat = req.POST['pass_repeat']
  # 2. Valido que ambas contraseñas coincidan
  if password != pass_repeat:
    messages.error(req, 'Las contraseñas no coinciden')
    return redirect('/accounts/profile')
  # 3. Actualizamos la contraseña
  req.user.set_password(password)
  req.user.save()
  # 4. Le avisamos al usuario que el cambio fué exitoso
  messages.success(req, 'Contraseña actualizada')
  return redirect('/accounts/profile')



# pendientes para trabajar con grupos
def solo_arrendadores(req):
  return HttpResponse('sólo arrendadores')

def solo_arrendatarios(req):
  return HttpResponse('sólo arrendatarios')


def register(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            direccion = form.cleaned_data['direccion']
            telefono = form.cleaned_data.get('telefono')
            rol = form.cleaned_data['rol']

            # Crear usuario
            user, created = User.objects.get_or_create(username=username, defaults={
                'first_name': first_name,
                'last_name': last_name,
                'email': email
            })

            if created:
                user.set_password(password)
                user.save()
                # Crear perfil de usuario
                UserProfile.objects.create(user=user, direccion=direccion, telefono=telefono, rol=rol)
                messages.success(req, "Tu cuenta ha sido creada exitosamente. ¡Bienvenido!")
            else:
                # Si el usuario ya existía, actualiza el perfil
                user_profile, profile_created = UserProfile.objects.get_or_create(user=user)
                if not profile_created:
                    user_profile.direccion = direccion
                    user_profile.telefono = telefono
                    user_profile.rol = rol
                    user_profile.save()
                    messages.success(req, "Tu cuenta ha sido actualizada exitosamente.")
                else:
                    messages.error(req, "El usuario ya existe y su perfil ha sido actualizado.")
            
            # Iniciar sesión
            login(req, user)
            return redirect('home')
        else:
            messages.error(req, "Por favor corrige los errores a continuación.")
    else:
        form = RegisterForm()
    
    return render(req, 'registration/register.html', {'form': form})


def inmueble_detail(req, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    return render(req, 'inmueble_detail.html', {'inmueble': inmueble})