---
data: "2026-08-08"
tipo: progetto
stato: attivo
priorita: alta
cliente: ""
percorso_file: "D:\_CLAUDE"
tags: [zirkonia, dashboard, sviluppo, prompt, implementazione]
summary: "Prompt di implementazione pronto da incollare per lo sviluppo (repo STUDIO): aggiunge il sistema di maturità cosmico (Nebula/Nucleus/Comet/Planet/Galaxy), la metrica di ritmo medio, l'emblema visivo e il pannello task alla dashboard esistente — rinominando il tab 'Panoramica' in 'Dashboard' — senza toccare i widget già costruiti (313 note, 133.365 parole, 958 collegamenti, attività 30gg, tendenza mensile, distribuzione cartelle, note connesse, modifiche recenti)."
---

# ZirkonIA — Prompt di Implementazione: Dashboard di Maturità del Brain

> Screenshot dello stato reale della dashboard allegato da Federico il 2026-08-08 — prima verifica diretta contro il codice vero, non solo contro la descrizione teorica in [[ZirkonIA - App (Sviluppo Tecnico)]]. Questa nota contiene il **prompt pronto da incollare** in una sessione di sviluppo (Claude Code o altro, repo `STUDIO`, `D:\_CLAUDE`). Il ragionamento completo dietro ogni numero è in [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] e [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]] — qui solo la sintesi azionabile.

## Il prompt

