# Generated by Django 2.1.7 on 2019-03-31 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0012_auto_20190330_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]