from django.contrib import admin

# Register your models here.
from .models import Autos
from .models import Make

admin.site.register(Make)
admin.site.register(Autos)
