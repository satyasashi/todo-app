# Generated by Django 2.1.2 on 2018-10-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notify_me_before',
            field=models.IntegerField(default=1, help_text="Mention number of hours before 'Due-Date' you want to get notified. Default is 1 hour"),
        ),
    ]
