# Generated by Django 3.0.8 on 2020-08-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_picture_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='deviceId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
