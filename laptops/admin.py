from django.contrib import admin
from .models import Laptop, Program, Graphic

# Register your models here.

admin.site.register(Laptop)
admin.site.register(Program)
admin.site.register(Graphic)