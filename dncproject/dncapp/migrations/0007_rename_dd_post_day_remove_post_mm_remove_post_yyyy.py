# Generated by Django 4.0.2 on 2022-03-25 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dncapp', '0006_alter_post_yyyy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='dd',
            new_name='day',
        ),
        migrations.RemoveField(
            model_name='post',
            name='mm',
        ),
        migrations.RemoveField(
            model_name='post',
            name='yyyy',
        ),
    ]
