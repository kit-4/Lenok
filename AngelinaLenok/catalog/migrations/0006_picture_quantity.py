# Generated by Django 3.0.8 on 2020-08-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
