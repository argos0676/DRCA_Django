# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170928_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='d_requisito',
            field=models.ManyToManyField(blank=True, to='core.Disciplina'),
        ),
    ]
