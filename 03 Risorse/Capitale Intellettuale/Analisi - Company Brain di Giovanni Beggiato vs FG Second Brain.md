---
tipo: risorsa
tags: [capitale-intellettuale, second-brain, obsidian, ai, metodo]
data: "2026-07-07"
---

# Analisi — "Company Brain" di Giovanni Beggiato vs FG Second Brain

> Basata sulla trascrizione di un video tutorial YouTube di Giovanni Beggiato ("Company Brain — tutorial completo"), caricata da Federico il 2026-07-07. Sintesi e confronto in forma condensata (non riproduzione della trascrizione) — per il contenuto originale vedi il video.

## Fonte
Video YouTube di Giovanni Beggiato, "CORSO COMPLETO SECOND BRAIN 2h: Claude + Obsidian" (pubblicato 11/06/2026, canale con ~8,91K iscritti al momento della visione, ~13k visualizzazioni). URL: https://www.youtube.com/watch?v=RnoC5IlOUhs. Trascrizione integrale (2h18m) analizzata dal player YouTube. Contenuto in parte promozionale per la community a pagamento dell'autore ("Avanguardia Plus") — le soglie numeriche citate (19% tempo perso, soglie 2.500/20.000 note) sono presentate da Beggiato come indicative, non verificate in modo indipendente qui.

