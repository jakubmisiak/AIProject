# Generated by Django 3.1.4 on 2021-05-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_auto_20210519_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
