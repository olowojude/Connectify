# Generated by Django 5.1.4 on 2025-01-11 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_link_name_alter_link_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='avatar.png', upload_to='images/'),
        ),
    ]
