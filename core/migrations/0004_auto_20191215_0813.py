# Generated by Django 2.0.13 on 2019-12-15 08:13

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191214_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_image_path),
        ),
    ]
