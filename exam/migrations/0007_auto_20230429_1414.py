# Generated by Django 3.0.5 on 2023-04-29 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_capturedimage'),
        ('exam', '0006_coding_course_coding_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coding_question',
            old_name='answer',
            new_name='coding_answer',
        ),
        migrations.RenameField(
            model_name='coding_question',
            old_name='course',
            new_name='coding_course',
        ),
        migrations.RenameField(
            model_name='coding_question',
            old_name='marks',
            new_name='coding_marks',
        ),
        migrations.RenameField(
            model_name='coding_question',
            old_name='question',
            new_name='coding_question',
        ),
        migrations.RemoveField(
            model_name='coding_question',
            name='option',
        ),
        migrations.CreateModel(
            name='coding_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.coding_course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
