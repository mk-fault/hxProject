from rest_framework import serializers

from .models import QGModel

class QGModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QGModel
        exclude = ['id']
        extra_kwargs = {
            'code':{
                'write_only':True,
            }
        }