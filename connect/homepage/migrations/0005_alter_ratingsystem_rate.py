# Generated by Django 5.1.1 on 2024-11-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_ratingsystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingsystem',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
