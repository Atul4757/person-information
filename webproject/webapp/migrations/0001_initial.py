# Generated by Django 3.1.4 on 2020-12-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('registerno', models.IntegerField(max_length=50, null=True)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('sername', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
