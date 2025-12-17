#vistas ultra corregidass
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from myApp.models import Persona
from .serializers import PersonaSerializer

# Persona aleatoria (SIN token)
@api_view(['GET'])
def persona_unica(request):
    try:
        personas = Persona.objects.all()
        if personas.exists():
            persona = random.choice(personas)
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        else:
            return Response({
                'nombre': random.choice(['Juan', 'María', 'Carlos', 'Ana', 'Pedro']),
                'apellido': random.choice(['Pérez', 'Gómez', 'Rodríguez', 'López']),
                'edad': random.randint(20, 60)
            })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Todas las personas (CON token)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_personas(request): 
    """Devuelve TODAS las personas - Requiere token JWT"""
    try:
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Guardar persona (CON token) 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def guardar_persona(request):
    try:
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

