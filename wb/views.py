from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView

from .models import WBModel
from .serializers import WBModelSerializer
from stats.pagination import MyPageNumberPagination


# Create your views here.
'''
    状态码分配:20000-29999
'''

class WB(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self,request):
        # 获取code参数(必填)
        code = request.query_params.get('CODE')
        country = request.query_params.get('COU',None)
        year = request.query_params.get('YEAR',None)
        if not code:
            return Response({'code':20000,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        # 获取数据
        queryset = WBModel.objects.filter(Indicator_Code=code).order_by('Country_Name')
        if country:
            queryset = queryset.filter(Country_Code=country).order_by('year')
        if year:
            queryset = queryset.filter(year=year).order_by('Country_Code')
        # 分页
        paginator = MyPageNumberPagination()
        page_queryset = paginator.paginate_queryset(queryset,request)
        # 序列化
        ser = WBModelSerializer(page_queryset,many=True)
        # 返回数据
        return paginator.get_paginated_response(ser.data)
    
class IndexList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @staticmethod
    def remove_duplicates(lst):
        unique = set(frozenset(d.items()) for d in lst)
        return [dict(s) for s in unique]

    def get(self,request):
        # 获取code参数(必填)
        code = request.query_params.get('CODE')
        if not code:
            return Response({'code':20001,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        # 获取数据
        queryset = WBModel.objects.filter(Indicator_Code=code).order_by('Country_Name')
        countrylist = queryset.values('Country_Code','Country_Name')
        countrylist = self.remove_duplicates(countrylist)
        yearlist = list(set(queryset.values_list('year',flat=True)))
        # 返回数据
        return Response({'countrylist':countrylist,'yearlist':yearlist},status=status.HTTP_200_OK)