# Generated by Django 3.1.3 on 2020-12-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_mail',
            name='message',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user_mail',
            name='subject',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
