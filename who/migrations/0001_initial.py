# Generated by Django 4.1.8 on 2023-07-15 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WHOModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IndicatorCode', models.CharField(help_text='指标代码', max_length=50, verbose_name='指标代码')),
                ('SpatialDimType', models.CharField(blank=True, help_text='空间维度类型', max_length=30, null=True, verbose_name='空间维度类型')),
                ('SpatialDim', models.CharField(blank=True, help_text='空间维度', max_length=60, null=True, verbose_name='空间维度')),
                ('TimeDimType', models.CharField(blank=True, help_text='时间维度类型', max_length=10, null=True, verbose_name='时间维度类型')),
                ('TimeDim', models.IntegerField(blank=True, help_text='时间维度', null=True, verbose_name='时间维度')),
                ('Dim1Type', models.CharField(blank=True, help_text='维度1类型', max_length=30, null=True, verbose_name='维度1类型')),
                ('Dim1', models.CharField(blank=True, help_text='维度1', max_length=40, null=True, verbose_name='维度1')),
                ('Dim2Type', models.CharField(blank=True, help_text='维度2类型', max_length=30, null=True, verbose_name='维度2类型')),
                ('Dim2', models.CharField(blank=True, help_text='维度2', max_length=30, null=True, verbose_name='维度2')),
                ('Dim3Type', models.CharField(blank=True, help_text='维度3类型', max_length=30, null=True, verbose_name='维度3类型')),
                ('Dim3', models.CharField(blank=True, help_text='维度3', max_length=30, null=True, verbose_name='维度3')),
                ('Value', models.CharField(blank=True, help_text='值', max_length=170, null=True, verbose_name='值')),
                ('NumericValue', models.FloatField(blank=True, help_text='数值', null=True, verbose_name='数值')),
            ],
            options={
                'verbose_name': '世界卫生组织数据',
                'verbose_name_plural': '世界卫生组织数据',
                'db_table': 'who',
            },
        ),
    ]
