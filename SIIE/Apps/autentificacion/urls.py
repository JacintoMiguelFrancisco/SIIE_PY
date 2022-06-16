from django.urls import path
from .views import autentificacion

urlpatterns = [

    path('', autentificacion.as_view(), name="Autentificacion"),
    
]
