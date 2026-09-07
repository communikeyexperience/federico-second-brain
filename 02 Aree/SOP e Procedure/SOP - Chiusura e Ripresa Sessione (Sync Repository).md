---
data: "2026-07-20"
tipo: sop
tags: [zirkonia-core, brain, repository, git, sync]
---

# SOP — Chiusura e Ripresa Sessione (Sync Repository)

## Obiettivo
Mantenere allineati tra le macchine di Federico (Mac e PC) i **due** repository git del sistema, senza che lui debba ricordare o digitare comandi git. Ai bordi della sessione — chiusura e ripresa — l'allineamento avviene in automatico, riconosciuto per intento.

## I due repository
- **Vault / brain** — `D:\FG SECOND BRAIN` (Windows) o il percorso Mac equivalente → `communikeyexperience/federico-second-brain`. Contenuto vero: note, SOP, allegati, decisioni. Sincronizzato **sia via git sia via Obsidian Sync** (aggiornamento 2026-09-07: prima questa SOP diceva "solo Obsidian Sync"). Git è il canale di riferimento ai bordi sessione; Obsidian Sync è la ridondanza continua durante il lavoro.
- **STUDIO** — `D:\_CLAUDE` → `communikeyexperience/STUDIO`. Codice dell'app ZirkonIA (`zirkonia-app/`) e altro materiale di lavoro.

`zirkonia-app/data/` **non** è versionato (`/data/` in `.gitignore`): registro brain, brain attivo e indici RAG sono locali per postazione, perché il percorso del vault è diverso tra Windows e Mac. Si rigenerano da `zirkonia-app/brains.config.json` — questo **sì** versionato — con `npm run brains:bootstrap`.

## Trigger — Chiusura
Segnali di intento a chiudere la sessione: "ci vediamo", "chiudo per oggi", "stacco", "vado", "buonanotte", "a domani", "ho finito per oggi" e varianti equivalenti. **Non** il semplice "ciao" usato come saluto informale a inizio o metà conversazione — rischio di falso trigger, in quel caso non fare nulla. In caso di frase ambigua, confermare in una riga prima di agire.

### Procedura di chiusura
Per **ciascuno** dei due repository (prima il vault, poi STUDIO):
1. `git status`.
2. Se non ci sono modifiche, dirlo e passare all'altro repo — niente commit vuoti.
3. Se ci sono modifiche: `git add -A`, commit con messaggio descrittivo che riassume il lavoro della sessione (non un messaggio generico), poi `git pull` per integrare il remoto e infine `git push` sul branch remoto corrente. Se il pull dà conflitti: fermarsi e segnalarlo, non forzare.
4. Riportare a Federico, in coda al messaggio di saluto, cosa è stato committato/pushato **separatamente per i due repo** (file coinvolti + messaggio di commit). Anche "nulla da salvare" va dichiarato per entrambi.
5. **Non rigenerare l'indice RAG** automaticamente — resta un comando separato, [[SOP - Allineamento Brain-Repository]], e serve **solo** se `.env.local` usa `RAG_PROVIDER=fg-vault-embeddings`. Con il provider di default `fg-vault` (ricerca lessicale locale) non c'è alcun indice da mantenere. Se il brain è cambiato molto e si usa embeddings, segnalarlo come nota invece di rilanciarlo in automatico.

## Trigger — Ripresa
Segnali di intento a riprendere il lavoro: "buongiorno", "riprendiamo", "bentornato", "rieccomi", "continuiamo da dove eravamo" e varianti equivalenti.

### Procedura di ripresa
1. Per **ciascuno** dei due repository (vault e STUDIO), sulla macchina in uso in quel momento (Mac o PC, senza saperlo in anticipo): `git status`, poi `git pull` dal branch remoto corrente.
2. In `zirkonia-app`: `npm run brains:bootstrap`. Riallinea `data/brains.json` e `data/active-brain.json` ai percorsi di questa postazione letti da `brains.config.json`. È idempotente.
3. Verificare dall'output di bootstrap che il brain attivo punti a una cartella esistente e valida. Se `brains.config.json` non ha il percorso per il sistema operativo corrente (`win32`/`darwin`), compilarlo, committarlo e rilanciare bootstrap.
4. Se l'indice del brain attivo manca o è vuoto **e** `.env.local` ha `RAG_PROVIDER=fg-vault-embeddings`: segnalarlo (serve [[SOP - Allineamento Brain-Repository]]), non ricostruirlo di iniziativa.
5. Confermare in una riga cosa è arrivato di nuovo per ciascun repo (se rilevante).
6. Se ci sono conflitti o modifiche locali non salvate che bloccano un pull, **fermarsi e segnalarlo** — non forzare (reset, stash automatico) senza che Federico lo chieda esplicitamente.

## Limite fermo
Un push su un repository condiviso ha conseguenze reali — può innescare un deploy se STUDIO risultasse collegato a un servizio di hosting (oggi non risulta configurato localmente, ma non è verificabile con certezza da qui). Se al momento della chiusura ci sono modifiche di codice palesemente a metà o non testate in `zirkonia-app`, segnalarlo esplicitamente prima di pushare invece di pushare silenziosamente codice rotto.

## Nota tecnica — limite confermato il 2026-07-20 (aggiornato)
Da una sessione Cowork (cartella montata da remoto) è possibile **creare** file nella cartella montata (es. `.git/`) ma non **cancellarli**. Prima ipotesi era che il problema riguardasse solo i comandi di scrittura (`add`/`commit`); verificato poi che **anche un semplice `git status` da solo ricrea e lascia bloccato `index.lock`**, perché internamente tenta di scrivere e ripulire un lock come ottimizzazione. Non è un processo esterno che blocca (chiudere editor/GUI git sul Mac non risolve): è un limite strutturale di come Cowork accede alla cartella (verosimilmente permessi sandboxed di macOS di tipo "aggiungi" ma non "elimina" su cartelle come Desktop).

**Conseguenza pratica — regola ferma**: da una sessione Cowork su questi repository **non va lanciato alcun comando git**, nemmeno di sola lettura (`status`, e verosimilmente `pull`/`fetch` per lo stesso motivo). Se viene chiesto di chiudere/riprendere la sessione mentre si opera da Cowork, segnalare il limite e fermarsi — non verificare nulla con git, perché la verifica stessa lascia il repository in uno stato bloccato che poi richiede una cancellazione manuale del lock da parte di Federico. La chiusura/ripresa automatica reale funziona solo da una sessione Claude Code / Codex nativa (Mac o PC).

## Collegamenti
- [[SOP - Allineamento Brain-Repository]] — comando distinto per l'indice RAG (solo `fg-vault-embeddings`)
- [[Processi e Convenzioni]] — convenzioni generali del vault

## Note
