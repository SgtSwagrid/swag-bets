# Generated by Django 3.0.3 on 2020-03-02 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0011_auto_20200302_1818'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proposition',
            options={'ordering': ['-active', 'resolves', 'code']},
        ),
        migrations.AddField(
            model_name='proposition',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 2, 18, 19, 7, 117019), help_text='The time at which this proposition was created.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proposition',
            name='resolves',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 2, 18, 19, 13, 3464), help_text='The time at which this proposition resolved/will resolve.'),
            preserve_default=False,
        ),
    ]
