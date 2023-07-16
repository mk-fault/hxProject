from django.db import models

# Create your models here.
class QGModel(models.Model):
    measure = models.CharField(max_length=100,verbose_name="指标",help_text="指标")
    code = models.CharField(max_length=10,verbose_name="代码",help_text="代码")
    year = models.IntegerField(verbose_name="年份",help_text="年份")
    value = models.FloatField(verbose_name="值",help_text="值")

    class Meta:
        db_table = "stats_qg"
        verbose_name = "全国指标"
        verbose_name_plural = verbose_name
