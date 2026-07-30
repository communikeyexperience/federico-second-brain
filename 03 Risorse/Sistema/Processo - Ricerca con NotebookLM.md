---
tipo: risorsa
tags: [sistema, notebooklm, ricerca, processo]
---

# Processo — Ricerca con NotebookLM → Obsidian

Come usare NotebookLM per fare ricerca web su un soggetto (persona, cliente, competitor, tema) e trasformarla in note affidabili in questo vault. Nato dal lavoro fatto sul profilo di Federico stesso nel notebook "FG Second Brain" — qui generalizzato per riusarlo su qualsiasi altro soggetto attivo.

## Quando si attiva

- Nasce un nuovo soggetto da profilare a fondo: un cliente nuovo, un competitor per [[ZirconIA]], un tema per la content pipeline.
- Un soggetto esistente ha nuovo materiale: un progetto avanza, un cliente manda documenti, un'attività online cambia.
- Serve aggiornare periodicamente un profilo già creato (come succede per [[Federico Gaudino]]).

Non è un processo a calendario fisso: si attiva quando un progetto/soggetto è **attivo** e c'è qualcosa di nuovo da cercare o verificare — non una scadenza automatica.

## Cosa può fare NotebookLM (in pratica)

- **Fonti web**: si cercano direttamente dentro NotebookLM ("Cerca nuove fonti sul web") o si incollano URL specifici. Per pagine che bloccano lo scraping (LinkedIn personale, Instagram) l'import URL fallisce: si usa allora **"Testo copiato"**, incollando a mano il contenuto catturato via browser.
- **Deep Research**: genera un report di sintesi ampio su un argomento, incrociando più fonti — utile per un primo quadro complessivo su un soggetto nuovo.
- **Chat mirata**: domande puntuali con risposta grounded sulle fonti caricate — utile per fatti specifici (date, referenti, cifre, ruoli).
- **Studio** (pannello a destra): Report, Mappa mentale, Tabella di dati, Timeline dentro un report, Audio/Video Overview, Flashcard, Quiz, Infografica. Non tutti servono sempre — vedi sotto quale scegliere.

## Quale output scegliere, in base al soggetto

| Tipo di soggetto | Output NotebookLM più utile | Dove finisce in Obsidian |
|---|---|---|
| Persona / profilo (es. un nuovo referente, un partner) | Deep Research per il quadro generale + chat mirata per fatti puntuali | Nota profilo o sezione "Chi è" della nota cliente |
| Cliente / progetto con documenti propri (riunioni, email, contratti) | Chat mirata per estrarre decisioni e scadenze | Sezione "Prossimi passi" o "Stato attuale" del progetto |
| Competitor / mercato (es. ricerca per ZirconIA) | Deep Research + Tabella di dati o Mappa mentale per confronti strutturati | Nota area/risorsa dedicata |
| Content pipeline (sintesi prima di scrivere) | Deep Research come base, poi riscrittura in voce propria | Bozza articolo/post nel progetto relativo |

Non è una regola rigida: si sceglie in base a cosa serve davvero, non per completezza.

## La regola ferrea di verifica

Lezione imparata sul profilo di Federico: quasi ogni nome ha omonimi (un calciatore, un consulente in Spagna, un'azienda con lo stesso nome in un'altra città). Prima di tenere una fonte:

1. **Cita esplicitamente il soggetto per nome**, non solo per argomento generico? Una fonte "di contesto" (es. panoramica di mercato) non è una conferma, anche se topicamente rilevante.
2. **È davvero lo stesso soggetto** e non un omonimo? Incrociare almeno 2-3 dettagli distintivi (località, data, azienda collegata, ruolo) prima di accettare una fonte come valida.
3. Se il soggetto stesso corregge o conferma un dato (es. "sì, questa è la mia azienda"), quel dato passa da "da verificare" a **confermato** — e va segnalato come tale nella nota.

Le fonti che non superano questo controllo vanno rimosse dal notebook, non solo ignorate: un notebook pieno di fonti non pertinenti degrada la qualità di ogni Deep Research successivo.

## Workflow passo-passo

1. **Crea o riusa un notebook dedicato al soggetto** — un notebook per soggetto (persona/cliente/progetto/competitor), non un unico notebook per tutto. Se il soggetto è collegato a un progetto/cliente già esistente in Obsidian, riusa il suo notebook se già ne ha uno.
2. **Aggiungi fonti**: ricerca web dentro NotebookLM o URL diretti; "Testo copiato" per le pagine bloccate.
3. **Verifica ogni fonte** con la regola ferrea sopra, prima di lasciarla nel notebook.
4. **Genera l'output giusto** per il caso (tabella sopra): Deep Research, chat mirata, o uno strumento di Studio.
5. **Estrai in Obsidian**: aggiorna la nota giusta copiando solo i fatti confermati, citando la fonte. Segna sempre esplicitamente cosa è "confermato" e cosa è "da verificare" — mai presentarli allo stesso livello.
6. **Registra l'id del notebook** nella nota del soggetto (tabella "Strumenti di lavoro" o sezione dedicata), così è ritrovabile la volta successiva.
7. **Riapri lo stesso notebook** quando il soggetto torna attivo, invece di crearne uno nuovo — mantiene lo storico e evita di ripetere ricerche già fatte.

## Template collegato

[[Templates/Nota di Ricerca (NotebookLM)]] — da usare per registrare una sessione di ricerca (obiettivo, fonti confermate/scartate, sintesi, cosa resta da verificare).

## Esempio di riferimento

Il notebook "FG Second Brain" (id `901fe146-3107-40e1-a829-f5341934c077`) applicato al profilo di Federico stesso — vedi [[Ricerca - Presenza Online (Federico Gaudino)|Ricerca - Presenza Online]] per il caso completo, incluso l'episodio di pulizia fonti che ha originato la regola ferrea sopra.

Vedi anche [[Processi e Convenzioni]] per il quadro generale del vault.
