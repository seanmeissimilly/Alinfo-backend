# Generated by Django 5.1.1 on 2024-10-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_captcha'),
    ]

    operations = [
        migrations.AddField(
            model_name='captcha',
            name='image_file',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]