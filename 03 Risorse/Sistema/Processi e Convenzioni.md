---
tipo: risorsa
tags: [sistema, meta]
---

# Processi e Convenzioni

Come funziona questo vault: routine, stati, convenzioni. Se hai un dubbio su "dove metto questa cosa", parti da qui. Per il significato dei singoli termini vedi [[Glossario]].

## Metodo: PARA + Inbox

- **00 Inbox** — cattura grezza, tutto quello che ti passa per la testa. Non organizzare qui, solo butta dentro.
- **01 Progetti** — cose con un obiettivo e una fine (anche se la scadenza non è formale). Se ha dei "prossimi passi", è un progetto.
- **02 Aree** — responsabilità continue, senza fine (conoscenza di coaching, content pipeline, journaling). Non "si completano".
- **03 Risorse** — materiale di riferimento: clienti, template, processi, letture.
- **04 Archivio** — progetti chiusi o in pausa lunga. Si sposta qui, non si cancella.

## Routine di cattura (ogni giorno)

Tutto ciò che arriva — idee, appunti da riunioni, link, cose da approfondire — va nell'**Inbox**, mai direttamente in un progetto o area. Zero attrito: scrivi e basta, smisti dopo.

## Revisione settimanale (15–20 minuti, giorno fisso)

1. Svuota l'Inbox: ogni voce va spostata nel progetto/area giusta, o cancellata se non serve più.
2. Scorri i progetti attivi (vedi [[01 Progetti/Progetti.base|Progetti]]): aggiorna "Prossimi passi", cambia stato se serve.
3. Progetti conclusi o fermi da tempo → sposta la nota in **04 Archivio** e aggiorna `stato: archiviato`.
4. Controlla scadenze vicine e priorità alta.

## Stati progetto (`stato` nel frontmatter)

| Stato | Significato |
|---|---|
| `attivo` | Ci stai lavorando o è nella pipeline a breve |
| `in-pausa` | Fermo in attesa di qualcosa (risposta cliente, materiale, decisione) |
| `completato` | Consegnato, ma tenuto in Progetti per riferimento a breve termine |
| `archiviato` | Chiuso — nota spostata in 04 Archivio |

## Priorità (`priorita` nel frontmatter)

`alta` · `media` · `bassa` — rivista ad ogni revisione settimanale, non è statica.

## Schema frontmatter per tipo di nota

```yaml
# Progetto
tipo: progetto
stato: attivo        # attivo | in-pausa | completato | archiviato
priorita: media       # alta | media | bassa
cliente: "[[Nome Cliente]]"   # vuoto se progetto personale
scadenza: ""          # YYYY-MM-DD, opzionale
percorso_file: ""     # cartella reale in D:\_CLAUDE
tags: []

# Cliente
tipo: cliente
settore: ""
referente: ""
stato_relazione: attivo   # attivo | pausa | concluso
tags: []

# Area / Risorsa / Archivio
tipo: area | risorsa | archivio
tags: []

# Voce di glossario
tipo: glossario
fonte: ""
tags: []

# Ricerca (NotebookLM o altro)
tipo: ricerca
soggetto: ""
notebook_id: ""
data: ""
stato: in-corso   # in-corso | completata
tags: []

# SOP / Procedura
data: ""
tipo: sop
tags: []

# Strategia / Capitale intellettuale
data: ""
tipo: strategia
tags: []

# Riunione
data: ""
tipo: riunione
cliente_o_progetto: ""
tags: []
```

## Campo consigliato — `summary` (aggiunto 2026-07-07)
Da [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]]: ogni nota nuova dovrebbe avere, oltre ai campi già previsti, un campo `summary` nel frontmatter — una riga che riassume di cosa parla la nota. Serve a capire la pertinenza di una nota senza doverla aprire tutta, sia per te scorrendo il vault sia per me quando devo decidere se è rilevante. Non è retroattivo: da applicare alle note nuove, non serve riscrivere quelle esistenti.

