# Generated by Django 2.2.2 on 2020-08-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20200813_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='PreviousValue',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='edit',
            name='Value',
            field=models.TextField(default=None, null=True),
        ),
    ]
