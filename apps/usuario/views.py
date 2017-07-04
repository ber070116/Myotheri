from .models import Usuario
from .serializers import UsuarioSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class UsuarioDetail(APIView):
    """
    Informacion del usuario
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        usuario = Usuario.objects.all()[0]
        serializer = UsuarioSerializer(usuario)

        return Response(serializer.data)
