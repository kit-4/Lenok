# Generated by Django 3.0.8 on 2020-08-29 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_customer_deviceid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_order',
        ),
    ]
