from rest_framework import serializers
from .models import Usuario


# serializacion
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'id', 'nombre_usuario',
            'email', 'fecha_nacimiento',
        )
