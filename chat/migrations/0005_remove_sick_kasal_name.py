# Generated by Django 3.2.6 on 2024-02-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_delete_huruj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sick',
            name='kasal_name',
        ),
    ]
