from rest_framework import serializers
from pet.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            'id',
            'user',
            'type_pet',
            'pet_name',
            'date_birth_pet',
        ]

