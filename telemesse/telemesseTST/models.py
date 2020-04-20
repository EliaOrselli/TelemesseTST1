# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# File creato da Elia Orselli v.0.1 18/04/2020

# TAG, per eventuale classificazione con elementi ricorrenti dei contenuti delle omelie
class tag(models.Model):
	tag = models.CharField(max_length=150)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.tag
	class Meta:
		verbose_name_plural = "tag"

# REGIONE ECCLESIASTICA: ripartizione delle diocesi in Italia
class regioni_ecclesiastiche(models.Model):
	denominazione = models.CharField(max_length=50)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.denominazione
	class Meta:
		verbose_name_plural = "regioni ecclesiastiche"
# TIPOLOGIA DIOCESI: tipo di sede per la classificazione delle diocesi
class tipo_diocesi(models.Model):
	denominazione = models.CharField(max_length=50)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.denominazione
	class Meta:
		verbose_name_plural = "Tipologie diocesi"
# DIOCESI: scheda identificativa della diocesi
class diocesi(models.Model):
	denominazione = models.CharField(max_length=250)	
	tipologia = models.ForeignKey(tipo_diocesi,blank=True)
	regione = models.ForeignKey(regioni_ecclesiastiche,null=True)
	vescovo = models.ForeignKey('persone', blank=True, null=True)
	riferimenti_decreti = models.TextField(blank=True)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return '%s - %s' % (self.regione, self.denominazione)
	class Meta:
		verbose_name_plural = "Diocesi"

# TIPOLOGIA CHIESA: tabella per identificare tipo chiese
class tipo_chiesa(models.Model):
	tipologia = models.CharField(max_length=50)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return self.tipologia
	class Meta:
		verbose_name_plural = "Tipologie chiese"

# CHIESE: Identificazione delle chiese, comunità o parrocchie che organizzano celebrazioni.
# possibilità di associare link alle pagine social per una più rapida verifica di nuove celebrazioni pubblicate
class chiese(models.Model):
	denominazione = models.CharField(max_length=250)	
	diocesi = models.ForeignKey(diocesi)
	tipologia = models.ForeignKey(tipo_chiesa)
	luogo_e_indirizzo = models.CharField(max_length=600, blank=True, help_text="Indicare nella forma Città, indirizzo (laddove possibile)")
	persone_collegate = models.ManyToManyField('persone', blank=True, help_text="Si possono selezionare più voci")
	facebook = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto alla pagina dedicata ai video")
	youtube = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto al canale della chiesa")
	sito_web = models.URLField(max_length=1000, blank=True, help_text="Inserire il link della sezione dedicata ai video")
	altro_1 = models.URLField(max_length=1000, blank=True, help_text="Inserire un link correlato alla chiesa")
	altro_2 = models.URLField(max_length=1000, blank=True, help_text="Inserire un link correlato alla chiesa")	
	riferimenti_decreti = models.TextField(blank=True)
	note = models.TextField(blank=True)
	def __unicode__(self):
		return '%s - %s' % (self.diocesi, self.denominazione)
	class Meta:
		verbose_name_plural = "chiese"

# PERSONE: Anagrafiche delle persone schedate da associare a record "diocesi", "chiese" o "celebrazione"
class persone(models.Model):
	nome = models.CharField(max_length=100)
	cognome = models.CharField(max_length=100)	
	RUOLO_CHOICES = (
		('Vescovo diocesano', 'Vescovo diocesano'),
		('Vescovo titolare', 'Vescovo titolare'),
		('Sacerdote parroco', 'Sacerdote parroco'),
		('Sacerdote', 'Sacerdote'),
		('Diacono', 'Diacono'),
		('Laico', 'Laico'),
		('Altro', 'Altro'),
	)
	ruolo = models.CharField(max_length=30, choices=RUOLO_CHOICES, default='Sacerdote parroco')
	note = models.TextField(blank=True)
	def __unicode__(self):
		return '%s %s - %s' % (self.cognome, self.nome, self.ruolo)
	class Meta:
		verbose_name_plural = "Persone"

# CELEBRAZIONE: Scheda della singola celebrazione. I dati proposti sono di ampio spettro, per permettere un approfondimento della schedatura e la realizzazione di statistiche più avanzate.
class celebrazione(models.Model):
	
	# Dati principali	
	
	data = models.DateField('data')
	orario = models.TimeField(auto_now=False,auto_now_add=False, help_text="Scrivere nella forma hh:mm:ss - es. 11:00:00")	
	liturgia_celebrata = models.CharField(max_length=200,blank=True, help_text="Ove siano possibili più schemi di letture. Es 'Pasqua giorno' o 'Pasqua vespertina'")
	predicatore = models.ForeignKey(persone, blank=True)
	luogo = models.ForeignKey(chiese)

	# Estremi dell'omelia

	omelia_file = models.FileField(upload_to='omelie/', blank=True, help_text="Consente il caricamento sul server di qualunque tipo di file")
	timecode_inizio_omelia = models.TimeField(auto_now=False,auto_now_add=False,blank=True, help_text="Scrivere nella forma hh:mm:ss - es 00:15:00", null=True)
	timecode_fine_omelia = models.TimeField(auto_now=False,auto_now_add=False,blank=True, help_text="Scrivere nella forma hh:mm:ss - es 00:20:00", null=True)
	facebook = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto al video")
	youtube = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto al video")
	sito_web = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto al video")
	altro_1 = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto al video")
	altro_2 = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto al video")	

	# Trascrizione e note

	trascrizione_omelia = models.TextField(blank=True)
	trascrizione_file = models.FileField(upload_to='omelie/trascrizioni/', blank=True, help_text="Consente il caricamento sul server di qualunque tipo di file contenente la trascrizione")
	link_trascrizione = models.URLField(max_length=1000, blank=True, help_text="Inserire il link diretto alla trascrizione del testo, se pubblicata")
	tag_cloud = models.ManyToManyField(tag, blank = True)
	note = models.TextField(blank=True)
	
	# Dati per statistiche aggiuntive	

	Persone_presenti = models.IntegerField(blank=True, null=True)
	LUOGOCEL_CHOICES = (
		('Altare maggiore', 'Altare maggiore'),
		('Altare secondario', 'Altare secondario'),
		('Altro locale', 'Altro locale'),
		('Spazio aperto', 'Spazio aperto'),
		('Altro', 'Altro'),
	)
	luogo_celebrazione = models.CharField(max_length=30, choices=LUOGOCEL_CHOICES, blank=True)
	PARAMENTI_CHOICES = (
		('Casula', 'Casula'),
		('Stola', 'Stola'),
		('Pianeta', 'Pianeta'),
		('Piviale', 'Piviale'),
		('Altro', 'Altro'),
	)
	paramenti = models.CharField(max_length=30, choices=PARAMENTI_CHOICES, blank=True)
	DIREZIONE_CHOICES = (
		('Verso il popolo', 'Verso il popolo'),
		('Altare a muro', 'Altare a muro'),
		('Altro', 'Altro'),
	)
	direzione_celebrazione = models.CharField(max_length=30, choices=DIREZIONE_CHOICES, blank=True)	
	CANTO_CHOICES = (
		('Corale', 'Corale'),
		('Solista', 'Solista'),
		('Registrazione', 'Registrazione'),
		('Nessun canto', 'Nessun canto'),
		('Altro', 'Altro'),
	)
	animazione = models.CharField(max_length=30, choices=CANTO_CHOICES, blank=True)
	def __unicode__(self):
		return '%s - %s %s' % (self.luogo, self.data, self.orario)
	class Meta:
		verbose_name_plural = "celebrazioni"

