# Generated by Django 4.2.5 on 2024-02-15 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stationapi', '0004_remove_incident_assigned_units_incident_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Team_incident',
            new_name='Team_assign',
        ),
    ]