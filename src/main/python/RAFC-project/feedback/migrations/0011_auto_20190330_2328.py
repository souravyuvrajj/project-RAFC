# Generated by Django 2.1.7 on 2019-03-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0010_attendance_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='p_A',
            field=models.CharField(max_length=200),
        ),
    ]