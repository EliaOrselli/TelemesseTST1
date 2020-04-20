# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-19 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemesseTST', '0007_auto_20200419_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebrazione',
            name='timecode_omelia',
        ),
        migrations.AddField(
            model_name='celebrazione',
            name='timecode_fine_omelia',
            field=models.TimeField(blank=True, help_text='Scrivere nella forma hh:mm:ss - es 00:20:00', null=True),
        ),
        migrations.AddField(
            model_name='celebrazione',
            name='timecode_inizio_omelia',
            field=models.TimeField(blank=True, help_text='Scrivere nella forma hh:mm:ss - es 00:15:00', null=True),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='Persone_presenti',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='altro_1',
            field=models.URLField(blank=True, help_text='Inserire il link diretto al video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='altro_2',
            field=models.URLField(blank=True, help_text='Inserire il link diretto al video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='facebook',
            field=models.URLField(blank=True, help_text='Inserire il link diretto al video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='liturgia_celebrata',
            field=models.CharField(blank=True, help_text="Ove siano possibili pi\xf9 schemi di letture. Es 'Pasqua giorno' o 'Pasqua vespertina'", max_length=200),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='omelia_file',
            field=models.FileField(blank=True, help_text='Consente il caricamento sul server di qualunque tipo di file', upload_to='omelie/'),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='orario',
            field=models.TimeField(help_text='Scrivere nella forma hh:mm:ss - es. 11:00:00'),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='sito_web',
            field=models.URLField(blank=True, help_text='Inserire il link diretto al video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='celebrazione',
            name='youtube',
            field=models.URLField(blank=True, help_text='Inserire il link diretto al video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='altro_1',
            field=models.URLField(blank=True, help_text='Inserire un link correlato alla chiesa', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='altro_2',
            field=models.URLField(blank=True, help_text='Inserire un link correlato alla chiesa', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='facebook',
            field=models.URLField(blank=True, help_text='Inserire il link diretto alla pagina dedicata ai video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='luogo_e_indirizzo',
            field=models.CharField(blank=True, help_text='Indicare nella forma Citt\xe0, indirizzo (laddove possibile)', max_length=600),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='persone_collegate',
            field=models.ManyToManyField(help_text='Si possono selezionare pi\xf9 voci', to='telemesseTST.persone'),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='sito_web',
            field=models.URLField(blank=True, help_text='Inserire il link della sezione dedicata ai video', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chiese',
            name='youtube',
            field=models.URLField(blank=True, help_text='Inserire il link diretto al canale della chiesa', max_length=1000),
        ),
    ]
