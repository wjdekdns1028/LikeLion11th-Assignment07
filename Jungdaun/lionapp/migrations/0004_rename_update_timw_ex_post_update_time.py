# Generated by Django 4.2.1 on 2023-05-22 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lionapp', '0003_ex_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ex_post',
            old_name='update_timw',
            new_name='update_time',
        ),
    ]
