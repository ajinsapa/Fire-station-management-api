# Generated by Django 4.2.5 on 2024-02-15 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stationapi', '0003_equipment_vehicle_team_incident_incident_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='assigned_units',
        ),
        migrations.AddField(
            model_name='incident',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='severity',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team_incident',
            name='incident',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stationapi.incident'),
        ),
    ]
