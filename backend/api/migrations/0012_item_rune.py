# Generated by Django 3.1.2 on 2021-08-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20210829_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rune',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]