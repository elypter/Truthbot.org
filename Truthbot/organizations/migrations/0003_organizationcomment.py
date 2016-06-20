# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-08 20:34
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_organization_wiki_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tone', models.CharField(choices=[('P', 'Positive'), ('N', 'Neutral'), ('C', 'Critical')], default='N', max_length=1)),
                ('text', models.CharField(max_length=300)),
                ('sources', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=2083), blank=True, size=None)),
            ],
        ),
    ]