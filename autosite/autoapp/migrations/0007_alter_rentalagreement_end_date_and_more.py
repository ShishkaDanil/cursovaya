# Generated by Django 4.1.7 on 2023-05-05 01:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoapp', '0006_alter_rentalagreement_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalagreement',
            name='end_date',
            field=models.TextField(validators=[django.core.validators.RegexValidator(message='Invalid date format. DD.MM.YYYY is required.', regex='^\\d{2}\\.\\d{2}\\.\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='rentalagreement',
            name='start_date',
            field=models.TextField(validators=[django.core.validators.RegexValidator(message='Invalid date format. DD.MM.YYYY is required.', regex='^\\d{2}\\.\\d{2}\\.\\d{4}$')]),
        ),
    ]
