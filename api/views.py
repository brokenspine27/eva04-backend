from rest_framework.response import Response
from rest_framework.decorators import api_view
from myApp.models import Persona
from .serializers import PersonaSerializer

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