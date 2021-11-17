# Generated by Django 3.2.6 on 2021-10-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testinformation', '0010_rename_avaliability_tat_test_information_avaliability'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_information',
            name='complexity',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AddField(
            model_name='test_information',
            name='cpt_codes',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AddField(
            model_name='test_information',
            name='primary_instrument',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AddField(
            model_name='test_information',
            name='profciency_testing',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AddField(
            model_name='test_information',
            name='regulated_analyte',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AddField(
            model_name='test_information',
            name='subdiscipine',
            field=models.CharField(default='X', max_length=200),
        ),
    ]