# Generated by Django 3.2.6 on 2021-09-01 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testinformation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_information',
            name='test_code',
            field=models.CharField(default='X', max_length=25),
        ),
    ]
