# Generated by Django 2.1.2 on 2018-10-25 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20181025_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.date(2018, 10, 25), help_text='Date format yyyy-mm-dd'),
        ),
    ]
