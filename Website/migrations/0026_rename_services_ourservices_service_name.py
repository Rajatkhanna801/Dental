# Generated by Django 3.2.8 on 2021-12-13 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0025_ourservices_servicedashboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ourservices',
            old_name='services',
            new_name='service_name',
        ),
    ]
