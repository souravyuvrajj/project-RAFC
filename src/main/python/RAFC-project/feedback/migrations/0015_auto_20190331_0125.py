# Generated by Django 2.1.7 on 2019-03-31 01:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0014_auto_20190331_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
