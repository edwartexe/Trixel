from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import UsuarioSerializer
from .models import Usuarios
from .serializers import ListasSerializer
from .models import Listas
from .serializers import TareasSerializer
from .models import Tareas


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all().order_by('username')
    serializer_class = UsuarioSerializer
    
class ListasViewSet(viewsets.ModelViewSet):
    queryset = Listas.objects.all().order_by('id')
    serializer_class = ListasSerializer
    
class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all().order_by('id')
    serializer_class = TareasSerializer