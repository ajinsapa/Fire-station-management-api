# Generated by Django 4.2.5 on 2024-02-19 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stationapi', '0013_alter_training_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='stationapi.employee'),
        ),
    ]
