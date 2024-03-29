# Generated by Django 2.0 on 2019-08-28 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=100)),
                ('country_info', models.TextField()),
                ('country_info1', models.TextField()),
                ('country_info2', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=50)),
                ('migrant_num', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=1996)),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Country.Country')),
            ],
        ),
    ]
