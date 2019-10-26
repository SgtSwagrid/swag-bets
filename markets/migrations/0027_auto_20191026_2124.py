# Generated by Django 2.2.6 on 2019-10-26 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0026_auto_20191026_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resolution',
            name='proposition',
        ),
        migrations.RemoveField(
            model_name='resolution',
            name='user',
        ),
        migrations.AlterField(
            model_name='funds',
            name='value',
            field=models.DecimalField(decimal_places=2, help_text='Available funds ($AUD).', max_digits=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(help_text='The price the user is willing to pay per token (c).'),
        ),
        migrations.AlterField(
            model_name='stake',
            name='affirmative',
            field=models.BooleanField(help_text='Whether the stake is for the negative or affirmative.'),
        ),
        migrations.AlterField(
            model_name='stake',
            name='proposition',
            field=models.ForeignKey(help_text='The propostion in which the stake is held.', on_delete=django.db.models.deletion.CASCADE, to='markets.Proposition'),
        ),
        migrations.AlterField(
            model_name='stake',
            name='quantity',
            field=models.IntegerField(help_text='The amount of stake owned ($).'),
        ),
        migrations.AlterField(
            model_name='stake',
            name='user',
            field=models.ForeignKey(help_text='The owner of the stake.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.IntegerField(help_text='The affirmative price at which the tokens were traded (c).'),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='Resolution',
        ),
    ]