```yaml
summary: "Una riga che riassume il contenuto della nota"
```

## Principio — note atomiche, non note che crescono all'infinito (aggiunto 2026-07-07)
Quando possibile, preferire più note piccole e collegate a una nota unica che si allunga per aggiunte successive (è già successo con `ZirconIA.md`, `Business Experience.md`, `Persone.md` — utile per ora, ma da tenere d'occhio). Un segnale che è il momento di scorporare: una nota supera abbondantemente le 200-300 righe e copre più di un argomento distinto.

## Passaggio "Canon" per caricamenti massivi (aggiunto 2026-07-07)
Per trascrizioni lunghe o documenti corposi (nuove interviste EDUCAZIONE, libri, trascrizioni di riunioni lunghe): prima di strutturare in note tematiche, considerare un passaggio intermedio di estrazione dei soli fatti verificati (niente inventato, numeri che quadrano), da confermare prima di procedere — riduce il rischio di errori silenziosi su materiale lungo. Da applicare quando il materiale è particolarmente denso, non come passaggio obbligato sempre.

## Doppia lente per riunioni con parti esterne (aggiunto 2026-07-09)
Nato da un caso reale: la prima sintesi della riunione Coach Academy (Ninni/Cristiano) è risultata centrata quasi solo sui bisogni della controparte esterna (Ninni), sotto-pesando le idee/proposte fatte da Federico e Cristiano dal lato Communikey — non un errore isolato, ma un default strutturale del passaggio "Canon": una trascrizione tende naturalmente a foregrounding la narrazione più esplicita e sequenziale (di solito il "problema" della controparte), mentre i contributi più sparsi/esplorativi della parte Communikey sono più facili da sotto-pesare in una sintesi che privilegia "fatti verificati e decisionali".

Regola: quando si sintetizza una riunione/trascrizione che coinvolge una parte esterna (cliente, collaboratore, partner), applicare sempre **due lenti distinte**, non una sola:
1. i bisogni/la diagnosi della controparte (come già avviene);
2. cosa c'è per **la Experience Suite** — non solo per la singola verticale operativa che gestisce il rapporto (es. Communikey Experience), ma per il gruppo nel suo insieme (Business Experience, Communikey Experience, ZirconIA) — opportunità commerciali, angoli di business, proposte emerse dal lato Suite durante la riunione. Precisare comunque quale verticale eseguirebbe concretamente, quando è rilevante.

Se la lente 2 non produce nulla di rilevante, va dichiarato esplicitamente ("nessuna opportunità per la Suite identificata in questa riunione"), non semplicemente omesso — per evitare sia il bias opposto (inventare opportunità dove non ce ne sono) sia la ricaduta nel bias originale (ometterle di default). Vedi applicazione in [[Coach Academy - Riunione con Ninni e Cristiano (2026-07-03)]].

## Indice per cartella — `_index.md` / `README.md` (aggiunto 2026-07-08)
Ogni cartella del vault ha un file che collega sistematicamente tutte le note al suo interno (`_index.md`, o `README.md` dove esisteva già come introduzione alla cartella) — evita che una nota resti "orfana nel grafo" (mai raggiungibile da nessun altro punto del vault). Se crei una nota nuova in una cartella, aggiungila anche all'indice di quella cartella (o rilancia lo script di audit, che segnala le note orfane da agganciare — non le aggancia da solo).

## Script di audit qualità (aggiunto 2026-07-08)
`03 Risorse/Sistema/audit_vault.py` — controlla 6 cose in automatico: frontmatter con campo `tipo`, note troppo lunghe (>300 righe, solo avviso), minimo 3 wikilink in uscita (esclude Glossario Coaching e Templates, che sono note atomiche per design), zero link rotti, zero note orfane, un solo grafo connesso. Non corregge nulla da solo — produce un referto in italiano da leggere. Per lanciarlo (serve Python 3, già presente in un ambiente di sviluppo):
```
python3 "03 Risorse/Sistema/audit_vault.py"
```
Nato dal confronto con il metodo di Giovanni Beggiato, vedi [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]].

