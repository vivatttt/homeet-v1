# Generated by Django 4.2.7 on 2023-11-05 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='bday',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='course',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='faculty',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='op',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='step',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='work',
        ),
    ]
