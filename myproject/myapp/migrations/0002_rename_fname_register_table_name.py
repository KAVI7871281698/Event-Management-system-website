# Generated by Django 5.1.7 on 2025-03-16 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_table',
            old_name='fname',
            new_name='name',
        ),
    ]
