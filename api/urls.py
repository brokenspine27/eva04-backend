from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('persona/', views.persona_unica, name='persona_unica'),
    path('personas/', views.get_personas, name='get_personas'),
    path('guardar_persona/', views.guardar_persona, name='guardar_persona'),
]
