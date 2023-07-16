from rest_framework import serializers

from .models import WBModel

class WBModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WBModel
        exclude = ['id']
        extra_kwargs = {
            'Country_Code':{
                'write_only':True,
            },
            'Indicator_Code':{
                'write_only':True,
            },
        }