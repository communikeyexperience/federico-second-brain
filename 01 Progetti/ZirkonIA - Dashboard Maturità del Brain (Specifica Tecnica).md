---
data: "2026-08-08"
tipo: progetto
stato: attivo
priorita: alta
cliente: ""
percorso_file: "D:\_CLAUDE"
tags: [zirkonia, dashboard, sviluppo, specifica-tecnica, metriche]
summary: "Specifica tecnica per gli sviluppatori dell'app ZirkonIA (repo STUDIO): dati da esporre in dashboard (parole, nodi, collegamenti, aree), logica di calcolo dello stadio cosmico (Nebula/Nucleus/Comet/Planet/Galaxy) con soglie di parole, formula del ritmo medio (parole/minuti al giorno), logica del ciclo annuale Galaxy, un pannello task/to-do quotidiano (manuale + suggerito dal brain), schema dati proposto, e brief per l'emblema visivo che cambia forma con lo stadio."
---

# ZirkonIA — Dashboard Maturità del Brain (specifica tecnica)

> Nota per chi implementa la dashboard nel repo `STUDIO` (`D:\_CLAUDE`, vedi [[ZirkonIA - App (Sviluppo Tecnico)]]). Deriva da [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] (il ragionamento completo, con le decisioni e gli angoli ciechi) e da [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]] (i testi da mostrare in ogni stadio). Questa nota isola solo la parte tecnica: cosa calcolare, come, e cosa serve al design.

## 1. Metriche di base da esporre

| Metrica | Cos'è | Fonte | Stato |
|---|---|---|---|
| **Parole totali** | Conteggio parole su tutte le note del brain | Già disponibile in app | ✅ esistente |
| **Nodi totali** | Numero di note/nodi nel grafo | Già disponibile in app | ✅ esistente |
| **Collegamenti totali** | Numero di wikilink/edge nel grafo | Da aggiungere | ⬜ da implementare |
| **Densità media** | Collegamenti ÷ nodi (media di edge per nodo) | Da aggiungere | ⬜ da implementare |
| **Aree attive** | Numero di temi/cartelle con almeno **N nodi collegati** (soglia N da definire in sviluppo, proposta: N=3, coerente con la regola "minimo 3 wikilink" già in uso nel vault sorgente — vedi [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]]) | Da aggiungere | ⬜ da implementare |

Le prime due (parole, nodi) alimentano l'asse "consistenza"; le ultime tre (collegamenti, densità, aree attive) alimentano l'asse "ampiezza" — vedi [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] → "Le due dimensioni di base" per la logica di prodotto dietro la distinzione. In dashboard vanno mostrate entrambe le viste: lo stadio cosmico (sotto) come narrazione principale, i due assi come dettaglio secondario per chi vuole capire cosa lo sta trainando.

## 2. Stadio cosmico — logica di calcolo

Lo stadio è determinato **esclusivamente dal conteggio parole totali**, confrontato con soglie fisse:

| Stadio | Soglia (da, parole) | Soglia (a, parole) |
|---|---|---|
| Nebula | 0 | 25.000 |
| Nucleus | 25.000 | 250.000 |
| Comet | 250.000 | 1.000.000 |
| Planet | 1.000.000 | — (nessun tetto superiore) |

```
funzione stadio_corrente(parole_totali):
    se parole_totali < 25.000:      ritorna "Nebula"
    se parole_totali < 250.000:     ritorna "Nucleus"
    se parole_totali < 1.000.000:   ritorna "Comet"
    altrimenti:                      ritorna "Planet"  # -> vedi §4 per il passaggio a Galaxy
```

Le soglie sono un'ipotesi di lavoro calibrata su un solo caso reale (il vault di Federico) — vedi [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] → "Calibrazione sulle parole" per il calcolo completo. Da tenere come **costanti configurabili**, non hardcoded, perché andranno affinate sui primi beta tester ([[ZirkonIA - Piano Beta Testing e Cronoprogramma Matteo]]) senza richiedere una nuova release.

**Importante — non confondere con il calendario coach**: il calendario degli incontri (Giorno 0/10, Mese 3/6/9/12, vedi [[ZirkonIA - Protocollo di Delivery (Metodo e Cronoprogramma Annuale)]]) è un tracciato **separato e fisso**, usato per schedulare le sessioni con il coach — non deve determinare lo stadio mostrato in dashboard. Lo stadio è sempre e solo funzione delle parole.

