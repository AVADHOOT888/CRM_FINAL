# Generated by Django 3.1.2 on 2021-09-09 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210905_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='account11.png', null=True, upload_to=''),
        ),
    ]
