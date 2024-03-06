# Generated by Django 3.2.6 on 2024-02-28 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_sick_kasal_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hurujs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_times', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='chat.sick')),
            ],
        ),
    ]