**UI al cambio di stadio**: quando `stadio_corrente()` cambia, mostrare il testo di reveal corrispondente da [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]] (sezione "I cinque stadi") — un evento una tantum, non un banner permanente. Nessun colore/icona che comunichi giudizio negativo se il cliente resta a lungo in uno stadio: principio fermo già fissato nella nota di lavoro (angolo cieco "rischio demotivazione").

## 3. Ritmo medio — formula e uso

```
ritmo_medio_parole_giorno = parole_totali / giorni_trascorsi_dal_giorno_zero

ritmo_medio_minuti_giorno = ritmo_medio_parole_giorno / 140
    # 140 = stima parole/minuto di parlato medio (range reale 130-150,
    # usato il valore centrale — vedi nota sul limite della stima sotto)
```

**Giorno zero — decisione da confermare in sviluppo, non ancora fissata**: due opzioni ragionevoli, con impatto diverso sul numero risultante:
- **Opzione A (consigliata)**: giorno zero = data di Consegna (Giorno 10 del Protocollo, quando il brain "diventa operativo"). Motivazione: prima di quel momento il brain è ancora in costruzione guidata dal coach, non riflette ancora il ritmo autonomo del cliente — includerlo abbasserebbe artificialmente la media nei primi mesi.
- **Opzione B**: giorno zero = Giorno 0 (prima sessione delle 100 domande). Più semplice da implementare (una sola data di riferimento, non due), ma diluisce la media con un giorno atipico (il giorno della profilazione produce un picco di parole non rappresentativo del ritmo quotidiano).

Scegliere una delle due prima di implementare — segnalare la scelta fatta in questa nota una volta decisa, non lasciarla implicita nel codice.

**Come mostrarlo in dashboard**: numero grezzo (parole/giorno) + traduzione leggibile (minuti/giorno stimati). Confronto con il ritmo di riferimento (2.740 parole/giorno, ~19,6 min/giorno — il ritmo che porta a Planet in 12 mesi) solo come inquadramento informativo ("il tuo ritmo attuale ti porta verso Planet tra circa N mesi"), **mai** come giudizio, allarme o colore rosso — stesso principio del §2.

**Limite dichiarato**: la conversione minuti↔parole è una stima, non una misura — il vault di riferimento (Federico) include anche testo generato dall'assistente in fase di strutturazione, non solo parlato puro. Trattare "140 parole/minuto" come costante configurabile, da affinare quando ci saranno dati reali da clienti che usano prevalentemente il registratore fisico (ZirkonIA Touch) invece della chat diretta.

**Reset a ogni ciclo annuale**: aperto, non risolto — vedi §4.

## 4. Galaxy — ciclo annuale, logica di transizione

A differenza degli stadi 1-4 (guidati solo dalle parole), il passaggio **da Planet a Galaxy e la rinomina di ogni Galaxy successiva sono guidati dal calendario di rinnovo (billing), non dalle parole**:

- Un cliente può superare la soglia di 1.000.000 parole (= "sostanza da Planet") anche prima dei 12 mesi — in quel caso resta visivamente/narrativamente in stadio **Planet** finché non arriva la data di rinnovo del canone (vedi [[ZirkonIA]] → "Offerta e pricing", canone dal secondo anno €1.800/anno)
- Alla data di rinnovo, indipendentemente da quante parole ha accumulato oltre 1.000.000, il cliente passa a **Galaxy — anno 1 ("Prima Lux")**
- Ogni rinnovo successivo assegna il nome dell'anno successivo nella sequenza (anno 2 "Magnum Opus", anno 3 "Mens Aeterna" — sequenza completa e testi di reveal in [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]] → "La Galaxy che cambia nome ogni anno")

**Motivazione della scelta** (non lasciarla implicita in fase di dev, è una decisione di prodotto): la rinomina Galaxy è pensata come un evento di retention legato al momento commerciale del rinnovo — mostrarla prima, solo perché il cliente ha scritto molto, la scollegherebbe dal suo scopo (dare al rinnovo un momento riconoscibile da comunicare, vedi nota di lavoro).

