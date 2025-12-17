import random
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from myApp.models import Persona
from .serializers import PersonaSerializer

# 1. Persona aleatoria (NO requiere autenticación)
@api_view(['GET'])
def persona_aleatoria(request):
    try:
        # Obtén todas las personas
        personas = Persona.objects.all()
        if personas.exists():
            # Elige una persona aleatoria 
            persona = random.choice(personas)
            serializer = PersonaSerializer(persona)
            return Response(serializer.data)
        else:
            # Si no hay personas en la BD, crea una de ejemplo
            return Response({
                'nombre': random.choice(['Juan', 'María', 'Carlos', 'Ana', 'Pedro']),
                'apellido': random.choice(['Pérez', 'Gómez', 'Rodríguez', 'López']),
                'edad': random.randint(20, 60)  # Usa randint para números[citation:3]
            })
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 2. Todas las personas (SÍ requiere autenticación con JWT)
@api_view(['GET'])
@permission_classes([IsAuthenticated])  # Requiere token JWT válido
def todas_personas(request):
    personas = Persona.objects.all()
    serializer = PersonaSerializer(personas, many=True)
    return Response(serializer.data)

# 3. Guardar persona (SÍ requiere autenticación con JWT)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def guardar_persona(request):
    serializer = PersonaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Funciones básicas
@api_view(['GET'])
def get_personas(request):
    personas = Persona.objects.all()
    personas_json = PersonaSerializer(personas, many=True)
    return Response(personas_json.data)

@api_view(['POST'])
def crear_persona(request):
    persona = PersonaSerializer(data=request.data)
    if persona.is_valid():
        persona.save()
        return Response(persona.data)