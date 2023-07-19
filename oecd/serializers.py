from rest_framework import serializers

from . import models

class OECDModelSerializer_T1(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T1
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Financing_scheme_code':{
                'write_only':True,
            },
            'Revenues_of_financing_schemes_code':{
                'write_only':True,
            },
            'Measure_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            }
        }

class OECDModelSerializer_T2(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T2
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Variable_code':{
                'write_only':True,
            },
            'Measure_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            }
        }

class OECDModelSerializer_T3(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T3
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Provider_code':{
                'write_only':True,
            },
            'Factors_of_provision_code':{
                'write_only':True,
            },
            'Measure_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            }
        }

class OECDModelSerializer_T4(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T4
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Financing_scheme_code':{
                'write_only':True,
            },
            'Function_code':{
                'write_only':True,
            },
            'Measure_code':{
                'write_only':True,
            },
            'Provider_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            },
            'Unit_Code':{
                'write_only':True,
            },
            'PowerCode_Code':{
                'write_only':True,
            }
        }

class OECDModelSerializer_T5(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T5
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Variable_code':{
                'write_only':True,
            },
            'Country_of_origin_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            }
        }

class OECDModelSerializer_T6(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T6
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Indicator_code':{
                'write_only':True,
            },
            'Gender_code':{
                'write_only':True,
            },
            'Age_Group_code':{
                'write_only':True,
            },
            'Value_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            }
        }

class OECDModelSerializer_T7(serializers.ModelSerializer):
    class Meta:
        model = models.OECDModel_T7
        exclude = ['id']
        extra_kwargs = {
            'Code':{
                'write_only':True,
            },
            'Gender_code':{
                'write_only':True,
            },
            'Age_code':{
                'write_only':True,
            },
            'Variable_code':{
                'write_only':True,
            },
            'Country_code':{
                'write_only':True,
            }
        }