# Generated by Django 3.1.4 on 2020-12-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20201211_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(default='', upload_to='webapp/static/'),
        ),
    ]
