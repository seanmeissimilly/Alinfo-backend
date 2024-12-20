# Generated by Django 5.1.1 on 2024-09-27 16:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0013_alter_document_data_alter_historicaldocument_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'tex', 'odt', 'ods', 'odp'])]),
        ),
        migrations.AlterField(
            model_name='historicaldocument',
            name='data',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'txt', 'tex', 'odt', 'ods', 'odp'])]),
        ),
    ]
