# Generated by Django 5.1.1 on 2024-11-05 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_alter_ratingsystem_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingsystem',
            old_name='Freelancer',
            new_name='freelancer',
        ),
    ]