```
CONTESTO — stato attuale verificato (screenshot 2026-08-08)

La dashboard dell'app ZirkonIA ha oggi due tab in alto: "Panoramica" e "Grafo"
(più un pulsante "Cambia brain"). Il tab "Panoramica" mostra, dall'alto:

1. Cinque card metriche: Note totali (313), Parole totali (133.365),
   Collegamenti (958), Cartelle (6), Note isolate (0)
   — nota già presente sotto le card: "Il conteggio parole è sul corpo delle
   note (frontmatter escluso) e non considera le Skill dell'assistente."
2. Grafico "Attività — ultimi 30 giorni" (barre giornaliere, note toccate)
3. Grafico "Tendenza mensile" (barre, con selettore di range temporale)
4. "Distribuzione per cartella" (barre orizzontali: 02 Aree, 03 Risorse,
   01 Progetti, 00 Inbox, radice, 04 Archivio)
5. "Note più connesse" (lista con conteggio link)
6. "Modificate di recente" (lista con data "oggi"/altro)

TUTTO QUESTO FUNZIONA GIÀ E VA PRESERVATO. Non rimuovere, non rinominare,
non ristrutturare nessuno dei sei blocchi sopra, non cambiare la logica di
calcolo delle metriche esistenti (in particolare: il conteggio "Parole
totali" deve restare la fonte unica di verità anche per il nuovo sistema
sotto — non introdurre un secondo conteggio parole con logica diversa).


OBIETTIVO DI QUESTA MODIFICA

1. Rinominare il tab "Panoramica" in "Dashboard" (resta il tab di default/
   primo tab). Il tab "Grafo" non cambia nome.
2. Aggiungere alla vista "Dashboard" (non al tab "Grafo") un sistema di
   maturità del brain a 5 stadi cosmici, con soglie basate sul conteggio
   parole già esistente, una metrica di ritmo medio, un emblema visivo
   che cambia con lo stadio, la logica del ciclo annuale "Galaxy", e un
   pannello task in fondo alla pagina.

Posizionamento proposto nel layout esistente: il blocco di maturità
(stadio + emblema + ritmo medio) va aggiunto SOPRA le cinque card
metriche attuali, come nuovo elemento "hero" della pagina — le card
esistenti restano sotto, invariate, come dettaglio di supporto. Il
pannello task va aggiunto IN FONDO alla pagina, dopo "Modificate di
recente" — sezione nuova, non sostituisce nulla.


1) STADIO COSMICO — logica di calcolo

Stadio determinato dal campo "parole totali" già calcolato dall'app
(oggi 133.365 → cade nella fascia Nucleus):

  Nebula   : 0           <= parole < 25.000
  Nucleus  : 25.000      <= parole < 250.000
  Comet    : 250.000     <= parole < 1.000.000
  Planet   : parole >= 1.000.000   (nessun tetto superiore)

Le soglie sono costanti configurabili (non hardcoded): sono un'ipotesi
di lavoro calibrata su un solo brain reale, da affinare sui beta tester.

Ogni stadio ha: un nome, un breve testo di reveal (mostrato una tantum
al primo raggiungimento, non un banner permanente), un "cosa sai fare
ora" e uno "sblocco". Testi completi, pronti da usare, in
[[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]]
→ sezione "I cinque stadi". Non inventare nuovo copy: usare quello lì.

REGOLA DI TONO, non negoziabile: nessun colore rosso, nessun'icona di
allarme, nessun messaggio che suoni come un giudizio se il cliente resta
a lungo in uno stadio. Solo informazione neutra ("mancano N parole al
prossimo stadio").


2) RITMO MEDIO — formula

  ritmo_medio_parole_giorno = parole_totali / giorni_trascorsi_da_giorno_zero
  ritmo_medio_minuti_giorno = ritmo_medio_parole_giorno / 140

  (140 = parole/minuto di parlato medio, stima configurabile)

"giorno_zero" = data di creazione/attivazione del brain (DECISIONE DA
CONFERMARE prima di implementare: giorno della consegna/Fase 1 vs. giorno
della prima sessione — vedi [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]]
→ §3 per il dettaglio del trade-off, non deciderlo silenziosamente nel
codice).

Mostrare: numero grezzo (parole/giorno) + numero tradotto (minuti/giorno
stimati). Confronto col ritmo di riferimento (2.740 parole/giorno, ~19,6
min/giorno — il ritmo che porta a Planet in 12 mesi) solo come
inquadramento informativo, mai come voto.


3) EMBLEMA VISIVO — cosa deve rappresentare

Un singolo elemento grafico (badge/icona) che cambia forma con lo
stadio, posizionato accanto al nome dello stadio nel blocco hero.
Deve usare lo stesso linguaggio visivo del grafo reale (punti/nodi +
linee), non un'icona scollegata:
  - Nebula:  punti sparsi, radi, bassa opacità
  - Nucleus: punti addensati verso un centro, forma piccola e densa
  - Comet:   forma densa allungata, con una coda di punti più radi
  - Planet:  forma chiusa e coerente, quasi circolare, con l'icona
             cristallina ufficiale ("Z cristallino", vedi
             [[Brand Kit ZirkonIA]]) integrata al centro
  - Galaxy:  forma a spirale/cluster multipli, texture che varia
             leggermente per ogni Galaxy annuale (vedi punto 4)

Palette: riusare il gradiente verde-smeraldo #3BC79B → blu-petrolio
#3B93BA già definito in [[Brand Kit ZirkonIA]], non introdurne una nuova.
Serve una versione statica piccola (badge); una versione animata per il
momento del cambio di stadio è desiderabile ma non bloccante per il v1.


4) GALAXY — ciclo annuale, quando scatta

Il passaggio da Planet a Galaxy (e ogni rinomina successiva) è guidato
dal CALENDARIO DI RINNOVO del canone, non dal conteggio parole:

  - Un cliente può superare 1.000.000 parole prima dei 12 mesi: resta
    visivamente in stadio "Planet" finché non arriva la data di rinnovo
  - Alla data di rinnovo, il cliente passa a "Galaxy" con il nome
    dell'anno corrispondente:
      anno 1 = "Prima Lux"
      anno 2 = "Magnum Opus"
      anno 3 = "Mens Aeterna"
      (sequenza da estendere oltre l'anno 3 prima che serva davvero)
  - Testi di reveal per ogni Galaxy in
    [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]]
    → "La Galaxy che cambia nome ogni anno"

NON collegare la transizione Galaxy al superamento delle parole: è una
scelta di prodotto deliberata (retention legata al momento commerciale
del rinnovo), non un dettaglio implementativo arbitrario.


5) PANNELLO TASK — sezione in fondo alla pagina "Dashboard"

Sezione fissa, sotto "Modificate di recente", NON legata al conteggio
parole o allo stadio cosmico (sistema indipendente).

Campi per task: testo, stato (da fare / in corso / fatto), fonte
(manuale / suggerito dal brain), priorità opzionale, data opzionale.

SCOPE v1 (raccomandato): solo task manuali — il cliente/coach li
aggiunge a mano, lista semplice con checkbox. "Task suggeriti dal
brain" (ZirkonIA individua da sola azioni aperte nel contenuto) è v2,
non bloccare il rilascio su questo.


SCHEMA DATI DI RIFERIMENTO (non vincolante nell'implementazione)

{
  "parole_totali": 133365,          // già esistente, riusare
  "nodi_totali": 313,               // già esistente, riusare
  "collegamenti_totali": 958,       // già esistente, riusare
  "stadio_cosmico": "Nucleus",      // nuovo, calcolato da parole_totali
  "soglia_stadio_successivo": 250000,
  "parole_mancanti_a_stadio_successivo": 116635,
  "giorno_zero": "2026-07-12",      // da confermare quale evento lo definisce
  "ritmo_medio_parole_giorno": null,
  "ritmo_medio_minuti_giorno": null,
  "galaxy_numero_rinnovo": 0,
  "galaxy_nome_corrente": null,
  "data_prossimo_rinnovo": null,
  "task_list": []
}


PRIMA DI CONSIDERARE FATTO IL LAVORO — checklist

[ ] Tab rinominato "Panoramica" -> "Dashboard", tab "Grafo" invariato
[ ] Le cinque card esistenti + i quattro blocchi sotto sono ancora lì,
    identici, non riposizionati oltre a "spostati più in basso" per
    fare spazio al nuovo blocco hero
[ ] Il conteggio "parole totali" usato per lo stadio è lo STESSO numero
    già mostrato nella card "Parole totali" (nessun doppio conteggio)
[ ] Nessun elemento del nuovo sistema mostra un giudizio negativo/rosso
[ ] Le soglie (25k/250k/1M) sono costanti configurabili, non hardcoded
    sparse nel codice
[ ] Il pannello task non ha nessuna dipendenza dal sistema di stadi
```

## Collegamenti
- [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]] — dettaglio tecnico completo, formule estese, domande aperte
- [[ZirkonIA - Presentazione Dashboard Maturità del Brain (Contenuto Sorgente)]] — tutti i testi da usare (reveal stadi, Galaxy, apertura, chiusura)
- [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] — il ragionamento completo dietro ogni scelta
- [[Report - Sessione Dashboard Maturità ZirkonIA (2026-08-08)]] — percorso narrativo dell'intera sessione
- [[ZirkonIA - App (Sviluppo Tecnico)]] — dove vive il codice (repo STUDIO)
- [[Brand Kit ZirkonIA]] — palette e icona cristallina per l'emblema
