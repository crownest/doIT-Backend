# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='celery_task_id',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='Celery Task Id'),
        ),
    ]
