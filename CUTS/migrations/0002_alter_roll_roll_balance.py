# Generated by Django 3.2.16 on 2022-11-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CUTS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roll',
            name='roll_balance',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
