# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patiant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ehr1',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='ehr1',
            name='when',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='ehr1',
            name='why',
            field=models.TextField(verbose_name='Why did you come in today?'),
        ),
    ]
