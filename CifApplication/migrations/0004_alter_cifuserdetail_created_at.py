# Generated by Django 5.0.2 on 2024-02-29 08:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CifApplication', '0003_alter_cifuserdetail_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cifuserdetail',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]