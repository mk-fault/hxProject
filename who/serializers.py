from rest_framework import serializers

from .models import WHOModel

class WHOModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WHOModel
        exclude = ['id']