```
funzione stadio_visualizzato(parole_totali, data_rinnovo_corrente, numero_rinnovi):
    stadio_base = stadio_cosmico(parole_totali)   # come da §2
    se stadio_base != "Planet":
        ritorna stadio_base
    se oggi < data_rinnovo_corrente:
        ritorna "Planet"
    altrimenti:
        ritorna "Galaxy", nome_galaxy(numero_rinnovi)   # Prima Lux / Magnum Opus / Mens Aeterna / ...
```

**Sequenza di nomi oltre l'anno 3**: non ancora definita — la Serie B (registro latino) copre solo i primi 3 anni nella proposta attuale. Va estesa prima che un cliente reale arrivi al quarto rinnovo (tempo stimato ampio, non urgente, ma da non dimenticare).

## 5. Pannello Task/To-Do — sezione inferiore della dashboard
Sezione aggiuntiva richiesta da Federico (2026-08-08, ottava revisione): una lista di lavori/task quotidiani, in una fascia fissa nella parte inferiore della dashboard, sotto la rappresentazione dello stadio cosmico. Esempi reali dati da Federico per illustrare il tipo di contenuto: "mandare documenti a Cristiano", "sviluppare ZirkonIA" — task operativi di ogni giorno, non legati alla crescita del brain (nessun collegamento con parole/stadio/ritmo, salvo diversa indicazione futura).

**Origine dei task — due fonti da combinare**:
1. **Task manuali** — il cliente (o il coach) li aggiunge direttamente, come una to-do list semplice
2. **Task suggeriti dal brain** — ZirkonIA individua azioni aperte dal contenuto stesso (decisioni prese ma non ancora eseguite, follow-up citati in una sessione EDUCAZIONE, impegni presi durante una riunione registrata) e li propone come bozza da confermare — coerente con il posizionamento "alleato attivo" già descritto per gli stadi avanzati (§2, Comet/Planet: "non si limita a rispondere, anticipa, propone")

**Non è un meccanismo inventato senza precedente**: questo stesso vault applica già lo stesso pattern su sé stesso — la nota [[Punti Aperti]] tiene una lista di cose in sospeso, e ogni nota progetto ha campi `stato`/`priorita` in frontmatter (vedi ad es. questa stessa nota). Il pannello dashboard è la versione UI, esposta al cliente, di un meccanismo che il prodotto già usa internamente.

**Campi minimi per task**:
| Campo | Note |
|---|---|
| `testo` | descrizione del task |
| `stato` | da fare / in corso / fatto |
| `fonte` | manuale / suggerito dal brain |
| `priorita` (opzionale) | alta / media / bassa |
| `data` (opzionale) | scadenza, se presente |

**Comportamento**:
- Sezione fissa, sempre visibile, non legata a uno stadio specifico
- Task completati restano visibili/archiviati per un periodo invece di sparire subito (coerente con il principio "l'archivio non cancella, sposta" già in uso nel vault sorgente)
- Nessuna interazione con il conteggio parole o lo stadio cosmico nella v1 — sistemi separati

**Raccomandazione sullo scope v1**: solo task manuali nella prima versione. "Task suggeriti dal brain" richiede analisi del contenuto delle note per individuare azioni aperte — funzionalità più corposa, da trattare come v2 una volta che il resto del sistema di stadi/reveal è stabile, non da bloccare la prima release.

## 6. Schema dati proposto (per API/stato applicativo)

Non vincolante nell'implementazione, ma utile come lista completa dei campi che la dashboard deve poter leggere:

```json
{
  "parole_totali": 129749,
  "nodi_totali": 319,
  "collegamenti_totali": null,
  "densita_media": null,
  "aree_attive": null,
  "stadio_cosmico": "Comet",
  "soglia_stadio_successivo": 1000000,
  "parole_mancanti_a_stadio_successivo": 870251,
  "giorno_zero": "2026-07-12",
  "ritmo_medio_parole_giorno": 3507,
  "ritmo_medio_minuti_giorno": 25.1,
  "galaxy_numero_rinnovo": 0,
  "galaxy_nome_corrente": null,
  "data_prossimo_rinnovo": "2027-07-12",
  "task_list": [
    { "testo": "Mandare documenti a Cristiano", "stato": "da fare", "fonte": "manuale", "priorita": "alta", "data": null },
    { "testo": "Sviluppare ZirkonIA — modulo X", "stato": "in corso", "fonte": "manuale", "priorita": "media", "data": null }
  ]
}
```

## 7. Brief per l'emblema visivo dello stadio

