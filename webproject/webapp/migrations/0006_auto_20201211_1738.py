# Generated by Django 3.1.4 on 2020-12-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20201211_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default='', upload_to='media/'),
        ),
    ]
