# Generated by Django 3.1.2 on 2021-09-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210905_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/11.png', null=True, upload_to=''),
        ),
    ]
