# Generated by Django 3.0.6 on 2020-06-05 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20200604_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='title',
            new_name='question',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='question',
        ),
    ]
