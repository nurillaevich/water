# Generated by Django 4.2.3 on 2024-06-21 13:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
