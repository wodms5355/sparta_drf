# Generated by Django 4.2 on 2024-05-01 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poduct',
            old_name='login_state',
            new_name='login_status',
        ),
    ]