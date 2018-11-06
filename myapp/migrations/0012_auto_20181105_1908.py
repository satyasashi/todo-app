# Generated by Django 2.1.2 on 2018-11-05 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181105_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notify_before',
            field=models.IntegerField(default=1, help_text="Mention number of hours before 'Due-Date' you want to get notified. Default is 1 hour", null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(23)]),
        ),
    ]