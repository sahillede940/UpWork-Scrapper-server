# Generated by Django 5.1.1 on 2024-10-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_comment_client_feedback_comment_freelancer_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_on',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
