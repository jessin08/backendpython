from rest_framework import serializers
from .models import User1

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User1
        fields = ('name', 'alias')