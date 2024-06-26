# Generated by Django 5.0.6 on 2024-06-15 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gasoline_tanks', models.PositiveIntegerField(default=0)),
                ('gasoline_nozzles', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('gas_tanks', models.PositiveIntegerField(default=0)),
                ('gas_nozzles', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('control_period', models.CharField(choices=[('start', 'ابتدا دوره'), ('end', 'انتهای دوره')], max_length=50)),
                ('product_type', models.CharField(choices=[('gasoline', 'بنزین'), ('diesel', 'نفتگاز'), ('both', 'هر دو')], max_length=50)),
                ('gasoline_initial_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('gasoline_received', models.PositiveIntegerField(blank=True, null=True)),
                ('gasoline_tank1_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('gasoline_tank2_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('gasoline_electronic_sales', models.PositiveIntegerField(blank=True, null=True)),
                ('gas_initial_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('gas_received', models.PositiveIntegerField(blank=True, null=True)),
                ('gas_tank1_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('gas_tank2_stock', models.PositiveIntegerField(blank=True, null=True)),
                ('diesel_electronic_sales', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GasNozzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nozzle_number', models.PositiveIntegerField()),
                ('totalizer_start', models.PositiveIntegerField()),
                ('totalizer_end', models.PositiveIntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gas_nozzles_details', to='stations.fuelstation')),
            ],
        ),
        migrations.CreateModel(
            name='GasolineNozzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nozzle_number', models.PositiveIntegerField()),
                ('totalizer_start', models.PositiveIntegerField()),
                ('totalizer_end', models.PositiveIntegerField()),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gasoline_nozzles_details', to='stations.fuelstation')),
            ],
        ),
    ]
