# Generated by Django 5.0.6 on 2024-07-05 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashpensers', '0003_rename_firstname_ashpensersprofile_ashpenser_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ashpensersprofile',
            old_name='ashpenser_firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='ashpensersprofile',
            old_name='ashpenser_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='ashpensersprofile',
            old_name='ashpenser_lastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='ashpensersprofile',
            old_name='ashpenser_mfa',
            new_name='mfa',
        ),
    ]