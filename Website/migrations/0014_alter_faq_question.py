# Generated by Django 3.2.8 on 2021-11-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0013_smilesection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]