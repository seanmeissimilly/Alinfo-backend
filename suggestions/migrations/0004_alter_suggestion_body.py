# Generated by Django 5.0.6 on 2024-07-19 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0003_alter_suggestion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestion',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]
