# Generated by Django 5.1.1 on 2024-10-07 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_job_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='billed_amount',
            field=models.CharField(default='0.0', max_length=200),
        ),
    ]
