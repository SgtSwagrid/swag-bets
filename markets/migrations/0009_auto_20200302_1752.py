# Generated by Django 3.0.3 on 2020-03-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0008_auto_20200302_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposition',
            name='resolves',
            field=models.DateTimeField(help_text='The time at which this proposition actually resolved.'),
        ),
    ]