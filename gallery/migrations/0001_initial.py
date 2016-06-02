# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('album_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image', models.FileField(upload_to='uploads/', blank=True)),
                ('name_text', models.CharField(max_length=20)),
                ('album', models.ForeignKey(to='gallery.Album')),
            ],
        ),
    ]
