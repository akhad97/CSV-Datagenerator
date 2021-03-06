# Generated by Django 3.2.6 on 2021-08-14 18:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210814_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='order',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='order2',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)]),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='type',
            field=models.CharField(blank=True, choices=[('1', 'Select...'), ('2', 'string'), ('3', 'int'), ('4', 'bool'), ('5', 'list'), ('6', 'float'), ('7', 'tuple')], default='Select...', max_length=30),
        ),
        migrations.AlterField(
            model_name='scheme',
            name='type2',
            field=models.CharField(blank=True, choices=[('1', 'Select...'), ('2', 'string'), ('3', 'int'), ('4', 'bool'), ('5', 'list'), ('6', 'float'), ('7', 'tuple')], default='Select...', max_length=30),
        ),
    ]
