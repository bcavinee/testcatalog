# Generated by Django 3.2.6 on 2021-10-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testinformation', '0008_auto_20211026_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_information',
            name='tat',
            field=models.CharField(default='X', max_length=200),
        ),
    ]