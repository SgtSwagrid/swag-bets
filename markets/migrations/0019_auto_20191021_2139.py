# Generated by Django 2.2.6 on 2019-10-21 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0018_auto_20191021_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='balance',
            options={'ordering': ['quantity', 'user', 'proposition']},
        ),
    ]
