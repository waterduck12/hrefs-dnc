# Generated by Django 4.0.2 on 2022-03-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dncapp', '0002_cook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yyyy', models.TextField()),
                ('mm', models.TextField()),
                ('dd', models.TextField()),
                ('cookname', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cook',
        ),
    ]
