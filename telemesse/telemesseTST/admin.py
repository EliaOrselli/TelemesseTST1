# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import diocesi, chiese, persone, celebrazione, tipo_diocesi, tipo_chiesa, regioni_ecclesiastiche, tag
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#	MODULI DI IMPORT_EXPORT

	# DIOCESI
class diocesiResource(resources.ModelResource):
	
	class Meta:
		model = diocesi

	#CELEBRAZIONE
class celebrazioneResource(resources.ModelResource):
	
	class Meta:
		model = celebrazione

	#CHIESE
class chieseResource(resources.ModelResource):
	
	class Meta:
		model = chiese

	#PERSONE
class personeResource(resources.ModelResource):
	
	class Meta:
		model = persone

	#TAG
class tagResource(resources.ModelResource):
	
	class Meta:
		model = tag


# 	VISUALIZZAZIONE ADMIN

class chieseAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = chieseResource
	fieldsets = [
		('Dati essenziali', {'fields': ['denominazione', 'diocesi', 'tipologia']}),
		('Collegamenti social', {'fields': ['facebook', 'youtube', 'sito_web', 'altro_1', 'altro_2']}),
		('Dati aggiuntivi', {'fields': ['persone_collegate', 'luogo_e_indirizzo', 'riferimenti_decreti', 'note']}),
	]
	list_display = ('denominazione', 'diocesi', 'luogo_e_indirizzo')
	list_filter = ['diocesi']
	search_fields = ['denominazione','luogo_e_indirizzo']


class celebrazioneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = celebrazioneResource	
	fieldsets = [
		('Dati essenziali', {'fields': ['data', 'orario', 'predicatore', 'luogo', 'liturgia_celebrata']}),
		('Registrazione', {'fields': ['omelia_file','timecode_inizio_omelia', 'timecode_fine_omelia', 'facebook','youtube','sito_web','altro_1','altro_2']}),
		('Trascrizione', {'fields':['trascrizione_omelia','trascrizione_file','link_trascrizione']}),
		('Dati statistici', {'fields': ['Persone_presenti','luogo_celebrazione','paramenti','direzione_celebrazione','animazione']}),
		('Dati aggiuntivi', {'fields': ['tag_cloud','note']}),
	]
	list_display = ('luogo','data', 'orario', 'predicatore')


class diocesiAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = diocesiResource	
	list_display = ('denominazione', 'regione', 'tipologia')
	list_filter = ['regione', 'tipologia']
	search_fields = ['denominazione', 'regione', 'tipologia']


class personeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = personeResource
	list_display = ('cognome', 'nome', 'ruolo')
	list_filter = ['ruolo']
	search_fields = ['cognome', 'nome']

class tagAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = tagResource
	list_filter = ['tag']


# Models

admin.site.register(diocesi, diocesiAdmin)
admin.site.register(chiese, chieseAdmin)
admin.site.register(persone, personeAdmin)
admin.site.register(celebrazione, celebrazioneAdmin)
admin.site.register(tipo_diocesi)
admin.site.register(tipo_chiesa)
admin.site.register(regioni_ecclesiastiche)
admin.site.register(tag, tagAdmin)
