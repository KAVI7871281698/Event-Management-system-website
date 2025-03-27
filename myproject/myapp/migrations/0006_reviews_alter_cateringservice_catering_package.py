# Generated by Django 5.1.7 on 2025-03-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('reviews', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='cateringservice',
            name='catering_package',
            field=models.CharField(choices=[('Simple', 'Simple (6-8 item    s)'), ('Standerd', 'Standard (10-12 items)'), ('Premium', 'Premium (15-20 items)')], max_length=20),
        ),
    ]
