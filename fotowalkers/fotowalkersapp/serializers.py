from rest_framework import serializers
from fotowalkersapp.models import Spot

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('id', 'title', 'created', 'latitude', 'longitude', 'image')
