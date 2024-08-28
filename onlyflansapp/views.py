from django.core.management.base import BaseCommand, no_translations
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, LoginForm
from .forms import PostForm,ContactForm,LoginPostForm
from django.contrib.auth.decorators import login_required



# Create your views here.


def index(request):
        # context = {
        # "mensaje": "este es un msj str ",
        # "productos": [{"titulo": "titulo tarjeta", "descripcion":"descripcion de la tarjeta"},{"titulo": "titulo tarjeta", "descripcion":"descripcion de la tarjeta"},{"titulo": "titulo tarjeta", "descripcion":"descripcion de la tarjeta"}]
        # }
    
        flans_publicos = Flan.objects.filter(is_private=False)
        return render(request, 'index.html', {"flans_publicos": flans_publicos})
    
        # return render(request, 'index.html', context)

@login_required
def bienvenido(request):
        # template = loader.get_template('bienvenido.html')
        # context = {
        #         "usuario":  "PEPE",
        #         # "usuario":  "PEPE1",
        #         }
        print(f'USUARIO: {request.user.username}') 
       
        flans_privados = Flan.objects.filter(is_private=True)
        return render(request, 'bienvenido.html', {"flans_privados": flans_privados})

        # return render(request, 'bienvenido.html', context)
        # return HttpResponse(template.render(context, request)) 

def about(request):
    return render(request, 'about.html', {})


def contacto(request):
    if request.method == 'POST':
        form = PostForm(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        print('POST')
        print(str(form.is_valid()))
        
        # print(str(form))
        # print(form.declared_fields.get("customer_email").__str__())
       
        # print(ContactForm.customer_email.value_from_object())
        # print(form.customer_name.bound_data())
     
        # print( form["customer_email"].value())
        # print (form.data["customer_email"])
        
        # form.customer_email
        
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            print('POST form.is_valid')
            ContactForm.objects.create(**form.cleaned_data) # TODO: ** **form.cleaned_data PASA LOS DATOS COMO ARGUMENTOS PARA INSERT EN LA DDBB
            # return HttpResponseRedirect('exito.html')
            return render(request, 'exito.html', {})
    else: 
        print('GET')
        form = PostForm()   
    return render(request, 'contacto.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginPostForm(request.POST) #TODO: SON LOS CAMPOS Y VALORES DEL FORMULARIO ES UN DICCIONARIO
        print('LOGIN POST')
        print(str(form.is_valid()))
        
        if form.is_valid(): #TODO: VALIDA LOS CAMPOS O PARAMETROS
            print('POST form.is_valid')
            LoginForm.objects.create(**form.cleaned_data) # TODO: ** **form.cleaned_data PASA LOS DATOS COMO ARGUMENTOS PARA INSERT EN LA DDBB
            # return HttpResponseRedirect('exito.html')
            return render(request, 'exito.html', {})
    else: 
        print('GET')
        form = LoginPostForm()   
    return render(request, 'login.html', {'form':form})

# def contacto_model_form(request):
#     return render(request, 'contacto.html', {})
# *  --- apply ContactModelForm ---

def exito(request):
    return render(request, 'exito.html', {})


#TODO: VISTA GRILLA
def grilla(request):
    flans_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'grilla.html', {"flans_publicos": flans_publicos})


#TODO: VISTA DETALLE
def detalles(request, flan_uuid):
    print(f'FLAN.FLAN_UUID: {flan_uuid}')
    flan = Flan.objects.get(flan_uuid = flan_uuid)
    
    return render(request, 'detalles.html', {'flan' : flan})