# Generated by Django 4.2.4 on 2023-11-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wb", "0002_alter_wbmodel_country_name_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="wbmodel",
            index=models.Index(fields=["Indicator_Code"], name="indicator_idx"),
        ),
    ]