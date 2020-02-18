from django.contrib import admin

# Register your models here.

from .models import Usuarios
admin.site.register(Usuarios)

from .models import Listas
admin.site.register(Listas)

from .models import Tareas
admin.site.register(Tareas)