# Generated by Django 3.2.8 on 2022-01-21 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20220121_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_date',
            field=models.DateField(),
        ),
    ]