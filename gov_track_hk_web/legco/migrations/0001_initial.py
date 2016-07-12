# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=512)),
                ('name_ch', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Council',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=512)),
                ('name_ch', models.CharField(max_length=512)),
                ('start_year', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=512)),
                ('name_ch', models.CharField(max_length=512)),
                ('image', models.CharField(blank=True, default=None, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndividualVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[(b'YES', b'Yes'), (b'NO', b'No'), (b'ABSENT', b'Absent'), (b'ABSTAIN', b'Abstain')], default=b'NO', max_length=64)),
                ('individual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legco.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meeting_type', models.CharField(default=None, max_length=1024)),
                ('key', models.CharField(blank=True, default=b'no-key', max_length=255, null=True, unique=True)),
                ('source_url', models.CharField(max_length=2048, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=512)),
                ('name_ch', models.CharField(max_length=512)),
                ('mover_type', models.CharField(max_length=512)),
                ('mover_ch', models.CharField(default=None, max_length=512)),
                ('mover_en', models.CharField(default=None, max_length=512)),
                ('mover_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legco.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=2048)),
                ('key', models.CharField(blank=True, default=b'no-key', max_length=255, null=True, unique=True)),
                ('title', models.CharField(max_length=2048)),
                ('text', models.TextField(default=b'', max_length=33554432)),
                ('image', models.TextField(blank=True, default=None, max_length=33554432, null=True)),
                ('source', models.CharField(max_length=256)),
                ('individuals', models.ManyToManyField(to='legco.Individual')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=512)),
                ('name_ch', models.CharField(max_length=512)),
                ('image', models.CharField(blank=True, default=None, max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('vote_number', models.IntegerField()),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legco.Meeting')),
                ('motion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legco.Motion')),
            ],
        ),
        migrations.CreateModel(
            name='VoteSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_type', models.CharField(choices=[(b'FUNC', b'Functional'), (b'OVER', b'Overall'), (b'GEOG', b'GEOG')], max_length=64)),
                ('present_count', models.IntegerField(default=0)),
                ('vote_count', models.IntegerField(default=0)),
                ('yes_count', models.IntegerField(default=0)),
                ('no_count', models.IntegerField(default=0)),
                ('abstain_count', models.IntegerField(default=0)),
                ('result', models.CharField(max_length=512)),
                ('vote', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='legco.Vote')),
            ],
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='parties',
            field=models.ManyToManyField(to='legco.Party'),
        ),
        migrations.AddField(
            model_name='individualvote',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legco.Vote'),
        ),
        migrations.AddField(
            model_name='individual',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legco.Party'),
        ),
    ]
