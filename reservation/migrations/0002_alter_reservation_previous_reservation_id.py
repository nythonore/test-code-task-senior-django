# Generated by Django 4.0.3 on 2022-04-01 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='previous_reservation_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
