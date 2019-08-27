# Generated by Django 2.0 on 2019-08-27 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Country', '0001_initial'),
    ]

    operations = [
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
