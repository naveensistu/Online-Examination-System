# Generated by Django 3.0.5 on 2023-05-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_auto_20230515_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='codearea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_area', models.CharField(max_length=1000)),
                ('input_area', models.CharField(max_length=1000)),
                ('output', models.CharField(max_length=1000)),
            ],
        ),
    ]