# Generated by Django 5.1.1 on 2024-10-06 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_list',
            name='posted_time',
            field=models.CharField(max_length=200),
        ),
    ]
