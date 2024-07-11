# Generated by Django 5.0.6 on 2024-07-11 07:42

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apm_categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ASHPenserEarnings',
            fields=[
                ('earn_data', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('payer', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('ashpenser_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apm_categories.ashpensercategories')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apm_categories.ashpenserpaymentmethod')),
            ],
            options={
                'verbose_name_plural': 'EarningsData',
                'db_table': 'income_earnings',
                'ordering': ('date', 'category', 'payer', 'payment_method'),
            },
        ),
    ]
