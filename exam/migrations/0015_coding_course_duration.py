# Generated by Django 3.0.5 on 2023-05-19 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_course_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='coding_course',
            name='duration',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]