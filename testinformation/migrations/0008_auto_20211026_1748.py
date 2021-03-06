# Generated by Django 3.2.6 on 2021-10-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testinformation', '0007_alter_test_information_methodology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_information',
            name='avaliability_tat',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='critical_values',
            field=models.CharField(default='X', max_length=100),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='outreach_notes',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='reference_range',
            field=models.CharField(default='X', max_length=100),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='reportable_range',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='source_of_reference_range',
            field=models.CharField(default='X', max_length=200),
        ),
        migrations.AlterField(
            model_name='test_information',
            name='special_instructions',
            field=models.CharField(default='X', max_length=200),
        ),
    ]
