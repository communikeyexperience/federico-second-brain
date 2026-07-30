---
tipo: risorsa
tags: [glossario, sistema, meta]
summary: "Glossario dei termini di sistema, protocollo e metodo usati in questo vault — da leggere e aggiornare liberamente."
---

# Glossario

Tutti i termini tecnici/di metodo usati in questo vault, in un solo posto. Aggiornalo quando ne emerge uno nuovo o quando una definizione ti sembra imprecisa — è pensato per essere letto e corretto da te, non solo da me.

## Struttura e metodo del vault

**PARA** — il metodo di organizzazione delle cartelle: **P**rogetti, **A**ree, **R**isorse, **A**rchivio, più una zona di cattura (Inbox). Vedi [[Processi e Convenzioni]].

**Inbox (00 Inbox)** — cattura grezza, tutto quello che non hai ancora deciso dove mettere. Si smista dopo, non si organizza al momento della cattura.

**Progetto (01 Progetti)** — qualcosa con un obiettivo e una fine, anche se la scadenza non è formale. Se ha "prossimi passi" verso una conclusione, è un progetto.

**Area (02 Aree)** — una responsabilità continua, senza fine (es. Business Experience, Communikey Experience). Non "si completa".

**Risorsa (03 Risorse)** — materiale di riferimento: clienti, capitale intellettuale, template, sistema.

**Archivio (04 Archivio)** — progetti chiusi o in pausa lunga. Si sposta qui, non si cancella mai.

**YAML / frontmatter** — il blocco di testo tra i tre trattini (`---`) in cima a ogni nota. Contiene i metadati (tipo, stato, priorità, tag...) che permettono a Obsidian e a me di filtrare, ordinare e collegare le note senza doverle rileggere tutte ogni volta.

**tipo** (campo frontmatter) — che genere di nota è: `progetto`, `cliente`, `area`, `risorsa`, `sop`, `strategia`, `riunione`, `profilo`, `archivio`, `ricerca`.

**stato** (campo frontmatter, solo progetti) — `attivo` · `in-pausa` · `completato` · `archiviato`.

**priorita** (campo frontmatter, solo progetti) — `alta` · `media` · `bassa`, rivista periodicamente.

**summary** (campo frontmatter, nuovo 2026-07-07) — una riga che riassume il contenuto della nota, utile a capire la pertinenza senza aprirla tutta.

**Nota atomica** — una nota che tratta un solo concetto/argomento, tenuta relativamente breve e collegata alle altre — più facile da riusare in contesti diversi di una nota unica che cresce all'infinito. Concetto ripreso dall'analisi del sistema di Giovanni Beggiato, vedi [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]].

**Wikilink** — il collegamento tra due note scritto tra doppie parentesi quadre, es. `[[Business Experience]]`. È quello che crea la "rete" navigabile del vault, sia per te in Obsidian sia per me.

**Grafo (graph view)** — la rappresentazione visiva di Obsidian di tutte le note e dei loro collegamenti, sotto forma di punti e linee.

## Terminologia AI / Second Brain (dal video di Giovanni Beggiato)
Termini tecnici sull'uso dell'IA per costruire una base di conoscenza, emersi dall'analisi del video di Giovanni Beggiato — vedi [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]] per il confronto completo con il nostro metodo.

**Company Brain** — il nome che Beggiato dà a una base di conoscenza aziendale in Obsidian, navigabile da un'IA, pensata per dare un vantaggio competitivo che un'IA generica (senza contesto proprietario) non può dare.

**Tassonomia** — *dove* archivi le informazioni (la struttura delle cartelle). Nel nostro vault è il PARA (vedi sopra); nel sistema di Beggiato sono le 11 cartelle per grado di "azionabilità".

**Ontologia** — *come* colleghi le informazioni tra loro (wikilink, relazioni) — a differenza della tassonomia, è la parte che dà "struttura al ragionamento" quando un'IA naviga il vault, perché un'IA si muove seguendo i collegamenti, non le cartelle.

**Azionabilità** — il criterio di archiviazione di Beggiato: più un contenuto è pronto per essere usato/eseguito, più si sposta verso cartelle "operative" (nel suo schema: code, outputs) invece che verso l'archivio grezzo.

