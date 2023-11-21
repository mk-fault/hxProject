from django.db import models

# Create your models here.
class QGModel(models.Model):
    measure = models.CharField(max_length=100,verbose_name="指标",help_text="指标")
    code = models.CharField(max_length=10,verbose_name="代码",help_text="代码")
    year = models.IntegerField(verbose_name="年份",help_text="年份")
    value = models.FloatField(verbose_name="值",help_text="值")

    class Meta:
        indexes = [
            models.Index(fields=['code'], name='code_idx'),
        ]
        db_table = "stats_qg"
        verbose_name = "全国指标"
        verbose_name_plural = verbose_name

class GSModel(models.Model):
    measure = models.CharField(max_length=100,verbose_name="指标",help_text="指标")
    mea_code = models.CharField(max_length=8,verbose_name="指标代码",help_text="指标代码")
    province = models.CharField(max_length=20,verbose_name="省份",help_text="省份")
    prov_code = models.CharField(max_length=4,verbose_name="省份代码",help_text="省份代码")
    year = models.IntegerField(verbose_name="年份",help_text="年份")
    value = models.FloatField(verbose_name="值",help_text="值")
    class Meta:
        indexes = [
            models.Index(fields=['mea_code'], name='mea_code_idx'),
        ]
        db_table = "stats_gs"
        verbose_name = "各省指标"
        verbose_name_plural = verbose_name