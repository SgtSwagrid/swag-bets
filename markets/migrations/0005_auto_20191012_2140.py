# Generated by Django 2.2.4 on 2019-10-12 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0004_auto_20191012_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='result',
            new_name='affirmative',
        ),
    ]
