from django.contrib import admin
from django.urls import path, include
# dos librerias  recien añadido para subir fotos 
from django.conf import settings
from django.conf.urls.static import static
from api.views import TiendaApiView,TiendaCATApiView

urlpatterns = [
    path('productos/', TiendaApiView.as_view()),
    path('productosCat/', TiendaCATApiView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
#    urlpatterns+=static(static.MEDIA_URL, document_root=settings.MEDIA_ROOT)
