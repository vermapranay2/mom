# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mom2k17', '0010_auto_20161208_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='event',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('TME', 'Technical Model Exhibition'), ('IIP', 'Brainwave'), ('QUIZ', 'Quiz'), ('APP', 'Apps Corner'), ('Flash', 'Flash')], max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='momid',
            field=models.CharField(default='MOM2K17-000', max_length=15),
        ),
    ]
