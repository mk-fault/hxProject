# Generated by Django 4.1.8 on 2023-07-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oecd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oecdmodel_t6',
            name='Year',
        ),
        migrations.AddField(
            model_name='oecdmodel_t6',
            name='Periods',
            field=models.CharField(blank=True, help_text='Periods', max_length=12, null=True, verbose_name='Periods'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t1',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=12, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t1',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=80, null=True, verbose_name='Flags'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t2',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=12, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t2',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=80, null=True, verbose_name='Flags'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t2',
            name='Value',
            field=models.FloatField(blank=True, help_text='Value', null=True, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t3',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=4, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t3',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=30, null=True, verbose_name='Flags'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t4',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=12, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t4',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=80, null=True, verbose_name='Flags'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t5',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=4, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t5',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=30, null=True, verbose_name='Flags'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t5',
            name='Value',
            field=models.FloatField(blank=True, help_text='Value', null=True, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t6',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=8, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t6',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=40, null=True, verbose_name='Flags'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t7',
            name='Flag_codes',
            field=models.CharField(blank=True, help_text='Flag_codes', max_length=4, null=True, verbose_name='Flag_codes'),
        ),
        migrations.AlterField(
            model_name='oecdmodel_t7',
            name='Flags',
            field=models.CharField(blank=True, help_text='Flags', max_length=30, null=True, verbose_name='Flags'),
        ),
    ]