from django.contrib import admin
from .models import Flan, ContactForm
# Register your models here.

#TODO: AGREGA EL MODELO CONTACTO AL ADMIN
admin.site.register(ContactForm)
#TODO: AGREGA EL MODELO FLAN AL ADMIN
admin.site.register(Flan)

 