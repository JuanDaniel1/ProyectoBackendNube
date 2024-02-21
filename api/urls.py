from rest_framework import routers
from api.views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
router  = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('categoria', CategoriasViewSet)
router.register('producto-popular', ProductoPopularViewSet)
router.register('carrito', CarritoViewSet)
router.register('jefe', JefeViewSet)
router.register('comercializadora', ComercViewSet)
router.register('factura', FacturaViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('productos/', ProductoList.as_view()),


  
  

] + router.urls