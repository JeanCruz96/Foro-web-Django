from django.urls import path
from django.conf.urls import url,include
from django.db import models
from Proyecto001.apps.Gestionacademica import views
#login1 esta importado en la urls.py GLOBAL 
from Proyecto001.apps.Gestionacademica.views import registrousuario
from Proyecto001.apps.Gestionacademica.views import menuforo

#URLS LOCALES ,SOLO PARA EL PROYECTO "apps"
urlpatterns = [
   path('login/',views.index),
   path('registro/',views.registrousuario),
   path('menuforo/',views.menuforo),
   path('buscar/',views.buscar),

]