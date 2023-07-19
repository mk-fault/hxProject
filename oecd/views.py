from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import models
from . import serializers
from stats.pagination import MyPageNumberPagination


# Create your views here.
'''
    状态码分配:40000-49999
'''

class OECD(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self,request):

        # 获取type参数(必填)
        type = request.query_params.get('TYPE')
        # 获取code参数(必填)
        code = request.query_params.get('CODE')
        if not type:
            return Response({'code':40000,'msg':'type参数必填'},status=status.HTTP_400_BAD_REQUEST)
        if not code:
            return Response({'code':40001,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        
        # 判断类型
        if type == 'type1':   
            Financing_scheme_code = request.query_params.get('FS',None)
            Revenues_of_financing_schemes_code = request.query_params.get('RFS',None)
            Measure_code = request.query_params.get('MEA',None)
            Country_code = request.query_params.get('COU',None)
            Year = request.query_params.get('YEAR',None)
            queryset = models.OECDModel_T1.objects.filter(Code=code).order_by('Country')
            if Financing_scheme_code:
                queryset = queryset.filter(Financing_scheme_code=Financing_scheme_code).order_by('Country')
            if Revenues_of_financing_schemes_code:
                queryset = queryset.filter(Revenues_of_financing_schemes_code=Revenues_of_financing_schemes_code).order_by('Country')
            if Measure_code:
                queryset = queryset.filter(Measure_code=Measure_code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Year:
                queryset = queryset.filter(Year=Year).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T1(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)  
         
        elif type == 'type2':
            Variable_code = request.query_params.get('VAR',None)
            Measure_code = request.query_params.get('MEA',None)
            Country_code = request.query_params.get('COU',None)
            Year = request.query_params.get('YEAR',None)
            queryset = models.OECDModel_T2.objects.filter(Code=code).order_by('Country')
            if Variable_code:
                queryset = queryset.filter(Variable_code=Variable_code).order_by('Country')
            if Measure_code:
                queryset = queryset.filter(Measure_code=Measure_code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Year:
                queryset = queryset.filter(Year=Year).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T2(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)
        
        elif type == 'type3':
            Provider_code = request.query_params.get('PRO',None)
            Factors_of_provision_code = request.query_params.get('FP',None)
            Measure_code = request.query_params.get('MEA',None)
            Country_code = request.query_params.get('COU',None)
            Year = request.query_params.get('YEAR',None)
            queryset = models.OECDModel_T3.objects.filter(Code=code).order_by('Country')
            if Provider_code:
                queryset = queryset.filter(Provider_code=Provider_code).order_by('Country')
            if Factors_of_provision_code:
                queryset = queryset.filter(Factors_of_provision_code=Factors_of_provision_code).order_by('Country')
            if Measure_code:
                queryset = queryset.filter(Measure_code=Measure_code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Year:
                queryset = queryset.filter(Year=Year).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T3(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)
        
        elif type == 'type4':
            Financing_scheme_code = request.query_params.get('FS',None)
            Function_code = request.query_params.get('FUN',None)
            Provider_code = request.query_params.get('PRO',None)
            Measure_code = request.query_params.get('MEA',None)
            Country_code = request.query_params.get('COU',None)
            Unit_Code = request.query_params.get('UNIT',None)
            PowerCode_Code = request.query_params.get('PC',None)
            Year = request.query_params.get('YEAR',None)
            queryset = models.OECDModel_T4.objects.filter(Code=code).order_by('Country')
            if Financing_scheme_code:
                queryset = queryset.filter(Financing_scheme_code=Financing_scheme_code).order_by('Country')
            if Function_code:
                queryset = queryset.filter(Function_code=Function_code).order_by('Country')
            if Provider_code:
                queryset = queryset.filter(Provider_code=Provider_code).order_by('Country')
            if Measure_code:
                queryset = queryset.filter(Measure_code=Measure_code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Unit_Code:
                queryset = queryset.filter(Unit_Code=Unit_Code).order_by('Country')
            if PowerCode_Code:
                queryset = queryset.filter(PowerCode_Code=PowerCode_Code).order_by('Country')
            if Year:
                queryset = queryset.filter(Year=Year).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T4(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)
        
        elif type == 'type5':
            Variable_code = request.query_params.get('VAR',None)
            Country_code = request.query_params.get('COU',None)
            Country_of_origin_code = request.query_params.get('COU2',None)
            Year = request.query_params.get('YEAR',None)
            queryset = models.OECDModel_T5.objects.filter(Code=code).order_by('Country')
            if Variable_code:
                queryset = queryset.filter(Variable_code=Variable_code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Country_of_origin_code:
                queryset = queryset.filter(Country_of_origin_code=Country_of_origin_code).order_by('Country')
            if Year:
                queryset = queryset.filter(Year=Year).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T5(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)
        
        elif type == 'type6':
            Indicator_code = request.query_params.get('IND',None)
            Country_code = request.query_params.get('COU',None)
            Gender_code = request.query_params.get('GEN',None)
            Age_Group_code = request.query_params.get('AGE',None)
            Value_code = request.query_params.get('VAL',None)
            Periods = request.query_params.get('PER',None)
            queryset = models.OECDModel_T6.objects.filter(Code=code).order_by('Country')
            if Indicator_code:
                queryset = queryset.filter(Indicator_code=Indicator_code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Gender_code:
                queryset = queryset.filter(Gender_code=Gender_code).order_by('Country')
            if Age_Group_code:
                queryset = queryset.filter(Age_Group_code=Age_Group_code).order_by('Country')
            if Value_code:
                queryset = queryset.filter(Value_code=Value_code).order_by('Country')
            if Periods:
                queryset = queryset.filter(Periods=Periods).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T6(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)
        
        elif type == 'type7':
            Country_code = request.query_params.get('COU',None)
            Gender_code = request.query_params.get('GEN',None)
            Age_code = request.query_params.get('AGE',None)
            Variable_code = request.query_params.get('VAR',None)
            Year = request.query_params.get('YEAR',None)
            queryset = models.OECDModel_T7.objects.filter(Code=code).order_by('Country')
            if Country_code:
                queryset = queryset.filter(Country_code=Country_code).order_by('Country')
            if Gender_code:
                queryset = queryset.filter(Gender_code=Gender_code).order_by('Country')
            if Age_code:
                queryset = queryset.filter(Age_code=Age_code).order_by('Country')
            if Variable_code:
                queryset = queryset.filter(Variable_code=Variable_code).order_by('Country')
            if Year:
                queryset = queryset.filter(Year=Year).order_by('Country')
            # 分页
            paginator = MyPageNumberPagination()
            page_queryset = paginator.paginate_queryset(queryset,request)
            # 序列化
            ser = serializers.OECDModelSerializer_T7(page_queryset,many=True)
            # 返回数据
            return paginator.get_paginated_response(ser.data)
        
        else:
            return Response({'code':40002,'msg':'type参数错误'},status=status.HTTP_400_BAD_REQUEST)
        
    
class IndexList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    @staticmethod
    def remove_duplicates(lst):
        unique = set(frozenset(d.items()) for d in lst)
        return [dict(s) for s in unique]

    def get(self,request):

        # 获取type参数(必填)
        type = request.query_params.get('TYPE')
        # 获取code参数(必填)
        code = request.query_params.get('CODE')
        if not type:
            return Response({'code':40003,'msg':'type参数必填'},status=status.HTTP_400_BAD_REQUEST)
        if not code:
            return Response({'code':40004,'msg':'code参数必填'},status=status.HTTP_400_BAD_REQUEST)
        
        if type == 'type1':
            queryset = models.OECDModel_T1.objects.filter(Code=code).order_by('Country')
            Financing_scheme_list = queryset.values('Financing_scheme_code','Financing_scheme').distinct()
            Financing_scheme_list = self.remove_duplicates(Financing_scheme_list)
            Revenues_of_financing_schemes_list = queryset.values('Revenues_of_financing_schemes_code','Revenues_of_financing_schemes').distinct()
            Revenues_of_financing_schemes_list = self.remove_duplicates(Revenues_of_financing_schemes_list)
            Measure_list = queryset.values('Measure_code','Measure').distinct()
            Measure_list = self.remove_duplicates(Measure_list)
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Year_list = list(set(queryset.values_list('Year',flat=True)))
            return Response({'Financing_scheme_list':Financing_scheme_list,'Revenues_of_financing_schemes_list':Revenues_of_financing_schemes_list,'Measure_list':Measure_list,'Country_list':Country_list,'Year_list':Year_list},status=status.HTTP_200_OK)
            
        elif type == 'type2':
            queryset = models.OECDModel_T2.objects.filter(Code=code).order_by('Country')
            Variable_list = queryset.values('Variable_code','Variable').distinct()
            Variable_list = self.remove_duplicates(Variable_list)
            Measure_list = queryset.values('Measure_code','Measure').distinct()
            Measure_list = self.remove_duplicates(Measure_list)
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Year_list = list(set(queryset.values_list('Year',flat=True)))
            return Response({'Variable_list':Variable_list,'Measure_list':Measure_list,'Country_list':Country_list,'Year_list':Year_list},status=status.HTTP_200_OK)
        
        elif type == 'type3':
            queryset = models.OECDModel_T3.objects.filter(Code=code).order_by('Country')
            Provider_list = queryset.values('Provider_code','Provider').distinct()
            Provider_list = self.remove_duplicates(Provider_list)
            Factors_of_provision_list = queryset.values('Factors_of_provision_code','Factors_of_provision').distinct()
            Factors_of_provision_list = self.remove_duplicates(Factors_of_provision_list)
            Measure_list = queryset.values('Measure_code','Measure').distinct()
            Measure_list = self.remove_duplicates(Measure_list)
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Year_list = list(set(queryset.values_list('Year',flat=True)))
            return Response({'Provider_list':Provider_list,'Factors_of_provision_list':Factors_of_provision_list,'Measure_list':Measure_list,'Country_list':Country_list,'Year_list':Year_list},status=status.HTTP_200_OK)
        
        elif type == 'type4':
            queryset = models.OECDModel_T4.objects.filter(Code=code).order_by('Country')
            Financing_scheme_list = queryset.values('Financing_scheme_code','Financing_scheme').distinct()
            Financing_scheme_list = self.remove_duplicates(Financing_scheme_list)
            Function_list = queryset.values('Function_code','Function').distinct()
            Function_list = self.remove_duplicates(Function_list)
            Provider_list = queryset.values('Provider_code','Provider').distinct()
            Provider_list = self.remove_duplicates(Provider_list)
            Measure_list = queryset.values('Measure_code','Measure').distinct()
            Measure_list = self.remove_duplicates(Measure_list)
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Unit_list = queryset.values('Unit_Code','Unit').distinct()
            Unit_list = self.remove_duplicates(Unit_list)
            PowerCode_list = queryset.values('PowerCode_Code','PowerCode').distinct()
            PowerCode_list = self.remove_duplicates(PowerCode_list)
            Year_list = list(set(queryset.values_list('Year',flat=True)))
            return Response({'Financing_scheme_list':Financing_scheme_list,'Function_list':Function_list,'Provider_list':Provider_list,'Measure_list':Measure_list,'Country_list':Country_list,'Unit_list':Unit_list,'PowerCode_list':PowerCode_list,'Year_list':Year_list},status=status.HTTP_200_OK)
        
        elif type == 'type5':
            queryset = models.OECDModel_T5.objects.filter(Code=code).order_by('Country')
            Variable_list = queryset.values('Variable_code','Variable').distinct()
            Variable_list = self.remove_duplicates(Variable_list)
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Country_of_origin_list = queryset.values('Country_of_origin_code','Country_of_origin').distinct()
            Country_of_origin_list = self.remove_duplicates(Country_of_origin_list)
            Year_list = list(set(queryset.values_list('Year',flat=True)))
            return Response({'Variable_list':Variable_list,'Country_list':Country_list,'Country_of_origin_list':Country_of_origin_list,'Year_list':Year_list},status=status.HTTP_200_OK)
        
        elif type == 'type6':
            queryset = models.OECDModel_T6.objects.filter(Code=code).order_by('Country')
            Indicator_list = queryset.values('Indicator_code','Indicator').distinct()
            Indicator_list = self.remove_duplicates(Indicator_list)
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Gender_list = queryset.values('Gender_code','Gender').distinct()
            Gender_list = self.remove_duplicates(Gender_list)
            Age_Group_list = queryset.values('Age_Group_code','Age_Group').distinct()
            Age_Group_list = self.remove_duplicates(Age_Group_list)
            Value_list = queryset.values('Value_code','Value').distinct()
            Value_list = self.remove_duplicates(Value_list)
            Periods_list = list(set(queryset.values_list('Periods',flat=True)))
            return Response({'Indicator_list':Indicator_list,'Country_list':Country_list,'Gender_list':Gender_list,'Age_Group_list':Age_Group_list,'Value_list':Value_list,'Periods_list':Periods_list},status=status.HTTP_200_OK)
        
        elif type == 'type7':
            queryset = models.OECDModel_T7.objects.filter(Code=code).order_by('Country')
            Country_list = queryset.values('Country_code','Country').distinct()
            Country_list = self.remove_duplicates(Country_list)
            Gender_list = queryset.values('Gender_code','Gender').distinct()
            Gender_list = self.remove_duplicates(Gender_list)
            Age_list = queryset.values('Age_code','Age').distinct()
            Age_list = self.remove_duplicates(Age_list)
            Variable_list = queryset.values('Variable_code','Variable').distinct()
            Variable_list = self.remove_duplicates(Variable_list)
            Year_list = list(set(queryset.values_list('Year',flat=True)))
            return Response({'Country_list':Country_list,'Gender_list':Gender_list,'Age_list':Age_list,'Variable_list':Variable_list,'Year_list':Year_list},status=status.HTTP_200_OK)
        
        else:
            return Response({'code':40005,'msg':'type参数错误'},status=status.HTTP_400_BAD_REQUEST)