**Canon** — un passaggio intermedio prima di scrivere le note vere e proprie: l'IA legge tutto il materiale grezzo (trascrizioni, documenti) e produce un unico documento con **solo i fatti verificati**, senza nulla di inventato, che l'umano conferma prima che venga spezzato in note atomiche. Serve a prevenire allucinazioni su materiale lungo. Adattato nel nostro vault, vedi [[Processi e Convenzioni]] (sezione "Passaggio Canon").

**Zettelkasten** — il metodo (di Niklas Luhmann, non nominato esplicitamente da Beggiato ma riconoscibile) su cui si basa il principio di "nota atomica": una nota, un'idea, breve e riutilizzabile in più contesti, invece di documenti lunghi e monolitici. Vedi anche "Nota atomica" sopra.

**Hub-and-spoke** — creare prima le note "hub" (una nota centrale per cartella/area) e solo dopo le note di dettaglio ("foglie") — evita che l'IA generi note scollegate dal grafo mentre lavora.

**Nota orfana** — una nota che nessun'altra nota collega mai (zero wikilink in entrata) — invisibile per un'IA che naviga il vault seguendo solo i collegamenti, anche se il file esiste fisicamente.

**Componente connessa** (teoria dei grafi) — un insieme di note tutte raggiungibili tra loro seguendo i wikilink. L'obiettivo è un solo componente connesso nell'intero vault: se ce ne sono più di uno, ci sono "isole" isolate dal resto.

**Gate di qualità / script di audit** — un controllo automatico (nel nostro caso `03 Risorse/Sistema/audit_vault.py`) che verifica un set di regole fisse (frontmatter completo, lunghezza massima, minimo di wikilink, zero link rotti, zero orfani, un solo componente connesso) e produce un referto, senza correggere nulla da solo — la decisione resta umana.

**`_index.md`** — un file per cartella che collega sistematicamente tutte le note al suo interno, così nessuna resta orfana nel grafo. Nel nostro vault, dove esisteva già un `README.md` introduttivo, l'abbiamo integrato lì invece di duplicare il file.

**`llms.txt`** — un indice sintetico in radice al vault, pensato per riassumere cosa contiene ogni cartella e far risparmiare token all'IA, che altrimenti dovrebbe rileggere tutta la struttura a ogni sessione. Non ancora implementato nel nostro vault (rimandato: utile quando crescerà molto di più).

**`showcase.md`** — una dashboard testuale con metriche del vault (numero di note, wikilink, componenti connesse) per un audit visivo rapido. Non implementato da noi per lo stesso motivo di `llms.txt`.

**Version control (Git/commit/branch)** — trattare il vault come una repository: un *commit* è una fotografia dello stato in un momento preciso, un *branch* è una versione isolata su cui sperimentare senza intaccare quella principale. Nel nostro vault abbiamo scelto Obsidian Sync (che include già cronologia versioni) invece di introdurre Git — vedi [[Processi e Convenzioni]].

**RAG (Retrieval-Augmented Generation)** — tecnica per cui un'IA, invece di leggere tutto il vault, recupera solo i frammenti di testo più pertinenti a una domanda (tramite ricerca semantica) prima di rispondere. Utile solo oltre una certa scala di note (Beggiato indica la soglia dei 2.500+); il nostro vault (196 note) è molto al di sotto.

**Embedding** — la rappresentazione numerica (un vettore) del significato di un testo, usata per confrontare quanto due testi sono semanticamente simili — è il meccanismo su cui si basa la ricerca RAG.

**Database vettoriale** (es. Supabase, Qdrant, Pinecone, Weaviate) — un database pensato per salvare e cercare velocemente tra milioni di embedding — necessario solo quando si costruisce una pipeline RAG completa, su vault molto più grandi del nostro.

**Memoria viva** — un sistema a tre comandi (inizio sessione, fine sessione, fine giornata) per tenere un log delle sessioni di lavoro interrogabile nel tempo ("cosa ci siamo detti il 3 luglio") — diverso dal nostro Recap Stato, che fotografa solo lo stato *attuale* dei progetti aperti, non la storia.

## Il protocollo ZirconIA Core

**ZirconIA Core** — la "persona" con cui opero di default in questo vault: non solo esecutore di task, ma partner che applica strategia, posizionamento, copywriting a quello che c'è nel vault. Vedi [[SOP - Tono e Stile ZirconIA Core]].

