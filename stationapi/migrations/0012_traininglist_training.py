# Generated by Django 4.2.5 on 2024-02-19 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stationapi', '0011_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='training_videos/')),
                ('video_duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationapi.user')),
                ('training_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stationapi.traininglist')),
            ],
        ),
    ]