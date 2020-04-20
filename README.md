# TelemesseTST1

Ipotesi di applicazione Django per la schedatura di contenuti video e parziale trascrizione dell'audio sviluppata a partire dalla ricerca sulle omelie nelle celebrazioni trasmesse attraverso le reti sociali in ragione dell'epidemia COVID-19 in Italia.
L'applicazione utilizza al momento il solo plugin ImportExport https://django-import-export.readthedocs.io/en/latest/ per semplificare il caricamento dei dati iniziali e l'utilizzo promiscuo di fogli excel per la prima fase di raccolta informazioni.


## Organizzazione della struttura

### Tabelle principali
#### Persone
Raccoglie i dati identificativi delle persone:
- nome
- cognome
- ruolo (scelta da lista predefinita)
- note

##### Modifiche da prevedere:
1. uniformare a ISAAR(CPF)

#### Chiese
Raccoglie i luoghi delle celebrazioni e i riferimenti alle pagine social:
- denominazione
- diocesi di appartenenza (da elenco)
- tipologia (da elenco)
- luogo e indirizzo
- persone collegate (da elenco)
- facebook
- youtube
- sito web
- altro link 1
- altro link 2
- riferimenti a decreti specifici in materia di COVID-19
- note

##### Modifiche da prevedere:
1. uniformare a ISAAR(CPF)
2. georeferenziare i luoghi  / adeguare il campo a possibili sviluppi cartografici
3. inserire campo instagram

#### Celebrazioni
Identifica le singole celebrazioni oggetto di studio:
- Dati principali
  - data
  - orario
  - liturgia celebrata (in caso di solennità con più schemi di letture)
  - predicatore (da elenco)
  - luogo
- Estremi dell'omelia
  - file dell'omelia
  - timecode inizio
  - timecode fine
  - link facebook
  - link youtube
  - link sito web
  - altro link 1
  - altro link 2
- Trascrizione e note
  - trascrizione del contenuto
  - file contenente la trascrizione
  - link a trascrizione pubblicata su siti
  - tag cloud (da elenco)
  - note
- Dati per statistiche aggiuntive
  - numero persone presenti
  - luogo della celebrazione (scelta da elenco predefinito)
  - paramenti utilizzati (scelta da elenco predefinito)
  - direzione della celebrazione (scelta da elenco predefinito)
  - animazione (scelta da elenco predefinito)

##### Modifiche da Prevedere
1. Uniformare a ISAD(G)
2. Inserire sezione di registrazione dei metadata relativi al video. Es. modalità di ripresa; tipologia (diretta o registrazione); inquadratura...

### Tabelle di servizio
#### TAG
Contiene i TAG per la schedatura delle celebrazioni
- tag
- note

#### Regione ecclesiastica
Contiene le denominazioni delle regioni ecclesiastiche in cui è suddivisa l'Italia
- denominazione
- note

#### Tipologia diocesi
Contiene le denominazioni delle tipologie delle diocesi
- denominazione
- note

#### Diocesi
Contiene l'elenco delle diocesi d'Italia tratto da wikipedia e verificato con i dati del portale CEI
- denominazione
- tipologia (da elenco)
- regione ecclesiastica (da elenco)
- vescovo (da elenco)
- riferimenti a decreti diocesani sul COVID-19
- note

#### Tipologia chiesa
Contiene l'elenco delle tipologie di chiese:
- tipologia
- note
