# Generated by Django 3.2.6 on 2021-11-05 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testinformation', '0013_auto_20211105_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_information',
            name='tat',
        ),
    ]