# Generated by Django 3.1.7 on 2021-03-15 04:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='run_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
