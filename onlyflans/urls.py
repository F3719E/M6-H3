from django.contrib import admin
from django.urls import path,include
from onlyflansapp .views import index,bienvenido,about,contacto,exito,login
from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',index),
    path('bienvenido/',bienvenido),
    path('acerca/',about),
    path('contacto/',contacto ),
    path('exito/',exito ),
    path('login/',login ),
    path('onlyflansapp/',include('onlyflansapp.urls')),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
