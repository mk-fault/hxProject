# from django.test import TestCase

# Create your tests here.


# Create your tests here.
''''T1'''
from oecd import serializers
import pandas as pd
import numpy as np
dtypes = {
    'Flag Codes' : str,
    'Flags' : str,
    'CODE' : str,
}

df = pd.read_csv('/opt/hxProject/media/type1.csv',encoding='utf-8',dtype=dtypes)
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')
for i in dic:
    i['Code'] = i.pop('CODE')
    i['Financing_scheme_code'] = i.pop('HF')
    i['Revenues_of_financing_schemes_code'] = i.pop('FS')
    i['Measure_code'] = i.pop('MEASURE')
    i['Country_code'] = i.pop('LOCATION')
    i['Flag_codes'] = i.pop('Flag_Codes')

ser = serializers.OECDModelSerializer_T1(data=dic,many=True)
if ser.is_valid():
    print('验证成功')
    ser.save()
    print('添加成功')
else:
    print(ser.errors)

''''---------'''

''''T3'''
from oecd import serializers
import pandas as pd
import numpy as np
dtypes = {
    'Flag Codes' : str,
    'Flags' : str,
    'CODE' : str,
}

df = pd.read_csv('/opt/hxProject/media/type3.csv',encoding='utf-8',dtype=dtypes)
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')
for i in dic:
    i['Code'] = i.pop('CODE')
    i['Provider_code'] = i.pop('HP')
    i['Factors_of_provision_code'] = i.pop('FP')
    i['Measure_code'] = i.pop('MEASURE')
    i['Country_code'] = i.pop('LOCATION')
    i['Flag_codes'] = i.pop('Flag_Codes')

ser = serializers.OECDModelSerializer_T3(data=dic,many=True)
if ser.is_valid():
    print('验证成功')
    ser.save()
    print('添加成功')
else:
    print(ser.errors)

''''---------'''

'''T5'''
from oecd import serializers
import pandas as pd
import numpy as np
dtypes = {
    'Flag Codes' : str,
    'Flags' : str,
    'CODE' : str,
}
df = pd.read_csv('/opt/hxProject/media/type5.csv',encoding='utf-8',dtype=dtypes)
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')
for i in dic:
    i['Code'] = i.pop('CODE')
    i['Variable_code'] = i.pop('VAR')
    i['Country_of_origin_code'] = i.pop('CO2')
    i['Country_code'] = i.pop('COU')
    i['Flag_codes'] = i.pop('Flag_Codes')

ser = serializers.OECDModelSerializer_T5(data=dic,many=True)
if ser.is_valid():
    print('验证成功')
    ser.save()
    print('添加成功')