# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import api.models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Name')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('phone', models.CharField(max_length=140, verbose_name=b'Phone')),
                ('image', models.ImageField(upload_to=api.models.imgUpload, verbose_name=b'Image')),
                ('owner', models.ForeignKey(related_name='ClientsOwned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Name')),
                ('money', models.FloatField(verbose_name=b'Money')),
                ('paymentType', models.CharField(max_length=3, verbose_name=b'Type', choices=[(b'int', b'Initial'), (b'fnl', b'Final'), (b'otr', b'Other')])),
                ('date', models.DateTimeField(verbose_name=b'Date completed')),
                ('dateAdded', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Added')),
                ('taxPercentage', models.DecimalField(verbose_name=b'Tax Percentage', max_digits=5, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('owner', models.ForeignKey(related_name='PaymentsOwned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Description')),
                ('image', models.ImageField(upload_to=api.models.imgUpload, verbose_name=b'Image')),
                ('status', models.CharField(default=b'pnd', max_length=3, verbose_name=b'Status', choices=[(b'pnd', b'Pending'), (b'pgr', b'Progress'), (b'tst', b'Testing'), (b'cls', b'Closed')])),
                ('client', models.ForeignKey(related_name='ProjectsClient', to='api.Client')),
                ('owner', models.ForeignKey(related_name='ProjectsOwned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140, verbose_name=b'Name')),
                ('status', models.BooleanField(default=False, verbose_name=b'Status')),
                ('date', models.DateTimeField(verbose_name=b'ToDo Date')),
                ('dateAdded', models.DateTimeField(auto_now_add=True, verbose_name=b'Date added')),
                ('owner', models.ForeignKey(related_name='TasksOwned', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(related_name='TaskProjects', to='api.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payment',
            name='project',
            field=models.ForeignKey(related_name='PaymentProjects', to='api.Project'),
            preserve_default=True,
        ),
    ]
