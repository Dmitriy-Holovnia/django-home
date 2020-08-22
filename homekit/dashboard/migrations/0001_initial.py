# Generated by Django 3.1 on 2020-08-12 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Комнаты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Значение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.place', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Температура',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Pressure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Значение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.place', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Давление',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Значение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.place', verbose_name='Комната')),
            ],
            options={
                'verbose_name': 'Влажность',
                'ordering': ['-created_at'],
            },
        ),
    ]