## Version control (deciso 2026-07-08)
Il vault si affida a **Obsidian Sync** (piano a pagamento) invece che a Git: include già cronologia versioni, sync multi-device e crittografia, senza richiedere disciplina di commit separata — coerente con un vault a uso singolo/famiglia, non multi-collaboratore. Se in futuro ZirconIA gestirà vault-cliente con più collaboratori tecnici, rivalutare Git per quei casi specifici (lo starter kit clonabile lo lascia come opzione documentata, non imposta).

## Convenzioni di naming

- Note progetto: `Nome Progetto - Descrizione breve.md` (es. `Fagioli - Blog Ristorazione.md`)
- Note cliente: nome proprio o ragione sociale, senza abbreviazioni (es. `Centro Dentale 2EMME.md`)
- Voci di glossario: il termine esatto, niente prefissi — vivono come note atomiche in `02 Aree/Coaching - Conoscenza/Glossario/`
- Tag: minuscolo, con trattini al posto degli spazi (es. `blog-ristorazione`, non `Blog Ristorazione`)

## Regole ferme (da non dimenticare mai)

Regole operative raccolte dai singoli progetti, centralizzate qui perché non si perdano:

- **Fagioli**: mai toccare le featured image degli articoli.
- **Coach Academy**: il "Coach Academy BOOK" è materiale INTERNO per gli studenti, non un blog pubblico. Il blog per la scuola è un progetto separato, ancora da proporre.
- **Coaching, linguaggio**: il coach *supporta / accompagna / sostiene*, mai *aiuta / guida / suggerisce* (quei verbi vanno bene per un ruolo di mentor o consulente, non di coach).
- **File di lavoro (PDF, DOCX, XLSX, ecc.)**: salvare sempre direttamente nella cartella del vault (percorso corretto in PARA), mai lasciarli solo nella cartella temporanea di lavoro dell'agente.

## ZirconIA Core — archiviazione in background

Durante le conversazioni normali (non solo nelle sessioni di lavoro strutturato), i "Nodi di Valore" — decisioni prese, SOP generate, idee di business strutturate, sintesi di riunioni — vengono salvati proattivamente nel vault, senza chiedere il permesso ogni volta. Ogni messaggio in cui questo succede si chiude con un log sintetico delle azioni fatte sui file.

**Mappatura tassonomia → cartelle PARA** (per restare coerenti con la struttura già esistente, senza creare alberi paralleli):

| Categoria concettuale | Cartella reale nel vault |
|---|---|
| Progetti (scadenza definita) | `01 Progetti` |
| Aree aziendali / procedure (HR, admin, marketing trasversale) | `02 Aree/SOP e Procedure` — o direttamente nell'area specifica se pertinente a una sola (es. [[Business Experience]]) |
| Capitale intellettuale (modelli mentali, prompt, strategie) | `03 Risorse/Capitale Intellettuale` |
| Ecosistema (clienti, partner, fornitori) | `03 Risorse/Clienti` (il nome della cartella resta "Clienti" per non rompere i link esistenti, ma ospita anche partner/fornitori) |
| Non sicuro dove metterlo | `00 Inbox` |

## Strumenti esterni collegati

- `D:\_CLAUDE` — cartella di lavoro locale sul PC: sorgenti, script, export dei progetti.
- **NotebookLM** — un notebook per cliente/progetto/persona (gli ID sono annotati nelle rispettive note). Processo dettagliato: [[Processo - Ricerca con NotebookLM]].
- **Canva** — produzione grafica caroselli e social.
- **WordPress** (Elementor + Yoast) — pubblicazione blog clienti.

Vedi anche [[Federico Gaudino]] per il quadro d'insieme e [[Home]] come punto di partenza operativo.
