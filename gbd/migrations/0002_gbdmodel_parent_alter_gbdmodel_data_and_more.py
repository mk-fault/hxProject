# Generated by Django 4.2.4 on 2023-11-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gbd", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gbdmodel",
            name="parent",
            field=models.CharField(
                blank=True, help_text="父级", max_length=150, null=True, verbose_name="父级"
            ),
        ),
        migrations.AlterField(
            model_name="gbdmodel",
            name="data",
            field=models.JSONField(
                blank=True, help_text="数据", null=True, verbose_name="数据"
            ),
        ),
        migrations.AlterField(
            model_name="gbdmodel",
            name="title",
            field=models.CharField(
                blank=True, help_text="标题", max_length=100, null=True, verbose_name="标题"
            ),
        ),
    ]