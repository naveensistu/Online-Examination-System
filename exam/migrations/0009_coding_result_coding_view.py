# Generated by Django 3.0.5 on 2023-05-09 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_capturedimage'),
        ('exam', '0008_delete_coding_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='coding_view',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_output', models.CharField(max_length=1000)),
                ('student_code', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='coding_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coding_marks', models.PositiveIntegerField()),
                ('coding_date', models.DateTimeField(auto_now=True)),
                ('coding_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]
