# Generated by Django 2.2.2 on 2020-07-01 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahj_gis', '0003_auto_20200701_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='AHJ',
        ),
        migrations.RemoveField(
            model_name='county',
            name='AHJ',
        ),
    ]
