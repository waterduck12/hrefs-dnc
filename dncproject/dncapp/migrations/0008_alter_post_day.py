# Generated by Django 4.0.2 on 2022-03-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dncapp', '0007_rename_dd_post_day_remove_post_mm_remove_post_yyyy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='day',
            field=models.DateField(auto_now=True),
        ),
    ]
