from django.contrib import admin
from django.urls import path,include
from onlyflansapp .views import index,bienvenido,about,contacto,exito,grilla,login,detalles
from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',index),
    path('bienvenido/',bienvenido),
    path('acerca/',about),
    path('contacto/',contacto , name="contacto"),
    path('exito/',exito ),
    path('grilla/',grilla ),
    path('detalles/<uuid:flan_uuid>',detalles, name='detalles'),
    path('onlyflansapp/',include('onlyflansapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    
   
    
    
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

""" django.contrib.auth.urls HABILITA LAS SIGUIENTES 

accounts/ login/ [name='login'] * <- def login() -> render login.html, {user: dta}
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']

"""