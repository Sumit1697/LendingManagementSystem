# Generated by Django 5.0.2 on 2024-02-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CifApplication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cifuserdetail',
            name='updated_at',
            field=models.DateTimeField(default='null'),
        ),
    ]
