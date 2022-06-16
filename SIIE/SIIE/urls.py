#Django
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
#Views
from . import views 
from .views import Error404View 
# Errores 
from django.conf.urls import handler404


urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('autentificacion/', include("Apps.autentificacion.urls")),
    path('controlEscolar/', include("Apps.controlEscolar.urls")),
]
handler404 = Error404View.as_view()

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
