# Generated by Django 5.1.1 on 2024-10-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_rename_name_llmresponse_client_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llmresponse',
            name='client_name',
        ),
        migrations.AddField(
            model_name='llmresponse',
            name='client_names',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
