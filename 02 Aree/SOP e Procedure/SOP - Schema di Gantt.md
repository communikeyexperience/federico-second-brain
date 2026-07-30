---
data: "2026-07-22"
tipo: sop
tags: [gantt, cronosequenza, template, visualizzazione, sop]
---

# SOP — Schema di Gantt

## Obiettivo
Standard da applicare ogni volta che Federico chiede uno "schema di Gantt" o una "cronosequenza" con rappresentazione grafica — non ricominciare da zero il design ogni volta, partire da questo template.

## Quando si applica
Qualunque richiesta di cronosequenza/roadmap operativa con rappresentazione grafica su linea del tempo, non solo elenco testuale di tappe.

## Riferimento — file d'esempio
Il template è stato validato il 2026-07-22 su [[Cronosequenza Iknosys - Fagioli-Roberto Atzori (22 lug - 18 nov 2026)]] (pagina 1), dopo tre round di correzione con Federico. Usare quel file come riferimento visivo diretto.

## Le regole

**Struttura**: una riga per fase/evento, non un'unica striscia orizzontale con card posizionate a mano. Ogni riga = un badge numerato + titolo breve + date, a sinistra in colonna fissa; a destra la "corsia" (lane) con la barra colorata posizionata esattamente in percentuale sulla durata reale (data inizio/fine convertita in % del periodo totale).

**Perché le righe e non le card sovrapposte**: la prima versione (card posizionate con coordinate assolute vicino a una singola linea del tempo) ha prodotto sovrapposizioni testo/grafica non professionali. Il fix strutturale è dare a ogni fase la propria corsia orizzontale esclusiva — così due elementi non possono mai condividere lo stesso spazio, non serve calcolare a mano se si toccano.

**Precisione delle date**: non fermarsi alle sole date di inizio mese. Aggiungere tacche/etichette intermedie ogni 5 giorni (5, 10, 15, 20, 25, 30) sotto l'asse, più leggere/piccole delle etichette di inizio mese (che restano in grassetto). Questo è quello che Federico intende per "dati ben leggibili" — deve poter leggere a colpo d'occhio quando inizia/finisce un evento, non solo in che mese.

**Milestone/scadenze vincolanti**: quando una fase è un evento puntuale (non un intervallo, es. "lancio campagna entro il 20 agosto"), non trattarla come le altre barre — darle uno stile distinto (colore scuro/contrasto, tag con testo "SCADENZA VINCOLANTE" o simile) così salta all'occhio come punto critico, non come una fase qualunque.

**Testo dentro le barre**: solo se la barra è abbastanza larga da contenerlo comodamente. Per barre strette, meglio nessun testo dentro (il titolo/date sono già nella colonna fissa a sinistra) piuttosto che testo che trabocca o si stringe illeggibile.

**Nota di cornice**: chiudere sempre con un box di nota (stile giallo/pesca, bordo sinistro colorato) per eventuali discrepanze non risolte (es. durata dichiarata in riunione vs. durata reale calcolata) — mai correggere in silenzio, sempre segnalare.

## Margini di miglioramento — da ricerca web (2026-07-22)
Ricerca fatta su richiesta di Federico per affinare lo standard. Convenzioni professionali non ancora applicate nel template attuale, da valutare per versioni future se il caso lo richiede:
- **Linea "oggi"**: molti Gantt professionali tracciano una linea verticale continua per tutta l'altezza del grafico nel punto corrispondente alla data corrente, non solo un'etichetta testuale sull'asse.
- **Milestone come rombo**: la convenzione standard per un evento puntuale (durata zero) è un marcatore a forma di rombo sulla linea del tempo, non una barra sottile — da considerare per le "scadenze vincolanti".
- **Frecce di dipendenza**: quando una fase può iniziare solo al termine di un'altra, una freccia che collega la fine di una barra all'inizio della successiva rende esplicita la dipendenza — utile se in futuro le fasi non sono strettamente sequenziali senza sovrapposizione.
- **Evidenziazione del percorso critico**: colorare/evidenziare la sequenza di fasi che determina la durata minima del progetto (nel caso Iknosys, le fasi 2-3 erano già state segnalate a parole come "il punto più a rischio" — si potrebbe rendere anche visivamente, con una fascia/sottolineatura dedicata).

Fonti consultate: [Docsie — Gantt Chart glossary](https://www.docsie.io/blog/glossary/gantt-chart/), [Airtable — Gantt view milestones, dependencies, and critical paths](https://support.airtable.com/docs/gantt-view-milestones-dependencies-and-critical-paths), [Figma — What is a Gantt Chart?](https://www.figma.com/resource-library/what-is-a-gantt-chart/), [Wrike — Gantt chart basics](https://www.wrike.com/project-management-guide/gantt-chart-basics/), [TeamGantt — Gantt Chart Guide](https://www.teamgantt.com/what-is-a-gantt-chart).

## Collegamenti
- [[Cronosequenza Iknosys - Fagioli-Roberto Atzori (22 lug - 18 nov 2026)]] — file di riferimento
- [[Fagioli - Preparazione Conversazione HubSpot e Roberto Atzori]] — contesto che ha generato questo standard
- [[Riunione con Roberto Atzori - Collaborazione e Iknosys (2026-07-18)]]
- [[Processi e Convenzioni]]
