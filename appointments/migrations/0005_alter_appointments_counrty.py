# Generated by Django 3.2.8 on 2022-01-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20220128_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='counrty',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
