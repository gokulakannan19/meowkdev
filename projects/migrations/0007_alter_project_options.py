# Generated by Django 3.2.8 on 2021-10-16 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20211016_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', '-created']},
        ),
    ]
