# from django.test import TestCase

# Create your tests here.
from who.serializers import WHOModelSerializer
import pandas as pd
import numpy as np

# Create your tests here.
dtyps = {
    'Dim2Type': str,
    'Dim3Type': str,
    'Dim2' : str,
    'Dim3' : str,
    'Value' : str,
    'Comments' : str,
}
df = pd.read_csv('/opt/hxProject/media/who_total.csv',encoding='utf-8',dtype=dtyps)
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')

ser = WHOModelSerializer(data=dic,many=True)
if ser.is_valid():
    print('验证成功')
    ser.save()
    print('添加成功')
else:
    print(ser.errors)