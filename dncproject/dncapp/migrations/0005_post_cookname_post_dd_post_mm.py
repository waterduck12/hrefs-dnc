# Generated by Django 4.0.2 on 2022-03-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dncapp', '0004_remove_post_cookname_remove_post_dd_remove_post_mm'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cookname',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='dd',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='mm',
            field=models.TextField(default=''),
        ),
    ]
