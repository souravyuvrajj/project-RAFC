# Generated by Django 2.1.7 on 2019-03-30 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0011_auto_20190330_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='p_A',
            new_name='P_A',
        ),
    ]
