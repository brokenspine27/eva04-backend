from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('personas/', views.get_personas),
    
    path('crear/', views.crear_persona),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('persona/', views.persona_aleatoria, name='persona_aleatoria'),
    path('personas/', views.get_personas, name='get_personas'),  # Ya e    path('all_persons/', views.todas_personas, name='all_persons'),
    path('guardar_persona/', views.guardar_persona_api, name='guardar_persona'),   
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')]
