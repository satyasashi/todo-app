# Generated by Django 2.1.2 on 2018-10-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20181025_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(help_text='Date format yyyy-mm-dd'),
        ),
    ]