## Di cosa parla il video, in breve
Beggiato (fondatore di un'agenzia di consulenza IA, "Gente Sei", e di una community a pagamento) insegna a costruire un "Company Brain": una base di conoscenza aziendale in Obsidian, navigabile da un'IA (Claude), con livelli aggiuntivi per collaborazione visiva (Notion), version control (Git/Google Drive) e, oltre una certa scala, ricerca semantica (RAG su database vettoriali). Tesi di fondo: un'IA generica (ChatGPT "di base") non dà alcun vantaggio competitivo perché tutti — voi e i vostri concorrenti — ottenete le stesse risposte; il vantaggio nasce solo da un contesto proprietario che l'IA può leggere e che nessun altro ha.

## Struttura proposta — le 11 cartelle
Self (identità/missione/clienti/obiettivi) · Areas (reparti/responsabilità continue) · Projects (lavori con inizio-fine) · Inbox/Sources (materiale grezzo) · Concepts (definizioni di termini/metriche specifiche dell'azienda) · Docs (SOP interne) · Entities (persone, prodotti, fornitori, tool) · Data (tabelle, KPI, report) · Code (script, automazioni) · Outputs (deliverable finiti) · Workspace (diario di sessioni/giornate).

Distingue esplicitamente **tassonomia** (come archivi le cose — nel suo caso, per grado di "azionabilità") da **ontologia** (come le colleghi logicamente — è questo che permette all'IA di "ragionare" navigando i link).

## Le linee guida di Beggiato, punto per punto
1. **ROI esplicito prima del "come"** — apre motivando l'investimento: conoscenza aziendale sparsa in 3 posti (chat/mail, testa delle persone — rischio "top performer"/bus factor, tool sparsi) costa ~19% del tempo lavorativo (dato McKinsey citato) cercando informazioni.
2. **Architettura a 11 cartelle fisse, agnostiche al settore**: self, areas, projects, inbox/sources, concepts, docs, entities, data, code, outputs, workspace — organizzate per grado di "azionabilità".
3. **Tassonomia vs ontologia** — la tassonomia è *dove* archiviare (le cartelle), l'ontologia è *come colleghi* le informazioni (wikilink/relazioni); la seconda dà "struttura al ragionamento" per l'IA.
4. **Canon aziendale** — prima di generare qualsiasi nota, l'IA legge tutto il materiale grezzo e produce un documento "Canon" unico (zero fatti inventati, solo quanto risulta dalle fonti), con un piano in 5 righe presentato prima di scrivere. Resta un file di lavoro temporaneo, non una nota finale.
5. **Note atomiche** (riconducibile allo Zettelkasten di Niklas Luhmann): una nota = un'idea, max 300 righe, frontmatter con title/summary/related (min. 3 wikilink).
6. **Hub-and-spoke prima delle note atomiche**: crea prima gli "hub" (nota centrale per cartella/area) e solo dopo spezzetta il materiale, per evitare file orfani creati "a caso".
7. **`_index.md` per cartella**: aggancia sistematicamente le note che altrimenti resterebbero isolate nel grafo — distingue "orfano concettuale" (accettabile) da "orfano nel grafo" (da evitare sempre).
8. **Gate di qualità automatizzato**: script Python che passa ogni nota contro 6 regole — frontmatter completo, max 300 righe, min. 3 wikilink, zero link rotti, zero orfani, una sola componente connessa nel grafo.
9. **`llms.txt`** — indice sintetico derivato (raccomandazione personale, non best practice consolidata) che riassume il contenuto del vault per risparmiare token, più una dashboard testuale `showcase.md` con metriche per audit visivo rapido.
10. **Version control esterno obbligatorio**: Obsidian è "local-first", nessun backup nativo — consiglia GitHub (più solido, scala meglio) o Google Drive (più semplice).
11. **Soglie dimensionali esplicite**: <2.500 note → solo hub + llms.txt; 2.500–20.000 → embeddings/RAG; 20.000+ → pipeline RAG completa con vector DB.
12. **Layer visivo separato dal layer AI**: Obsidian è per l'IA, non per gli umani del team — per quello propone dashboard HTML statiche o integrazione con Notion.
13. **Memoria viva a due livelli**: sessioni (granulari, una per conversazione) che si aggregano in un daily/giornale (riassunto), con skill dedicate inizio sessione / fine sessione / fine giornata.

## Confronto strutturale

| Dimensione | Beggiato (Company Brain) | Noi (FG Second Brain / ZirkonIA) |
|---|---|---|
| Archiviazione | Tassonomia propria a 11 cartelle "AI-first" | **PARA classico** (Inbox → Progetti → Aree → Risorse → Archivio), meno granulare su alcune distinzioni |
| Ontologia / collegamenti | Wikilink + hub obbligatori, gate automatico anti-orfani | Wikilink organici, **nessun hub sistematico né controllo automatico** — gap oggi in chiusura (vedi sotto) |
| Frontmatter | YAML con title/summary/related, enforcement via script | Schema già documentato in [[Processi e Convenzioni]], più maturo sulla semantica per tipo di nota, ora con `summary` aggiunto |
| Note atomiche | Principio esplicito e imposto | Applicato in parte (Glossario Coaching sì, note progetto/area spesso no) |
| Controllo qualità | Script Python automatico | In implementazione oggi (vedi sotto) |
| Indice per l'IA | `llms.txt` + `showcase.md` | CLAUDE.md + Home.md, non quantitativo |
| Version control | GitHub o Google Drive, requisito non opzionale | Deciso oggi: Obsidian Sync (include version history) |
| Skill/SOP comportamentali | Solo journal (equivalente di "recap-stato") | **Più maturo**: 6 skill triggerate per intento + SOP umane parallele |
| Scala e RAG | Soglie esplicite 2.500/20.000 note | Vault ancora piccolo, non si pone il tema |
| Posizionamento business | Corso pubblico + community a pagamento | Stessa direzione (second-brain-as-a-service), più avanti su SOP di dominio (coaching, mediazione soci) |

## Confronto con FG Second Brain (onesto, non solo elogiativo)

**Dove il sistema di Beggiato è oggettivamente più avanti**:
1. **Disciplina delle note atomiche** — è la differenza più concreta e più urgente da guardare. Il tuo vault tende ad avere poche note che *crescono* nel tempo per aggiunte successive (`ZirkonIA.md` è già a 24K caratteri, `Business Experience.md` a 20K, `Persone.md` a 12K) invece di scomporsi in note atomiche collegate. Questo rende più lento sia per me sia per te trovare un dettaglio specifico, e viola il principio "una nota, un'idea" che rende le note riusabili in contesti diversi.
2. **Passaggio "Canon" prima delle note atomiche** — quando carichi una trascrizione lunga (come le interviste EDUCAZIONE), io sintetizzo direttamente in note tematiche, senza un passaggio intermedio esplicito di "estrazione fatti verificati, conferma tua, poi struttura". Nella pratica ho comunque applicato la tua regola di disambiguazione (mai inventare, sempre flaggare l'incerto), ma non è un processo formalizzato e verificabile come il suo.
3. **Campo "summary" nel frontmatter** — il tuo schema attuale (in Processi e Convenzioni) non lo prevede. È un'aggiunta a costo quasi zero con beneficio concreto: mi permette di capire la pertinenza di una nota senza aprirla tutta.
4. **Zero orfani / indice per cartella / audit automatico** — non esiste nulla di equivalente nel tuo vault. Rischio concreto ma oggi contenuto (189 note, non migliaia).
5. **Memoria viva per data** — tu hai il Recap Stato (stato attuale dei progetti aperti), ma non un log per sessione/giornata interrogabile ("cosa ci siamo detti il 3 luglio"). Sono strumenti diversi con scopi diversi, non sovrapponibili.

**Dove il tuo sistema è oggettivamente più avanti (il video non lo copre affatto)**:
1. **Livello comportamentale/protocollo** — le tue SOP/skill (Tono, EDUCAZIONE, Mediazione, Strategia e Visione, Recap Stato) definiscono *come* l'assistente deve comportarsi e ragionare, non solo dove sta la conoscenza. Il tutorial di Beggiato è interamente sulla struttura dei dati — zero contenuto su tono, framework decisionali o persona dell'assistente.
2. **Regola di disambiguazione esplicita** — "mai unire omonimi per assunzione, sempre segnalare l'incerto" non ha equivalente nel suo sistema (che anzi, nella demo, si affida molto alla generazione automatica via prompt, con rischio di errori silenziosi se non controllati).
3. **Punti Aperti come nota dedicata** — non c'è nulla di simile nella sua struttura.
4. **Profondità relazionale/personale** (Persone.md, storie di famiglia, interviste di profilazione) — il suo esempio è un'azienda B2B SaaS fittizia, orientata a KPI/clienti/ricavi. Il tuo vault gestisce anche la dimensione umana, che è un'altra categoria di problema.

**Nota di calibrazione**: Beggiato vende una community/servizio su questo esatto argomento — il video è, in parte, materiale di marketing per la sua offerta (menzioni ricorrenti alla community a pagamento). Questo non invalida il contenuto tecnico (che è solido e coerente con pratiche note, es. Zettelkasten), ma alcune sue raccomandazioni (RAG, database vettoriali) sono pensate per scala aziendale/multi-cliente, non per un vault personale come il tuo.

## Risposta diretta alla domanda "è più performante?"
Non in assoluto — è più **ingegnerizzato per scalare** (pensato per arrivare a 20.000+ note gestite per conto di clienti terzi), mentre il tuo è ottimizzato per un caso d'uso diverso (un'unica persona/gruppo, profondità relazionale, comportamento dell'assistente calibrato). Sulla parte che i due sistemi hanno davvero in comune — l'igiene delle note e la navigabilità del grafo — il suo è più rigoroso, e su quello vale la pena imparare.

## Cosa è stato implementato (decisioni prese il 2026-07-08)
1. **Campo `summary` nel frontmatter** — fatto (vedi [[Processi e Convenzioni]])
2. **Principio "note atomiche" per i nuovi contenuti** — documentato in [[Processi e Convenzioni]]
3. **Passaggio "Canon" per i caricamenti massivi** — documentato in [[Processi e Convenzioni]]
4. **Script di controllo qualità** (6 regole, versione completa) — implementato, vedi [[Processi e Convenzioni]] per come lanciarlo
5. **`_index.md` per ogni cartella** — implementato per l'intero vault
6. **Version control**: deciso di affidarsi a **Obsidian Sync** (già include cronologia versioni + sync multi-device) invece di introdurre Git — coerente con un vault a uso singolo/famiglia, non multi-collaboratore

## Rimandato, non necessario ora
- **Indice leggero `llms.txt`/`showcase.md`** — utile quando il vault crescerà molto di più; CLAUDE.md + Home.md assolvono parzialmente la funzione oggi
- **RAG/database vettoriale** — il vault (189 note) è due ordini di grandezza sotto la soglia in cui inizia a servire

## Collegamenti
[[Processi e Convenzioni]] (schema frontmatter aggiornato con `summary`, principio note atomiche, passaggio Canon, script di audit), [[ZirkonIA]] (parallelismi diretti con il protocollo delle "200 domande" e l'architettura del vault come prodotto)

## Note
Video pubblicato 11/06/2026, canale con 8,91K iscritti al momento della visione (8/07/2026).
