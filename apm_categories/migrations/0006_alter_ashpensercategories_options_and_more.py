# Generated by Django 5.0.6 on 2024-06-29 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apm_categories', '0005_alter_ashpensercategories_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ashpensercategories',
            options={'ordering': ('category_name',), 'verbose_name_plural': 'CategoriesData'},
        ),
        migrations.AlterModelOptions(
            name='ashpenserpaymentmethod',
            options={'ordering': ('paymethod_name',), 'verbose_name_plural': 'PaymentMethodsData'},
        ),
        migrations.AlterModelOptions(
            name='ashpensersubcategories',
            options={'ordering': ('subcategory_name',), 'verbose_name_plural': 'SubCategoriesData'},
        ),
        migrations.RemoveField(
            model_name='ashpensercategories',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='ashpenserpaymentmethod',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='ashpensersubcategories',
            name='date_created',
        ),
    ]
