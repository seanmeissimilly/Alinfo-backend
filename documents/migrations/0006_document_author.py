# Generated by Django 5.0.6 on 2024-07-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_rename_name_document_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='author',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]