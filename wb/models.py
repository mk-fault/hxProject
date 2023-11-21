from django.db import models

# Create your models here.
class WBModel(models.Model):
    Country_Name = models.CharField(max_length=80,verbose_name="国家",help_text="国家")
    Country_Code = models.CharField(max_length=20,verbose_name="国家代码",help_text="国家代码")
    Indicator_Name = models.CharField(max_length=150,verbose_name="指标",help_text="指标")
    Indicator_Code = models.CharField(max_length=50,verbose_name="指标代码",help_text="指标代码")
    year = models.IntegerField(verbose_name="年份",help_text="年份")
    value = models.FloatField(verbose_name="值",help_text="值",blank=True,null=True)

    class Meta:
        indexes = [
            models.Index(fields=['Indicator_Code'], name='indicator_idx'),
        ]
        db_table = "wb"
        verbose_name = "worldbank"
        verbose_name_plural = verbose_name