**💎 [ZirconIA Log]** — il blocco che chiudo in fondo ai messaggi dove ho modificato/creato file, con l'elenco sintetico delle azioni fatte.

**Nodo di Valore** — una decisione presa, una SOP generata, una sintesi di riunione: il tipo di contenuto che archivio proattivamente nel vault durante le conversazioni normali, senza chiedere permesso ogni volta.

**Angolo Cieco** — nella struttura di risposta standard, il punto in cui segnalo un rischio, un'opportunità nascosta o una domanda scomoda non ancora considerata — anche quando non richiesto esplicitamente.

**SOP** — Standard Operating Procedure, una procedura scritta che descrive come affrontare una situazione ricorrente. Vivono in `02 Aree/SOP e Procedure/` e hanno una controparte eseguibile in `.claude/skills/`.

**Skill** — la versione "eseguibile" di una SOP, in `.claude/skills/`, scoperta automaticamente da Claude Code/Cowork all'apertura della cartella e attivata per intento (non solo parola esatta).

**EDUCAZIONE** — il protocollo con cui, su tuo trigger, ti interrogo per consolidare/validare conoscenza da archiviare nel vault (il flusso si inverte: sei tu a rispondere, non io).

**MEDIAZIONE** — il protocollo per conflitti tra soci, disallineamenti di governance o negoziazioni — usa il framework Posizioni vs Interessi, BATNA, ZOPA, matrice delle opzioni.

**STRATEGIA / VISIONE** — il protocollo per esplorare frontiere di crescita e scenari futuri, ancorati a dati reali del vault.

**RECAP / STATO** — il protocollo che dà un quadro rapido dei soli progetti aperti, in formato "semaforo" (🔴 Task, 🟡 In attesa di altri, 🟢 In corso).

**BATNA** — *Best Alternative to a Negotiated Agreement*: la migliore alternativa che una parte ha se non si trova un accordo. Chi ha il BATNA migliore ha più leva in una trattativa.

**ZOPA** — *Zone of Possible Agreement*: la zona in cui le condizioni accettabili di due parti in trattativa si sovrappongono, se esiste.

## Il gruppo e i progetti di Federico

**La Experience Suite** — il nome del gruppo che comprende tutte le attività di Federico. Oggi solo branding condiviso, holding formale non ancora creata.

**Business Experience** — la società di investimenti immobiliari in Sardegna, verticale "cappello" per l'edilizia/immobiliare del gruppo.

**Communikey Experience** — la società che sviluppa comunicazione, strategia e ricerca (co-fondata con Cristiano Musa), include ZirconIA come progetto tecnologico.

**ZirconIA** — il progetto/prodotto di "second brain as a service": profilazione consulenziale + vault Obsidian su misura + dispositivo fisico (il Cube). Questo stesso vault ne è il caso pilota.

**Cube** — l'interfaccia hardware fisica prevista per ZirconIA, in ceramica zirconia, con interfaccia vocale.

**Case Resilienti** — lo spin-off in fase di concept di Business Experience: case modulari resistenti a disastri, per il mercato USA.

## Framework dai libri letti (Capitale Intellettuale)

**Giusta Causa** — (da *Il Gioco Infinito*, Simon Sinek) una visione di uno stato futuro non ancora esistente, abbastanza affascinante da motivare sacrifici. Deve essere a favore di qualcosa, inclusiva, orientata al servizio, resiliente, idealistica.

**Sfera d'Influenza / Sfera di Coinvolgimento** — (da *Le sette regole per avere successo*, Stephen Covey) la parte di ciò che ci preoccupa su cui possiamo davvero agire, contro tutto ciò che ci preoccupa in generale. Le persone proattive investono energia sulla prima.

**Riprova sociale** — (da *Le armi della persuasione*, Robert Cialdini) la tendenza a decidere cosa è corretto osservando cosa fanno gli altri, soprattutto in condizioni di incertezza.

**Flessibilità esistenziale** — (da *Il Gioco Infinito*) la capacità di cambiare rotta radicalmente quando serve alla causa, anche smantellando ciò che ha già avuto successo.

## Note
Non è un elenco chiuso — aggiungi qui ogni termine che ti risulta poco chiaro o che uso spesso senza definirlo.
