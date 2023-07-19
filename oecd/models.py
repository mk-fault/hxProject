
from django.db import models

# Create your models here.
class OECDModel_T1(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Financing_scheme_code = models.CharField(max_length=12,verbose_name='HF',help_text='HF')
    Financing_scheme = models.CharField(max_length=50,verbose_name='financing_scheme',help_text='financing_scheme')
    Revenues_of_financing_schemes_code = models.CharField(max_length=12,verbose_name='FS',help_text='FS')
    Revenues_of_financing_schemes = models.CharField(max_length=50,verbose_name='revenues_of_financing_schemes',help_text='revenues_of_financing_schemes')
    Measure_code = models.CharField(max_length=12,verbose_name='Measure代码',help_text='Measure代码')
    Measure = models.CharField(max_length=50,verbose_name='Measure',help_text='Measure')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=50,verbose_name='Country',help_text='Country')
    Year = models.IntegerField(verbose_name='Year',help_text='Year')
    Value = models.FloatField(verbose_name='Value',help_text='Value')
    Flag_codes = models.CharField(max_length=12,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=80,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T1'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T1'

class OECDModel_T2(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Variable_code = models.CharField(max_length=12,verbose_name='Variable代码',help_text='Variable代码')
    Variable = models.CharField(max_length=120,verbose_name='Variable',help_text='Variable')
    Measure_code = models.CharField(max_length=12,verbose_name='Measure代码',help_text='Measure代码')
    Measure = models.CharField(max_length=120,verbose_name='Measure',help_text='Measure')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=50,verbose_name='Country',help_text='Country')
    Year = models.IntegerField(verbose_name='Year',help_text='Year')
    Value = models.FloatField(verbose_name='Value',help_text='Value',blank=True,null=True)
    Flag_codes = models.CharField(max_length=12,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=80,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T2'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T2'

class OECDModel_T3(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Provider_code = models.CharField(max_length=12,verbose_name='Provider代码',help_text='Provider代码')
    Provider = models.CharField(max_length=80,verbose_name='Provider',help_text='Provider')
    Factors_of_provision_code = models.CharField(max_length=12,verbose_name='Factors_of_provision代码',help_text='Factors_of_provision代码')
    Factors_of_provision = models.CharField(max_length=50,verbose_name='Factors_of_provision',help_text='Factors_of_provision')
    Measure_code = models.CharField(max_length=12,verbose_name='Measure代码',help_text='Measure代码')
    Measure = models.CharField(max_length=50,verbose_name='Measure',help_text='Measure')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=30,verbose_name='Country',help_text='Country')
    Year = models.IntegerField(verbose_name='Year',help_text='Year')
    Value = models.FloatField(verbose_name='Value',help_text='Value')
    Flag_codes = models.CharField(max_length=4,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=30,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T3'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T3'

class OECDModel_T4(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Financing_scheme_code = models.CharField(max_length=12,verbose_name='HF',help_text='HF')
    Financing_scheme = models.CharField(max_length=60,verbose_name='financing_scheme',help_text='financing_scheme')
    Function_code = models.CharField(max_length=12,verbose_name='HC',help_text='HC')
    Function = models.CharField(max_length=70,verbose_name='Function',help_text='Function')
    Provider_code = models.CharField(max_length=12,verbose_name='Provider代码',help_text='Provider代码')
    Provider = models.CharField(max_length=80,verbose_name='Provider',help_text='Provider')
    Measure_code = models.CharField(max_length=12,verbose_name='Measure代码',help_text='Measure代码')
    Measure = models.CharField(max_length=50,verbose_name='Measure',help_text='Measure')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=40,verbose_name='Country',help_text='Country')
    Unit_Code = models.CharField(max_length=4,verbose_name='Unit代码',help_text='Unit代码')
    Unit = models.CharField(max_length=30,verbose_name='Unit',help_text='Unit')
    PowerCode_Code = models.CharField(max_length=1,verbose_name='PowerCode代码',help_text='PowerCode代码')
    PowerCode = models.CharField(max_length=12,verbose_name='PowerCode',help_text='PowerCode')
    Year = models.IntegerField(verbose_name='Year',help_text='Year')
    Value = models.FloatField(verbose_name='Value',help_text='Value')
    Flag_codes = models.CharField(max_length=12,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=80,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T4'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T4'

class OECDModel_T5(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Variable_code = models.CharField(max_length=12,verbose_name='Variable代码',help_text='Variable代码')
    Variable = models.CharField(max_length=60,verbose_name='Variable',help_text='Variable')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=30,verbose_name='Country',help_text='Country')
    Country_of_origin_code = models.CharField(max_length=4,verbose_name='Country_of_origin代码',help_text='Country_of_origin代码')
    Country_of_origin = models.CharField(max_length=50,verbose_name='Country_of_origin',help_text='Country_of_origin')
    Year = models.IntegerField(verbose_name='Year',help_text='Year')
    Value = models.FloatField(verbose_name='Value',help_text='Value',blank=True,null=True)
    Flag_codes = models.CharField(max_length=4,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=30,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T5'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T5'

class OECDModel_T6(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=30,verbose_name='Country',help_text='Country')
    Indicator_code = models.CharField(max_length=12,verbose_name='Indicator代码',help_text='Indicator代码')
    Indicator = models.CharField(max_length=120,verbose_name='Indicator',help_text='Indicator')
    Gender_code = models.CharField(max_length=1,verbose_name='Gender代码',help_text='Gender代码')
    Gender = models.CharField(max_length=12,verbose_name='Gender',help_text='Gender')
    Age_Group_code = models.CharField(max_length=12,verbose_name='Age_Group代码',help_text='Age_Group代码')
    Age_Group = models.CharField(max_length=30,verbose_name='Age_Group',help_text='Age_Group')
    Value_code = models.CharField(max_length=20,verbose_name='Measure代码',help_text='Measure代码')
    Value = models.CharField(max_length=70,verbose_name='Measure',help_text='Measure')
    Periods = models.CharField(max_length=12,verbose_name='Periods',help_text='Periods',blank=True,null=True)
    NumericValue = models.FloatField(verbose_name='NumericValue',help_text='NumericValue')
    Flag_codes = models.CharField(max_length=8,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=40,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T6'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T6'

class OECDModel_T7(models.Model):
    Code = models.CharField(max_length=8,verbose_name='指标代码',help_text='指标代码')
    Country_code = models.CharField(max_length=4,verbose_name='Country代码',help_text='Country代码')
    Country = models.CharField(max_length=30,verbose_name='Country',help_text='Country')
    Week_number = models.SmallIntegerField(verbose_name='Week_number',help_text='Week_number')
    Gender_code = models.CharField(max_length=8,verbose_name='Gender代码',help_text='Gender代码')
    Gender = models.CharField(max_length=12,verbose_name='Gender',help_text='Gender')
    Age_code = models.CharField(max_length=12,verbose_name='Age代码',help_text='Age代码')
    Age = models.CharField(max_length=20,verbose_name='Age',help_text='Age')
    Variable_code = models.CharField(max_length=12,verbose_name='Variable代码',help_text='Variable代码')
    Variable = models.CharField(max_length=50,verbose_name='Variable',help_text='Variable')
    Year = models.IntegerField(verbose_name='Year',help_text='Year')
    Value = models.FloatField(verbose_name='Value',help_text='Value')
    Flag_codes = models.CharField(max_length=4,verbose_name='Flag_codes',help_text='Flag_codes',blank=True,null=True)
    Flags = models.CharField(max_length=30,verbose_name='Flags',help_text='Flags',blank=True,null=True)

    class Meta:
        verbose_name = 'OECDModel_T7'
        verbose_name_plural = verbose_name
        db_table = 'OECDModel_T7'

