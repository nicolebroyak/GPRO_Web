# Generated by Django 3.2.7 on 2021-11-19 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Sezon',
                'verbose_name_plural': 'Sezony',
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nazwa toru')),
            ],
            options={
                'verbose_name': 'Tor',
                'verbose_name_plural': 'Tory',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField()),
                ('date', models.DateField(verbose_name='Data wyścigu')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gpro.season', verbose_name='Sezon')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gpro.track', verbose_name='Tor')),
            ],
            options={
                'verbose_name': 'Wyścig',
                'verbose_name_plural': 'Wyścigi',
            },
        ),
    ]