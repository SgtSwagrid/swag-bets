# Generated by Django 2.2.6 on 2019-10-26 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('markets', '0022_auto_20191026_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bidder',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, help_text='The user who placed the order.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='affirmative',
            field=models.BooleanField(help_text='Whether the order is for the negative or affirmative.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(help_text='The price the user is willing to pay for the order.'),
        ),
        migrations.AlterField(
            model_name='order',
            name='proposition',
            field=models.ForeignKey(help_text='The proposition on which the order is placed.', on_delete=django.db.models.deletion.CASCADE, to='markets.Proposition'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(help_text='The number of tokens the user wants to purchase.'),
        ),
        migrations.AlterField(
            model_name='proposition',
            name='active',
            field=models.BooleanField(help_text='Whether this proposition is enabled and unresolved.'),
        ),
        migrations.AlterField(
            model_name='proposition',
            name='resolve_date',
            field=models.DateField(help_text='The date on which this proposition will resolve.'),
        ),
    ]
