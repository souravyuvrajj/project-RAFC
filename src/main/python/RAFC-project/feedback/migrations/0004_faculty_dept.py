# Generated by Django 2.1.7 on 2019-03-04 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_student_dept'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='dept',
            field=models.CharField(default='CSE', max_length=200),
            preserve_default=False,
        ),
    ]
