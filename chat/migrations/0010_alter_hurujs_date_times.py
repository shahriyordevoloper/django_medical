# Generated by Django 5.0.3 on 2024-03-14 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_auto_20240311_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hurujs',
            name='date_times',
            field=models.DateTimeField(),
        ),
    ]