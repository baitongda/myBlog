# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-02 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161031_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='blog_id',
            field=models.IntegerField(default=0),
        ),
    ]