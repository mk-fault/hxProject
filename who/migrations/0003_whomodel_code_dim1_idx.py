# Generated by Django 4.2.4 on 2023-11-21 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("who", "0002_whomodel_spatialdimdetail_alter_whomodel_spatialdim"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="whomodel",
            index=models.Index(fields=["IndicatorCode"], name="code_dim1_idx"),
        ),
    ]
