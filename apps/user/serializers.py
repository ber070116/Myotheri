from rest_framework import serializers
from .models import User


# serializacion
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username',
            'email', 'date_of_birth',
        )
