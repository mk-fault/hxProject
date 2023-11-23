from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import GenericAPIView

from stats.pagination import MyPageNumberPagination

import pandas as pd
import numpy as np
from sqlalchemy import create_engine


# Create your views here.
'''
    状态码分配:50000-59999
'''

class GBD(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self, request):
        title = request.query_params.get('TITLE',None)
        year = request.query_params.get('YEAR',None)
        location = request.query_params.get('LOCATION',None)
        page = request.query_params.get('PAGE', 1)
        page_size = request.query_params.get('PAGE_SIZE', 10000)
        page = int(page)
        page_size = int(page_size)
        year = int(year) if year else None

        if not title:
            return Response({'code':50001,'msg':'title参数必填'},status=status.HTTP_400_BAD_REQUEST)
        
        # 数据库连接
        try:
            # db = MySQLdb.connect('127.0.0.1','root','000314','hx_gbd')
            db = create_engine('mysql+pymysql://root:000314@127.0.0.1:3306/hx_gbd')
        except:
            return Response({'code':50002,'msg':'数据库连接失败'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # 查询数据
        if year and location:
            sql_query = f"select * from {title} where year={year} and location='{location}' limit {page_size} offset {(page-1)*page_size}"
            sql_query_count = f"select count(*) from {title} where year={year} and location='{location}'"
        elif year:
            sql_query = f"select * from {title} where year={year} limit {page_size} offset {(page-1)*page_size}"
            sql_query_count = f"select count(*) from {title} where year={year}"
        elif location:
            sql_query = f"select * from {title} where location='{location}' limit {page_size} offset {(page-1)*page_size}"
            sql_query_count = f"select count(*) from {title} where location='{location}'"
        else:
            sql_query = f"select * from {title} limit {page_size} offset {(page-1)*page_size}"
            sql_query_count = f"select count(*) from {title}"

        try:
            df = pd.read_sql(sql_query,db)
            df_count = pd.read_sql(sql_query_count,db)
        except:
            return Response({'code':50003,'msg':'查询失败, 请检查该表是否有year或location字段'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        db.dispose()
        # 制作返回数据
        df.replace([np.nan], [None],inplace=True)
        return_data = {}
        total_count = df_count.iloc[0,0]
        total_page = total_count // page_size + 1
        current_page = page
        if current_page > total_page:
            return Response({'code':50004,'msg':'页码超出范围'},status=status.HTTP_400_BAD_REQUEST)
        current_page_size = len(df)
        data = df.to_dict(orient='records')
        return_data['total_count'] = total_count
        return_data['total_page'] = total_page
        return_data['current_page'] = current_page
        return_data['current_page_size'] = current_page_size
        return_data['data'] = data
        return Response(return_data,status=status.HTTP_200_OK)



# class GBD(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly,]

#     def get(self, request):
#         parent = request.query_params.get('PARENT',None)
#         title = request.query_params.get('TITLE',None)
#         year = request.query_params.get('YEAR',None)
#         location = request.query_params.get('LOCATION',None)
#         page = request.query_params.get('PAGE', 1)
#         page = int(page)

#         if not parent:
#             return Response({'code':50000,'msg':'parent参数必填'},status=status.HTTP_400_BAD_REQUEST)
#         if not title:
#             return Response({'code':50001,'msg':'title参数必填'},status=status.HTTP_400_BAD_REQUEST)
        
#         # 查询数据
#         parent = parent.replace('+',' ')
#         queryset = GBDModel.objects.filter(title=title,parent=parent)
#         if len(queryset) == 0:
#             return Response({'code':50002,'msg':'未找到数据'},status=status.HTTP_404_NOT_FOUND)
        
#         # 制作返回数据
#         return_data = {}
#         return_data['parent'] = queryset[0].parent
#         return_data['title'] = queryset[0].title
#         return_data['visualizable'] = queryset[0].visualizable
#         return_data['data'] = []
        
#         if page > queryset[0].total_page:
#             return Response({'code':50003,'msg':'页码超出范围'},status=status.HTTP_400_BAD_REQUEST)
#         if page < 1:
#             return Response({'code':50003,'msg':'页码超出范围'},status=status.HTTP_400_BAD_REQUEST)
        
#         if (year or location) and queryset[0].visualizable == True:
#             temp_data = []
#             for q in queryset:
#                 for i in q.data:
#                     if year:
#                         if i['year'] != int(year):
#                             continue
#                     if location:
#                         if i['location'] != location:
#                             continue
#                     temp_data.append(i)
#             return_data['data'] = temp_data
#         else:
#             return_data['total_page'] = queryset[0].total_page
#             return_data['current_page'] = queryset[page-1].current_page
#             return_data['data'] = queryset[page-1].data

#         # temp_data = queryset[0].data
#         # for i in temp_data:
#         #     if year:
#         #         if i['year'] != int(year):
#         #             continue
#         #     if location:
#         #         if i['location'] != location:
#         #             continue
#         #     return_data['data'].append(i)   


#         return Response(return_data,status=status.HTTP_200_OK)
        
#         # paginator = MyPageNumberPagination()
#         # page_queryset = paginator.paginate_queryset(queryset,request)
#         # 序列化
#         # ser = GBDModelSerializer(page_queryset)
#         # ser = GBDModelSerializer(queryset,many=True)
#         # print(type(ser.data[0]['data']))
#         # print(len(ser.data[5]['data']))
#         # 返回数据
#         # return Response(ser.data)
#         # return paginator.get_paginated_response(ser.data)