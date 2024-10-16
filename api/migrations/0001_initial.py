# Generated by Django 5.1.1 on 2024-10-06 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(default='184064313115', max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('posted_time', models.DateField(default=datetime.date.today)),
                ('payment_verified', models.BooleanField(default=False)),
                ('total_spent', models.FloatField(default=0.0)),
                ('location', models.CharField(max_length=200)),
                ('rating', models.FloatField(null=True)),
                ('job_type', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('skills', models.JSONField(default=list)),
                ('proposals', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
