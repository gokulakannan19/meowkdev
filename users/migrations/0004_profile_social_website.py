# Generated by Django 3.2.8 on 2021-10-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211009_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
