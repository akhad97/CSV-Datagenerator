# Generated by Django 3.2.6 on 2021-08-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210807_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheme',
            name='upload',
            field=models.FileField(blank=True, upload_to='media/'),
        ),
    ]
