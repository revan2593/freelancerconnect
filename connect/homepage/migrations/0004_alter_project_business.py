# Generated by Django 5.1.1 on 2024-11-01 09:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.business1'),
        ),
    ]
