# Generated by Django 3.2.8 on 2021-11-14 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0019_auto_20211114_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotterContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=1000, null=True)),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
        ),
    ]
