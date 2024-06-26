# Generated by Django 5.0.6 on 2024-06-24 14:51

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_freeproduct_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='freeproduct',
            options={},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
