# Generated by Django 3.2 on 2022-12-13 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth0', '0005_myuser_ep'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ('-date_joined',)},
        ),
    ]
