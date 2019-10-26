# Generated by Django 2.2.4 on 2019-10-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0008_auto_20191013_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['affirmative', '-price', 'remaining_quantity']},
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.IntegerField(),
        ),
    ]
