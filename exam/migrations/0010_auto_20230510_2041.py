# Generated by Django 3.0.5 on 2023-05-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_coding_result_coding_view'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coding_view',
            old_name='student_code',
            new_name='coding_area',
        ),
        migrations.RenameField(
            model_name='coding_view',
            old_name='student_output',
            new_name='output',
        ),
    ]
