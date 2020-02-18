
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import serializers
from .models import Usuarios
from .models import Listas
from .models import Tareas



class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('id', 'username', 'salt', 'hash')



class ListasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listas
        fields = ('id', 'name', 'date', 'parentUserId')


class TareasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tareas
        fields = ('id', 'text', 'release_date', 'done','parentListID')



def index(request):
    rest_list = Tareas.objects.order_by('-release_date')
    context = {'rest_list': rest_list}
    return render(request, 'tareas/index.html', context)


def get_rest_list(request):
    if request.method == "GET":
        rest_list = Tareas.objects.order_by('-release_date')
        serializer = TareasSerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)