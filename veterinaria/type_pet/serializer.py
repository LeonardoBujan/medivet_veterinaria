from rest_framework import serializers
from type_pet.models import TypePet

class TypePetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePet
        fields = [
            'id',
            'type_pet_name',
        ]