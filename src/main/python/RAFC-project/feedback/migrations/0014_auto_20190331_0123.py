# Generated by Django 2.1.7 on 2019-03-31 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0013_auto_20190331_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]
