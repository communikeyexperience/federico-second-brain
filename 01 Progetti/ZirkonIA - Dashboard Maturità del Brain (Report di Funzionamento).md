---
data: "2026-08-08"
tipo: progetto
stato: attivo
priorita: media
cliente: ""
tags: [zirkonia, dashboard, report, maturità-brain, documentazione]
summary: "Report tecnico-concettuale di come funziona OGGI la Dashboard di maturità del brain in ZirkonIA GUI (repo sperimentale in C:\\Users\\user\\Desktop\\ZirkonIA GUI): i 5 stadi cosmici, le soglie di parole, il ritmo medio, il dock visivo, il reveal one-time, Galaxy, il pannello Task collegato a [[Punti Aperti]]. Fotografa lo stato reale del codice al 2026-08-08, dopo l'implementazione — complementare a [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]] (che era il piano, prima di scrivere il codice)."
---

# ZirkonIA — Dashboard Maturità del Brain: report di funzionamento (stato attuale)

> Non è un piano: è la fotografia di come funziona **oggi** la Dashboard, dopo una sessione di sviluppo e iterazione visiva sul progetto sperimentale **ZirkonIA GUI** (`C:\Users\user\Desktop\ZirkonIA GUI`, un fork "solo Dashboard/Grafo" distinto dall'app 1.0 in `D:\_CLAUDE`). Per il ragionamento originale dietro ogni scelta vedi [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]]; per i testi mostrati in-app vedi [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]].

## 1. Cosa vede il cliente, in ordine dall'alto

Il tab, prima chiamato "Panoramica", ora si chiama **Dashboard** (il tab "Grafo" è invariato). Dall'alto:

1. **Hero di maturità** — lo stadio cosmico, il "dock" con tutti e 5 gli stadi, il ritmo medio
2. Le 5 card metriche originali (Note totali, Parole totali, Collegamenti, Cartelle, Note isolate) — invariate
3. Grafico "Attività — ultimi 30 giorni" — reso più basso/sottile
4. **Pannello Task** — spostato qui (prima era in fondo alla pagina)
5. "Note più connesse" e "Modificate di recente" — invariate

Rimossi rispetto alla prima versione: "Tendenza mensile" e "Distribuzione per cartella" — giudicati poco utili, tolti insieme al codice che li generava.

## 2. I 5 stadi cosmici — come si calcola quello attuale

Lo stadio è funzione **esclusivamente del conteggio parole totali** (lo stesso numero già mostrato nella card "Parole totali" — nessun doppio conteggio):

| Stadio | Soglia (da) | Soglia (a) |
|---|---|---|
| **Nebula** | 0 parole | 25.000 |
| **Nucleus** | 25.000 | 250.000 |
| **Comet** | 250.000 | 1.000.000 |
| **Planet** | 1.000.000 | — (nessun tetto) |
| **Galaxy** | oltre Planet | — (guidato dal tempo, non dalle parole — vedi §5) |

Queste tre soglie (25k / 250k / 1M) sono **costanti configurabili** in un solo punto del codice (`DEFAULT_STAGE_THRESHOLDS` in `src/lib/maturity.ts`), non sparse nel codice — pensate per essere affinate sui beta tester reali senza toccare il resto della logica.

**Regola di tono, rispettata in ogni punto dell'interfaccia**: nessun colore rosso, nessuna icona di allarme. Se il cliente resta a lungo in uno stadio, l'unico messaggio è neutro ("mancano N parole al prossimo stadio").

## 3. Il "dock" degli stadi — la parte visiva più elaborata

Sotto il titolo "Stadio di maturità del tuo brain" c'è una riga con **tutti e 5 gli stadi sempre visibili**, non solo quello raggiunto — in stile dock di macOS:

- Lo stadio raggiunto è **al centro**, a piena dimensione, colorato, con il nome in maiuscolo grande e il range di parole sotto
- Gli altri quattro sono **sempre presenti** (passati a sinistra, futuri a destra), ma più piccoli e in stile **"ghost"** (grigio desaturato — stesso linguaggio usato per le categorie spente nella legenda del Grafo)
- Ogni icona, anche quelle ghost, mostra comunque il proprio nome (maiuscolo, piccolo) e il proprio range di parole (solo numeri, es. "250.000 – 1.000.000") — così il cliente vede a colpo d'occhio l'intera scala, non solo dove si trova
- **Rimpicciolimento a cascata**, non uniforme: rispetto allo stadio centrale, il primo vicino è al 60% della dimensione, il secondo al 48%, il terzo al 38,4% (ogni passo è −40% poi due volte −20% rispetto al passo precedente, non una riduzione fissa dal 100%) — effetto "dock" più naturale di una scala lineare
- Le icone sono allineate al centro (non su un'unica riga di base): ogni blocco icona+nome è centrato sul proprio baricentro, così il nome resta vicino alla propria icona invece di allinearsi tutto su una riga condivisa

### Le icone: linguaggio visivo organico, non geometria pura

Ogni emblema è disegnato con punti e linee — lo stesso linguaggio del Grafo reale — e usa la **stessa palette di colori del Grafo** (oro/verde/blu con rari accenti rossi), non un gradiente unico. I punti hanno un effetto "fade"/glow (alone morbido + nucleo pieno), non cerchi piatti. Le posizioni sono generate con formule deterministiche (mai casuali: l'icona non deve "saltare" ad ogni render) ma con jitter organico — non poligoni perfettamente regolari — con uno spacing minimo garantito per evitare che i pallini si sovrappongano, anche aumentando la densità.

Concetto distintivo per stadio:
- **Nebula**: punti sparsi, senza un centro riconoscibile — "dati ancora non ordinati"
- **Nucleus**: un centro dorato con un cluster organico di satelliti colorati attorno — "qualcosa che tiene"
- **Comet**: testa densa + una coda **corta e curva** ("swoosh", effetto più dinamico/futuristico di una semplice diagonale) — "il brain che si muove"
- **Planet**: doppio anello organico attorno a un **nucleo cristallino** (l'unico elemento che mantiene il gradiente di brand ufficiale verde-smeraldo → blu-petrolio, in attesa dell'asset PNG reale "Z cristallino" — vedi [[Brand Kit ZirkonIA]]) — "un corpo formato"
- **Galaxy**: bracci a spirale, colore che varia leggermente per ogni anno di Galaxy — "espansione"

Nota di correzione fatta in corsa: la prima versione dell'emblema Nucleus aveva un motivo a bracci piegati che, a uno sguardo veloce, poteva leggersi come una svastica — sostituito con un motivo puramente radiale (raggi dal centro, nessun braccio ruotato), che non ha questo rischio per costruzione.

## 4. Il tuo ritmo medio

Card a destra dell'hero. Formula:

```
ritmo_parole_giorno = parole_totali / giorni_trascorsi_dal_giorno_zero
ritmo_minuti_giorno = ritmo_parole_giorno / 140   (140 = parole/minuto di parlato medio, stima configurabile)
```

**La metrica mostrata in primo piano è i minuti/giorno**, non le parole/giorno — scelta esplicita perché "parole/giorno" è un numero poco intuitivo per chi non pensa in termini di battitura; le parole/giorno restano visibili ma come dettaglio secondario sotto.

**"Giorno zero"** (l'inizio da cui si conta il ritmo) è oggi calcolato **automaticamente come la nota meno recentemente modificata nel vault** — nessun campo manuale da compilare. Limite dichiarato e accettato consapevolmente: su un vault preesistente all'attivazione di ZirkonIA (come questo, o quello di Cristiano), il "giorno zero" risulta più indietro nel tempo del vero inizio del percorso ZirkonIA, quindi il ritmo medio calcolato oggi è sottostimato rispetto al ritmo reale di lavoro con ZirkonIA. Non blocca l'uso, ma è da tenere presente leggendo il numero.

Sotto, un confronto informativo (mai un voto): il ritmo di riferimento è **2.740 parole/giorno (~19,6 min/giorno)** — il ritmo che porta a Planet in 12 mesi.

## 5. Galaxy — perché non è "solo un altro stadio a parole"

A differenza dei primi 4 stadi (guidati solo dal conteggio parole), il passaggio da Planet a Galaxy è **guidato dal tempo trascorso dal giorno zero**, non dalle parole:

- Un cliente può superare 1.000.000 parole molto prima di 12 mesi: resta comunque "Planet" finché non matura il tempo
- Oggi (in assenza di un vero sistema di billing collegato) il "rinnovo" è approssimato come **multipli di 365 giorni dal giorno zero** — quando ne passa uno, chi è già a Planet diventa Galaxy
- Ogni Galaxy ha un nome che cambia ogni anno (registro latino): **anno 1 = Prima Lux, anno 2 = Magnum Opus, anno 3 = Mens Aeterna** — sequenza da estendere prima che un cliente reale arrivi al 4° anno

Questa è una scelta di prodotto deliberata (vedi [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]]): la rinomina Galaxy è pensata come un momento di retention legato al rinnovo commerciale, non un traguardo che si "sblocca" solo scrivendo tanto.

## 6. Il reveal — quando compare, quando no

Al primo raggiungimento di un nuovo stadio compare un modal a tutto schermo con: emblema grande, nome, il testo "letterario" completo (quello di [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]]) e un riquadro "Cosa fai ora". **È un evento una tantum**, non un banner permanente — la versione persistente in dashboard è una frase motivazionale breve ("Sei al secondo stadio del tuo brain. Continua così."), diversa e più asciutta.

Punto tecnico importante: il reveal **non scatta retroattivamente**. Se un brain è già a Nucleus quando questa funzione viene attivata per la prima volta, l'app registra silenziosamente "Nucleus" come stadio già visto, senza mostrare un pop-up di festeggiamento per qualcosa che è già acquisito da tempo. Scatta solo su un vero avanzamento osservato dall'app (es. da Nucleus a Comet mentre l'app è in uso). Questo stato è salvato per brain, non globale.

## 7. Pannello Task — non un secondo sistema, ma una vista sulla nota reale

Cambio di rotta importante rispetto alla prima versione: il pannello Task **non è più un gestionale separato con task salvati a parte**. Ora **legge live** la nota del vault che il brain usa già come lista di cose in sospeso — cercata per nome esatto, **"Punti Aperti"** (la stessa nota che questo vault usa da tempo per lo stesso scopo). È sempre la versione più aggiornata perché non è una copia: è il contenuto vero del file in questo momento.

Come funziona:
- Cerca nel vault una nota chiamata "Punti Aperti" (case-insensitive)
- La legge e la suddivide per sezioni (i titoli `##`) e checkbox (`- [ ]` / `- [x]`)
- La mostra raggruppata, collassabile per sezione, con il conteggio di quanti punti sono ancora aperti per sezione

**Limite noto**: la ricerca è per nome esatto. Funziona già bene per questo vault; se un brain-cliente futuro chiamasse la propria nota di cose-in-sospeso in altro modo, oggi il pannello mostra semplicemente un messaggio "nessuna nota trovata" invece di un errore — non c'è ancora un modo per indicare un nome alternativo.

## 8. Cosa resta esplicitamente aperto (da [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]], non tutto risolto oggi)

- Confermare definitivamente il significato di "giorno zero" quando si introdurrà una vera data di consegna/attivazione per cliente (oggi è solo un proxy automatico, vedi §4)
- "Aree attive" (soglia N=3) e "densità media" — metriche previste nella specifica originale, non ancora implementate in dashboard
- Validare le soglie di parole (25k/250k/1M) sui primi beta tester reali — oggi calibrate solo sul ritmo di Federico
- Estendere la sequenza di nomi Galaxy oltre l'anno 3
- Icona cristallina ufficiale "Z cristallino": non ancora disponibile come file nel repo, l'emblema Planet/Galaxy usa uno stand-in geometrico con il gradiente di brand corretto

## Collegamenti
- [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]] — il piano tecnico originale, prima di scrivere il codice
- [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]] — tutti i testi di reveal usati in-app
- [[ZirkonIA - Prompt di Implementazione Dashboard Maturità del Brain]] — il prompt sintetico usato per avviare lo sviluppo
- [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] — il ragionamento di prodotto completo dietro ogni scelta
- [[Report - Sessione Dashboard Maturità ZirkonIA (2026-08-08)]] — il percorso narrativo della sessione di lavoro sui contenuti
- [[Punti Aperti]] — la nota che il pannello Task legge live
- [[Brand Kit ZirkonIA]] — palette e icona cristallina per l'emblema
- [[ZirkonIA - App (Sviluppo Tecnico)]] — dove vive il codice (repo sperimentale ZirkonIA GUI, distinto dall'app 1.0)
