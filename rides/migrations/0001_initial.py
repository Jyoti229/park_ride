# Generated by Django 5.2.1 on 2025-07-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ride_type', models.CharField(choices=[('cab', 'Cab'), ('shuttle', 'Shuttle'), ('e_rickshaw', 'E-Rickshaw')], max_length=20)),
                ('pickup_point', models.CharField(max_length=100)),
                ('drop_point', models.CharField(max_length=100)),
                ('schedule_time', models.DateTimeField()),
                ('is_shared', models.BooleanField(default=False)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]
