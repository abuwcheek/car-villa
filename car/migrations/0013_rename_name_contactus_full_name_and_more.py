# Generated by Django 5.1.2 on 2024-12-23 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_about_twitter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='number',
            new_name='telephone',
        ),
    ]