# Generated by Django 3.2.16 on 2022-11-12 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranges', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolls', models.CharField(max_length=20)),
                ('roll_width', models.CharField(max_length=2)),
                ('roll_size', models.DecimalField(decimal_places=2, max_digits=4)),
                ('location', models.CharField(max_length=3)),
                ('ranges', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Range', to='CUTS.range')),
            ],
        ),
        migrations.AddField(
            model_name='range',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Supplier', to='CUTS.supplier'),
        ),
        migrations.CreateModel(
            name='Cut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cut', models.DateTimeField(auto_created=True, default='')),
                ('invoice', models.CharField(max_length=10)),
                ('cut_size', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cuts', models.BooleanField(default=False)),
                ('rolls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Roll', to='CUTS.roll')),
            ],
        ),
    ]
