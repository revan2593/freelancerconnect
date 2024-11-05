# Generated by Django 5.1.1 on 2024-11-05 06:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_alter_business1_photo_alter_freelancer_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ratingsystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('review', models.TextField()),
                ('Freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.freelancer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.assignedproject')),
            ],
        ),
    ]