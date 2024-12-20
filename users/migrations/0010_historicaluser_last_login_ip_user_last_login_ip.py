# Generated by Django 5.1.1 on 2024-09-07 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_historicaluser'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='last_login_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login_ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
