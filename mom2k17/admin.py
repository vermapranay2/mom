from django.contrib import admin

# Register your models here.
from .models import Info, Register, School

admin.site.register(Info)
admin.site.register(Register)
admin.site.register(School)
