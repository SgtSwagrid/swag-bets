# Generated by Django 2.2.6 on 2019-10-21 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0012_auto_20191021_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funds',
            options={'ordering': (['user'],)},
        ),
    ]