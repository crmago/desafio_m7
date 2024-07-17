from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(req):
  return render(req, 'home.html')

def solo_arrendadores(req):
  return HttpResponse('sólo arrendadores')

def solo_arrendatarios(req):
  return HttpResponse('sólo arrendatarios')