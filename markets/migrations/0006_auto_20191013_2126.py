# Generated by Django 2.2.4 on 2019-10-13 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0005_auto_20191012_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=10)),
                ('resolved', models.BooleanField()),
                ('resolves_on', models.DateField()),
                ('affirmative', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Commodities',
                'ordering': ['resolved', 'resolves_on', 'label'],
            },
        ),
        migrations.AlterModelOptions(
            name='balance',
            options={'ordering': ['user', 'proposition']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['proposition', 'time']},
        ),
        migrations.RemoveField(
            model_name='balance',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='resolution',
            name='commodity',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='commodity',
        ),
        migrations.DeleteModel(
            name='Commodity',
        ),
        migrations.AddField(
            model_name='balance',
            name='proposition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='markets.Proposition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='proposition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='markets.Proposition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resolution',
            name='proposition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='markets.Proposition'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='proposition',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='markets.Proposition'),
            preserve_default=False,
        ),
    ]