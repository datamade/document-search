# Generated by Django 2.2.8 on 2019-12-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docsearch', '0005_controlmonumentmap_plss'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeepTunnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('source_file', models.FileField(upload_to='DEEP_PARCEL_SURPLUS')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]