# Generated by Django 5.0.6 on 2024-07-05 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashpensers', '0005_ashpensersprofile_security_answer_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ashpensersprofile',
            options={'ordering': ('lastname', 'firstname'), 'verbose_name_plural': 'ASHPensersProfile'},
        ),
        migrations.AlterModelTable(
            name='ashpensersprofile',
            table='ashpensers_profiles',
        ),
    ]