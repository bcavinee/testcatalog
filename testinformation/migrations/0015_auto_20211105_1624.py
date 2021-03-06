# Generated by Django 3.2.6 on 2021-11-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testinformation', '0014_remove_test_information_tat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_information',
            name='amr',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='appropriate_tubetype',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='avaliability',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='complexity',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='cpt_codes',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='critical_values',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='eap',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='instrument',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='labs',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='methodology',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='outreach_notes',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='primary_instrument',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='profciency_testing',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='reference_range',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='refrigerated_stability',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='regulated_analyte',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='reportable_range',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='room_temp_stability',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='source_of_reference_range',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='special_instructions',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='subdiscipline',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='synonym',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='units',
            field=models.CharField(default='', max_length=25),
        ),
    ]
