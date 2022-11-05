# Generated by Django 3.2.16 on 2022-11-05 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CUTS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.CharField(max_length=10)),
                ('cut_size', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cut', models.BooleanField(default=False)),
                ('rolls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Roll', to='CUTS.roll')),
            ],
        ),
    ]
