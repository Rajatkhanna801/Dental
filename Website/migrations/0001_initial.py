# Generated by Django 3.2.8 on 2021-10-24 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='pictures')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.SlugField(blank=True, null=True)),
                ('fb_link', models.SlugField(blank=True, null=True)),
                ('twitter_link', models.SlugField(blank=True, null=True)),
                ('youtube_link', models.SlugField(blank=True, null=True)),
                ('opening_time', models.TimeField(blank=True, null=True)),
                ('closing_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DashboardContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=1000, null=True)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('sort_by', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_by'],
            },
        ),
    ]
