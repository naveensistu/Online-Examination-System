# Generated by Django 3.0.5 on 2023-05-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_codearea'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
