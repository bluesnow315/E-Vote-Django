# Generated by Django 3.1.8 on 2021-07-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='agenda',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]