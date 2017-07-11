# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doit', '0002_auto_20170711_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doit.Tasks', verbose_name='Görev')),
            ],
        ),
    ]