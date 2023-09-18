from rest_framework import serializers

from .models import QGModel, GSModel

class QGModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QGModel
        exclude = ['id']
        extra_kwargs = {
            'code':{
                'write_only':True,
            }
        }

class GSModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSModel
        exclude = ['id']
        extra_kwargs = {
            'mea_code':{
                'write_only':True,
            },
            'prov_code':{
                'write_only':True,
            }
        }