# Generated by Django 5.0.7 on 2024-08-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_alter_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
