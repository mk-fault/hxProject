from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView

from .models import WHOModel
from .serializers import WHOModelSerializer
from stats.pagination import MyPageNumberPagination

import pandas as pd

# Create your views here.
'''
    状态码分配:30000-39999
'''

class WHO(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self,request):
        # 获取code参数(必填)
        code = request.query_params.get('code')
        spatialtype = request.query_params.get('spatialtype',None)
        spatial = request.query_params.get('spatial',None)
        time = request.query_params.get('year',None)
        dim1 = request.query_params.get('dim1',None)
        dim2 = request.query_params.get('dim2',None)
        dim3 = request.query_params.get('dim3',None)
        if not code:
            return Response({'code':30000,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        # 获取数据
        queryset = WHOModel.objects.filter(IndicatorCode=code).order_by('SpatialDim')
        if spatialtype:
            queryset = queryset.filter(SpatialDimType=spatialtype).order_by('SpatialDim')
        if spatial:
            queryset = queryset.filter(SpatialDim=spatial).order_by('SpatialDim')
        if time:
            queryset = queryset.filter(TimeDim=time).order_by('SpatialDim')
        if dim1:
            queryset = queryset.filter(Dim1=dim1).order_by('SpatialDim')
        if dim2:
            queryset = queryset.filter(Dim2=dim2).order_by('SpatialDim')
        if dim3:
            queryset = queryset.filter(Dim3=dim3).order_by('SpatialDim')
        # 分页
        paginator = MyPageNumberPagination()
        page_queryset = paginator.paginate_queryset(queryset,request)
        # 序列化
        ser = WHOModelSerializer(page_queryset,many=True)
        # 返回数据
        return paginator.get_paginated_response(ser.data)
    
class IndexList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self,request):
        # 获取code参数(必填)
        code = request.query_params.get('code')
        if not code:
            return Response({'code':30001,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        
        # 获取数据
        queryset = WHOModel.objects.filter(IndicatorCode=code).order_by('SpatialDim')

        # 制作空间维度字典
        lst = queryset.values_list('SpatialDimType',flat=True)
        SpatialDimType = list(set(lst))

        # if not all(elem is None for elem in lst):
        #     lst = list(set(lst))
        #     for i in lst:
        #         SpatialDimDic[i] = list(set(queryset.filter(SpatialDimType=i).values_list('SpatialDim',flat=True)))

        # 制作Dim1维度字典
        lst = queryset.values_list('Dim1Type',flat=True)
        Dim1Dic = {}
        if not all(elem is None for elem in lst):
            lst = list(set(lst))
            for i in lst:
                Dim1Dic[i] = list(set(queryset.filter(Dim1Type=i).values_list('Dim1',flat=True)))

        # 制作Dim2维度字典
        lst = list(queryset.values_list('Dim2Type',flat=True))
        Dim2Dic = {}
        if not all(elem is None for elem in lst):
            lst = list(set(lst))
            for i in lst:
                Dim2Dic[i] = list(set(queryset.filter(Dim2Type=i).values_list('Dim2',flat=True)))

        # 制作Dim3维度字典
        lst = queryset.values_list('Dim3Type',flat=True)
        Dim3Dic = {}
        if not all(elem is None for elem in lst):
            lst = list(set(lst))
            for i in lst:
                Dim3Dic[i] = list(set(queryset.filter(Dim3Type=i).values_list('Dim3',flat=True)))

        # 制作时间维度字典
        lst = queryset.values_list('TimeDimType',flat=True)
        TimeDimDic = {}
        if not all(elem is None for elem in lst):
            lst = list(set(lst))
            for i in lst:
                TimeDimDic[i] = list(set(queryset.filter(TimeDimType=i).values_list('TimeDim',flat=True)))

        # 返回数据
        return Response({
            'SpatialDimTypeDic':SpatialDimType,
            'Dim1Dic':Dim1Dic,
            'Dim2Dic':Dim2Dic,
            'Dim3Dic':Dim3Dic,
            'TimeDimDic':TimeDimDic,
        },status=status.HTTP_200_OK)
