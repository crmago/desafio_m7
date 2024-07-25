from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from main.models import Inmueble, Region, Comuna
from main.services import crear_inmueble as crear_inmueble_service, eliminar_inmueble as eliminar_inmueble_service
from inmuebles.forms import InmuebleForm

# vamos a crear un test que sólo pasan los 'arrendadores'
def solo_arrendadores(user):
  if user.user_profile.rol == 'arrendador' or user.is_staff == True:
    return True
  else:
    return False

@user_passes_test(solo_arrendadores)
def editar_inmueble(req, id):
    # Obtengo el inmueble a editar
    inmueble = get_object_or_404(Inmueble, id=id)

    if req.method == 'GET':
        # Obtengo las regiones y comunas
        regiones = Region.objects.all()
        comunas = Comuna.objects.all()
        # Obtengo el código de la región
        cod_region_actual = inmueble.comuna_id[0:2]
        # Creo el 'context' con toda la info que requiere el template
        context = {
            'inmueble': inmueble,
            'regiones': regiones,
            'comunas': comunas,
            'cod_region': cod_region_actual
        }
        return render(req, 'editar_inmueble.html', context)
    
    elif req.method == 'POST':
        # Actualizo el inmueble con los datos del formulario
        inmueble.nombre = req.POST.get('nombre')
        inmueble.descripcion = req.POST.get('descripcion')
        inmueble.m2_construidos = req.POST.get('m2_construidos')
        inmueble.m2_totales = req.POST.get('m2_totales')
        inmueble.num_estacionamientos = req.POST.get('num_estacionamientos')
        inmueble.num_habitaciones = req.POST.get('num_habitaciones')
        inmueble.num_baños = req.POST.get('num_baños')
        inmueble.direccion = req.POST.get('direccion')
        inmueble.tipo_inmueble = req.POST.get('tipo_inmueble')
        inmueble.precio = req.POST.get('precio')
        comuna_id = req.POST.get('comuna')
        if comuna_id:
            inmueble.comuna = get_object_or_404(Comuna, id=comuna_id)
        inmueble.save()
        return redirect('/accounts/profile/')
    
    else:
        return HttpResponse('Método no permitido', status=405)

@user_passes_test(solo_arrendadores)
def nuevo_inmueble(req):
  # nos traemos la información de las comunas y las regiones
  regiones = Region.objects.all()
  comunas = Comuna.objects.all()
  # pasar los datos requeridos por el formulario
  context = {
    'tipos_inmueble': Inmueble.tipos,
    'regiones': regiones,
    'comunas': comunas
  }
  return render(req, 'nuevo_inmueble.html', context)

@user_passes_test(solo_arrendadores)
def eliminar_inmueble(req, id):
  eliminar_inmueble_service(id)
  messages.error(req, 'Inmueble ha sido eliminado')
  return redirect('/accounts/profile/')

@user_passes_test(solo_arrendadores)
def crear_inmueble(req):
  # obtener el rut del usuario
  propietario_rut = req.user.username
  # validar metraje (construídos vs totales)
  crear_inmueble_service(
    req.POST['nombre'],
    req.POST['descripcion'],
    int(req.POST['m2_construidos']),
    int(req.POST['m2_totales']),
    int(req.POST['num_estacionamientos']),
    int(req.POST['num_habitaciones']),
    int(req.POST['num_baños']),
    req.POST['direccion'],
    req.POST['tipo_inmueble'],
    int(req.POST['precio']),
    req.POST['comuna_cod'],
    propietario_rut
  )
  messages.success(req, 'Propiedad Creada')
  return redirect('/accounts/profile/')

@user_passes_test(solo_arrendadores)
def nuevo_inmueble(req):
  # nos traemos la información de las comunas y las regiones
  regiones = Region.objects.all()
  comunas = Comuna.objects.all()
  # pasar los datos requeridos por el formulario
  context = {
    'tipos_inmueble': Inmueble.tipos,
    'regiones': regiones,
    'comunas': comunas
  }
  return render(req, 'nuevo_inmueble.html', context)

