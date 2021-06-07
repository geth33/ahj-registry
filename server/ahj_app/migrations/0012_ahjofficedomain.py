# Generated by Django 3.1.3 on 2021-06-07 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahj_app', '0011_auto_20210606_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='AHJOfficeDomain',
            fields=[
                ('DomainID', models.AutoField(db_column='DomainID', primary_key=True, serialize=False)),
                ('Domain', models.CharField(db_column='Domain', max_length=254)),
                ('AHJID', models.ForeignKey(db_column='AHJID', on_delete=django.db.models.deletion.DO_NOTHING, to='ahj_app.ahj')),
            ],
        ),
    ]