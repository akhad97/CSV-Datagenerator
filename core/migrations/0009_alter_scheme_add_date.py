# Generated by Django 3.2.6 on 2021-08-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210806_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='add_date',
            field=models.DateField(null=True),
        ),
    ]