Richiesta di Federico: uno **stesso emblema/logo che cambia forma in base allo stadio raggiunto**, non un'icona generica per livello — e deve prendere ispirazione dal design del grafo stesso, non essere un elemento scollegato da esso.

**Direzione proposta, da validare con chi disegna l'interfaccia**:
- L'emblema usa lo stesso linguaggio visivo del grafo reale del cliente (punti/nodi + linee di collegamento), non un'iconografia a parte — deve leggersi come un "ritratto distillato" del grafo del cliente in quel momento, non un badge decorativo indipendente
- **Nebula**: punti sparsi, radi, senza una forma riconoscibile, opacità bassa
- **Nucleus**: i punti si addensano verso un centro — una forma piccola e densa
- **Comet**: la forma densa si allunga, con una "coda" di punti più radi dietro di sé — suggerisce movimento
- **Planet**: una forma chiusa, coerente, quasi circolare — con l'icona cristallina ufficiale (vedi [[Brand Kit ZirkonIA]] → "Z cristallino") integrata al centro come nucleo dell'emblema
- **Galaxy**: la forma si apre in una spirale o in cluster multipli attorno a un centro — varia leggermente tono/texture per ogni Galaxy annuale (proposta: Prima Lux più chiara/luminosa, Magnum Opus più satura/profonda, Mens Aeterna la versione più rifinita, quasi cristallina in ogni punto — da validare con chi disegna, è una proposta di direzione non un vincolo)
- Palette da riusare, non inventarne una nuova: gradiente verde-smeraldo `#3BC79B` → blu-petrolio `#3B93BA` già definito in [[Brand Kit ZirkonIA]]

**Formati necessari**: versione statica piccola (badge da header dashboard) e, se possibile, una versione animata/transizione per il momento esatto in cui lo stadio cambia (coerente col reveal testuale del §2) — non bloccante per una prima versione, ma da tenere in roadmap.

## 8. Domande aperte per lo sviluppo (da chiudere prima del rilascio)
- [ ] Confermare l'opzione A o B per il "giorno zero" del ritmo medio (§3)
- [ ] Definire la soglia N di "aree attive" (proposta N=3, da validare)
- [ ] Decidere se il reset del giorno-zero a ogni nuovo ciclo Galaxy è nel v1 o rimandato (vedi nota di lavoro, punto lasciato aperto da Federico)
- [ ] Estendere la sequenza di nomi Galaxy oltre l'anno 3
- [ ] Verificare se il layout del grafo reale può essere calibrato per assomigliare visivamente agli stadi descritti (nucleo denso → cluster → rete stellare), non solo l'emblema separato del §7
- [ ] Confermare lo scope v1 del pannello task (§5): solo manuali, o includere da subito i "suggeriti dal brain"
- [ ] Decidere se il pannello task è cliente-per-cliente o condiviso/visibile anche al coach durante gli incontri di allineamento

## Collegamenti
- [[ZirkonIA - Dashboard Maturità del Brain (Report di Funzionamento)]] — come funziona davvero oggi, dopo l'implementazione (questa nota era il piano, prima di scrivere il codice)
- [[ZirkonIA - Prompt di Implementazione Dashboard Maturità del Brain]] — la versione sintetica e azionabile di questa specifica, verificata contro lo screenshot reale della dashboard, pronta da incollare in una sessione di sviluppo
- [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] — il ragionamento completo dietro ogni numero e ogni scelta qui
- [[Punti Aperti]] — precedente diretto del pannello task: lo stesso pattern già in uso in questo vault, qui esposto come funzionalità del prodotto
- [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]] — i testi da mostrare in dashboard per ogni stadio e per ogni Galaxy
- [[Report - Sessione Dashboard Maturità ZirkonIA (2026-08-08)]] — il percorso completo della sessione
- [[ZirkonIA - App (Sviluppo Tecnico)]] — dove vive il codice (repo STUDIO, `D:\_CLAUDE`)
- [[ZirkonIA - Protocollo di Delivery (Metodo e Cronoprogramma Annuale)]] — il calendario coach, separato dallo stadio cosmico
- [[Brand Kit ZirkonIA]] — palette e icona cristallina per l'emblema
- [[ZirkonIA - Piano Beta Testing e Cronoprogramma Matteo]] — dove verranno validate le soglie e le costanti
