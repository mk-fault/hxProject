from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView

from .models import QGModel
from .serializers import QGModelSerializer
from .pagination import MyPageNumberPagination

import pandas as pd

# Create your views here.
'''
    状态码分配:10000-19999
'''

class QG(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self,request):
        # 获取code参数(必填)
        code = request.query_params.get('code')
        if not code:
            return Response({'code':10000,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        # 获取数据
        queryset = QGModel.objects.filter(code=code).order_by('year')
        # 分页
        paginator = MyPageNumberPagination()
        page_queryset = paginator.paginate_queryset(queryset,request)
        # 序列化
        ser = QGModelSerializer(page_queryset,many=True)
        # 返回数据
        return paginator.get_paginated_response(ser.data)
    
    def post(self,request):
        # 获取文件
        obj = request.data.get('file')
        # 检查文件格式
        try:
            df = pd.read_excel(obj)
        except:
            return Response({'msg':'文件格式错误,请传入xlsx文件','code':10001},status=status.HTTP_400_BAD_REQUEST)
        # 检查上传的数据的列名是否正确，以此判断是否为信息表
        if set(df.columns) != set(['measure','code','year','value']):
            return Response({'msg':'文件格式错误,请传入正确的全国范围表','code':10002},status=status.HTTP_400_BAD_REQUEST)
        #  df转字典
        df_dict = df.to_dict(orient='records')
        # 保存数据
        ser = QGModelSerializer(data=df_dict,many=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'上传成功'},status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
