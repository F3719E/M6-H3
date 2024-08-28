from django.db import models
import uuid
from django.contrib.auth.models import User

# MODELO FLAN
class Flan(models.Model): #* MODELO
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    precio =  models.IntegerField(default=0) #TODO: 5 DIGITOS Y CERO DECIMALES
    detalle_contacto = models.CharField(max_length=150)
    
# MODELO CONTACO
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.TextField(max_length=64)
    customer_email = models.TextField()
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name
    

# MODELO LOGIN
class LoginForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_name = models.TextField(max_length=64)
    customer_email = models.TextField()
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name
    
    