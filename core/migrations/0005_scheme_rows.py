# Generated by Django 3.2.6 on 2021-08-14 18:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210814_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheme',
            name='rows',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
