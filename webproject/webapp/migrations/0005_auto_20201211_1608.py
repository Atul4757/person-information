# Generated by Django 3.1.4 on 2020-12-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20201211_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default='', upload_to='webapp/upload_data/'),
        ),
    ]