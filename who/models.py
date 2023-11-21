from django.db import models

# Create your models here.
class WHOModel(models.Model):
    IndicatorCode = models.CharField(max_length=50,verbose_name='指标代码',help_text='指标代码')
    SpatialDimType = models.CharField(max_length=30,verbose_name='空间维度类型',help_text='空间维度类型',blank=True,null=True)
    SpatialDim = models.CharField(max_length=60,verbose_name='空间维度代码',help_text='空间维度代码',blank=True,null=True)
    SpatialDimDetail = models.CharField(max_length=40,verbose_name='空间维度',help_text='空间维度',blank=True,null=True)
    TimeDimType = models.CharField(max_length=10,verbose_name='时间维度类型',help_text='时间维度类型',blank=True,null=True)
    TimeDim = models.IntegerField(verbose_name='时间维度',help_text='时间维度',blank=True,null=True)
    Dim1Type = models.CharField(max_length=30,verbose_name='维度1类型',help_text='维度1类型',blank=True,null=True)
    Dim1 = models.CharField(max_length=40,verbose_name='维度1',help_text='维度1',blank=True,null=True)
    Dim2Type = models.CharField(max_length=30,verbose_name='维度2类型',help_text='维度2类型',blank=True,null=True)
    Dim2 = models.CharField(max_length=30,verbose_name='维度2',help_text='维度2',blank=True,null=True)
    Dim3Type = models.CharField(max_length=30,verbose_name='维度3类型',help_text='维度3类型',blank=True,null=True)
    Dim3 = models.CharField(max_length=30,verbose_name='维度3',help_text='维度3',blank=True,null=True)
    Value = models.CharField(max_length=170,verbose_name='值',help_text='值',blank=True,null=True)
    NumericValue = models.FloatField(verbose_name='数值',help_text='数值',blank=True,null=True)

    class Meta:
        indexes = [
            models.Index(fields=['IndicatorCode'], name='code_dim1_idx'),
        ]
        db_table = 'who'
        verbose_name = '世界卫生组织数据'
        verbose_name_plural = verbose_name
