# FG SECOND BRAIN — istruzioni per Claude Code

Questo è il second brain personale di **Federico Gaudino** (Obsidian vault + PARA), e anche il **caso pilota di [[ZirkonIA]]** — l'azienda "second brain as a service" che Federico sta costruendo. Se questo vault viene copiato/adattato per un cliente reale di ZirkonIA, questo file va aggiornato di conseguenza (vedi nota in fondo).

## All'inizio di ogni sessione

Prima di rispondere a qualunque richiesta operativa, leggi **[[Processi e Convenzioni]]** (`03 Risorse/Sistema/Processi e Convenzioni.md`) — metodo PARA, stati/priorità, schema frontmatter, regole ferme (Fagioli, Coach Academy, linguaggio coaching).

## Skill comportamentali (`.claude/skills/`)

Le 8 modalità operative sono implementate come Claude Code Skill in `.claude/skills/` — Claude Code le scopre in automatico all'apertura di questa cartella e le attiva per intento (non solo parola esatta), senza bisogno di istruzioni manuali:

| Skill | Trigger | Quando si applica |
|---|---|---|
| `zirkonia-core-tone` | *(default)* | Ogni volta che Federico chiede un punto di vista/analisi strategica, non solo esecuzione o ricerca |
| `zirkonia-visual-identity` | "crea la presentazione", "documento brandizzato", deliverable ZirkonIA per clienti | Ogni volta che si produce un documento/presentazione esterno di ZirkonIA (landing, playbook, protocollo, pitch) — palette, tipografia, wordmark provvisorio |
| `educazione` | `EDUCAZIONE`, "modalità educazione", "lancia l'educational" | Federico vuole essere interrogato per consolidare/validare conoscenza nel vault |
| `mediazione` | `MEDIAZIONE` | Conflitti tra soci, disallineamenti di governance, decisioni multi-parte |
| `strategia-visione` | `STRATEGIA`, `VISIONE`, "dove potremmo arrivare" | Esplorazione di scenari di crescita/frontiere, non un conflitto da risolvere |
| `recap-stato` | `RECAP`, `STATO`, "come siamo messi" | Quadro rapido e azionabile dei progetti aperti — solo azioni/stato, niente prosa |
| `federico-voice-writer` | "scrivi come me", testi a firma personale di Federico | Ghostwriting nella voce personale di Federico — non i contenuti brandizzati dei clienti Communikey |
| `allineamento-brain` | "allinea il brain", "aggiorna l'indice", "sincronizza ZirkonIA" | Rigenera `data/vault-index.json` nel repository `STUDIO` dal contenuto aggiornato del brain (comando intenzionale, non stringa fissa) |
| `sync-repository-sessione` | saluti di chiusura ("ci vediamo", "stacco") o ripresa ("buongiorno", "riprendiamo") | Push automatico del repository `STUDIO` alla chiusura sessione, pull automatico alla ripresa — allinea Mac e PC senza comandi git manuali |

Se un trigger è ambiguo (potrebbe essere il nome di un progetto/cliente invece del protocollo), conferma in una riga prima di procedere invece di assumere in silenzio — vale soprattutto per `EDUCAZIONE`, che non va confuso con la nota cliente "Coach Academy Cagliari".

**Skill tecniche aggiuntive (portate qui da `STUDIO/.claude/skills`, 2026-07-31)**: `higgsfield-generate`, `higgsfield-soul-id`, `higgsfield-product-photoshoot`, `higgsfield-marketplace-cards` — wrapper del CLI `higgsfield` per generazione immagini/video/3D/audio via Higgsfield AI. Non sono comportamentali come le 8 sopra, sono strumenti di produzione creativa che Federico usa anche fuori da STUDIO. Copiate qui (non spostate: restano anche in `STUDIO/.claude/skills`) per rendere questo vault un kit autosufficiente, portabile su un'altra macchina senza dipendere dal repo STUDIO.

**Manutenzione — nessuna sincronizzazione automatica**: le note in `02 Aree/SOP e Procedure/` restano la fonte "umana" originale (versionabile, leggibile, modificabile in Obsidian), le Skill in `.claude/skills/` sono la loro controparte eseguibile. Se modifichi una SOP, aggiorna a mano anche la Skill corrispondente (e viceversa) — oggi non c'è alcun meccanismo che le tenga allineate automaticamente.

**Limite di canale**: questo meccanismo vale per sessioni Claude Code aperte in questa cartella (voi, i coach). Il futuro dispositivo fisico di ZirkonIA (nome di lavoro "ZirkonIA Touch", concetto in ridefinizione dal 2026-07-15 — sostituisce il precedente concept "Cube" da scrivania, vedi [[ZirkonIA]] → "Pivot hardware") non passerà da Claude Code e non vedrà queste Skill — per quel canale il contenuto delle SOP va iniettato nel system prompt da un backend dedicato (Modulo B/C, ancora da costruire).

## Dove sta cosa

Parti da **[[Home]]** come dashboard. Struttura PARA: `00 Inbox` (cattura), `01 Progetti` (obiettivo + fine), `02 Aree` (responsabilità continue), `03 Risorse` (clienti, capitale intellettuale, sistema), `04 Archivio`. Dettagli completi in [[Processi e Convenzioni]] — non duplicarli qui.

## Comportamento di default

- Archivia proattivamente nel vault le decisioni prese, le SOP generate, le sintesi di riunioni ("Nodi di Valore") durante conversazioni normali, senza chiedere permesso ogni volta — chiudi il messaggio con un log sintetico delle azioni fatte sui file (vedi addendum in [[SOP - Tono e Stile ZirkonIA Core]]).
- Resta invece a chiedere conferma per decisioni realmente ambigue (scelte strutturali di cartelle/tassonomia) o quando manca un dato necessario.
- **Integrità del grafo, sempre attiva** (vedi [[Processi e Convenzioni]] → "Integrità del grafo — procedura standard"): ogni nota/allegato nuovo va agganciato all'indice della cartella e collegato da almeno una nota; i link verso allegati non-.md includono sempre l'estensione. Se emergono note orfane o allegati scollegati, segnalalo invece di correggere/eliminare in autonomia.
- Su materie fiscali/legali/societarie: opinione strategica sì, ma dichiarata come tale — mai sostituire un professionista abilitato (commercialista, notaio, legale).

## Nota per il delivery a clienti ZirkonIA

Questo file è scritto su misura per il vault personale di Federico (nomi propri, clienti, gerarchia Business Experience). Per un vault-cliente:
- Adatta la tabella dei trigger alle SOP realmente presenti in quel vault (non tutte le 6 SOP di Federico sono rilevanti per un cliente esterno — es. Federico Voice Writer è specifica a lui).
- Sostituisci i riferimenti a "Federico" con il nome del cliente.
- Questo è il punto di partenza naturale per lo **starter kit clonabile** citato nei "Prossimi passi" di [[ZirkonIA]].
