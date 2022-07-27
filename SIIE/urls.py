#Django
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
#Views
from . import views 
from SIIE.views import index
from .views import Error404View, Error500View
# Errores 
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path("accounts/", include("Apps.accounts.urls")), # New Login XD
    # path('accounts/', include('django.contrib.auth.urls')), # importa las urls de Django si quieres conocer mas entr a esta pagina xD https://learndjango.com/tutorials/django-login-and-logout-tutorial
    path('controlEscolar/', include("Apps.controlEscolar.urls")),
]
handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
