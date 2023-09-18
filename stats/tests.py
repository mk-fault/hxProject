# from django.test import TestCase

# Create your tests here.

"""全国"""
from stats.serializers import QGModelSerializer
import pandas as pd
import numpy as np

# Create your tests here.
df = pd.read_excel("/home/mk/python/hxProject/media/qg_total.xlsx")
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')

ser = QGModelSerializer(data=dic,many=True)
if ser.is_valid():
    print('验证成功')
    ser.save()
    print('添加成功')
else:
    print(ser.errors)


"""各省"""
from stats.serializers import GSModelSerializer
import pandas as pd
import numpy as np

# Create your tests here.
df = pd.read_excel("/home/mk/python/hxProject/media/gs_total.xlsx")
df.replace([np.nan], [None],inplace=True)
dic = df.to_dict(orient='records')

ser = GSModelSerializer(data=dic,many=True)
if ser.is_valid():
    print('验证成功')
    ser.save()
    print('添加成功')
else:
    print(ser.errors)