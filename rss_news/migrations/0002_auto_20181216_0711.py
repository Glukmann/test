# Generated by Django 2.1.4 on 2018-12-16 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
