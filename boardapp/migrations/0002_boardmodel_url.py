# Generated by Django 2.2.1 on 2019-05-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='url',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
