# Generated by Django 5.0.6 on 2024-07-05 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apm_accounts', '0003_remove_ashpenser_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ashpenser',
            options={'ordering': ('username',), 'verbose_name_plural': 'ASHPenserAdmin'},
        ),
        migrations.AlterModelTable(
            name='ashpenser',
            table='ashpenser_admin',
        ),
    ]
