# Generated by Django 3.2.8 on 2021-10-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0006_dashboardcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardcontent',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
