from django.test import TestCase
from wb.serializers import WBModelSerializer
import pandas as pd
import numpy as np

# Create your tests here.
df = pd.read_csv('/home/mk/python/hxProject/media/wb_total2.csv',encoding='utf-8')
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')
for item in dic:
    item['Country_Name'] = item.pop('Country Name')
    item['Country_Code'] = item.pop('Country Code')
    item['Indicator_Name'] = item.pop('Indicator Name')
    item['Indicator_Code'] = item.pop('Indicator Code')

ser = WBModelSerializer(data=dic,many=True)
if ser.is_valid():
    ser.save()
    print('添加成功')
else:
    print(ser.errors)