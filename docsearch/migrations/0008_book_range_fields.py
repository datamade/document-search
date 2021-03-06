# Generated by Django 2.2.8 on 2019-12-20 21:00

import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docsearch', '0007_easement_license_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='range',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='section',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='township',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(blank=True, max_length=255, null=True),
        ),
    ]
