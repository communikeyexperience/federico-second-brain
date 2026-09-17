---
name: sync-repository-sessione
description: |
  Allinea il repository STUDIO tra le macchine di Federico (Mac/PC) ai bordi
  della sessione di lavoro: push automatico alla chiusura, pull automatico
  alla ripresa. Comando intenzionale, riconosciuto dai saluti/segnali di
  chiusura o ripresa, non da una stringa fissa.
  Use when (CHIUSURA): Federico esprime l'intento di chiudere la sessione —
  "ci vediamo", "chiudo per oggi", "stacco", "vado", "buonanotte", "a
  domani", "ho finito per oggi" o equivalenti. NON il semplice "ciao" usato
  come saluto informale a inizio/metà conversazione.
  Use when (RIPRESA): Federico esprime l'intento di riprendere il lavoro —
  "buongiorno", "riprendiamo", "bentornato", "rieccomi", "continuiamo da
  dove eravamo" o equivalenti.
---

# Sync Repository — Chiusura e Ripresa Sessione

Fonte umana: `02 Aree/SOP e Procedure/SOP - Chiusura e Ripresa Sessione (Sync Repository).md`.

## Due repository git da tenere allineati fra Mac e PC
- **Vault / brain** — `D:\FG SECOND BRAIN` (Windows) o il percorso Mac equivalente → `communikeyexperience/federico-second-brain`. Contenuto vero: note, SOP, allegati, decisioni. Sincronizzato **sia via git sia via Obsidian Sync**: git è il canale di riferimento ai bordi sessione, Obsidian Sync è la ridondanza continua.
- **STUDIO** — `D:\_CLAUDE` → `communikeyexperience/STUDIO`. Codice dell'app ZirkonIA (`zirkonia-app/`) e altro materiale di lavoro.

`zirkonia-app/data/` **non** è versionato (`.gitignore`): registro brain, brain attivo e indici RAG sono locali per postazione (i percorsi del vault sono diversi Windows/Mac). Si rigenerano da `zirkonia-app/brains.config.json` — questo sì versionato — con `npm run brains:bootstrap`.

## Chiusura — procedura
Per **ciascuno** dei due repository (prima il vault, poi STUDIO):
1. `git status`. Se non ci sono modifiche, dirlo e passare all'altro repo — niente commit vuoti.
2. Se ci sono modifiche: `git add -A`, commit con messaggio descrittivo del lavoro fatto in sessione (non generico), poi `git pull` per integrare il remoto e infine `git push` sul branch remoto corrente. Se il pull dà conflitti: fermarsi e segnalarlo, non forzare.
3. Riportare in coda al saluto, **separatamente per i due repo**, cosa è stato committato/pushato (file + messaggio di commit). Anche "nulla da salvare" va dichiarato per entrambi.

Non rigenerare l'indice RAG in automatico: è un comando a parte ([[SOP - Allineamento Brain-Repository]]) e serve **solo** se `.env.local` usa `RAG_PROVIDER=fg-vault-embeddings`. Con il provider di default `fg-vault` (ricerca lessicale locale nel testo del brain) non c'è nessun indice da mantenere.

## Ripresa — procedura
1. Per **ciascuno** dei due repository (vault e STUDIO), sulla macchina in uso in quel momento (Mac o PC, senza saperlo in anticipo): `git status`, poi `git pull` dal branch remoto corrente.
2. In `zirkonia-app`: `npm run brains:bootstrap`. Riallinea `data/brains.json` e `data/active-brain.json` ai percorsi di questa postazione letti da `brains.config.json`. È idempotente: se il registro locale è già coerente non cambia nulla.
3. Verificare dall'output di bootstrap che il brain attivo punti a una cartella esistente e valida. Se `brains.config.json` non ha il percorso per il sistema operativo corrente (`win32`/`darwin`), compilarlo, committarlo e rilanciare bootstrap.
4. Se l'indice del brain attivo manca o è vuoto **e** `.env.local` ha `RAG_PROVIDER=fg-vault-embeddings`: segnalarlo (serve [[SOP - Allineamento Brain-Repository]]), non ricostruirlo di iniziativa.
5. Confermare in una riga cosa è arrivato di nuovo per ciascun repo, se rilevante.
6. Conflitti o modifiche locali non salvate che bloccano un pull: fermarsi e segnalarlo, mai forzare (reset/stash automatico) senza richiesta esplicita.

## Limite fermo
Un push su un repository condiviso ha conseguenze reali (possibile deploy automatico se collegato a un hosting). Se al momento della chiusura ci sono modifiche di codice palesemente a metà o non testate in `zirkonia-app`, segnalarlo esplicitamente prima di pushare.

## Nota tecnica — limite confermato (aggiornato 2026-07-20)
Da una sessione Cowork (cartella montata da remoto) su questi repository, **NESSUN comando git va eseguito**, nemmeno di sola lettura (`git status` incluso): è stato verificato che anche `git status` da solo ricrea `index.lock` e lo lascia bloccato, perché la cartella montata permette di creare file ma non di cancellarli. Conseguenza operativa: questa skill, se invocata da una sessione Cowork, deve SOLO segnalare il limite a Federico e fermarsi — non deve lanciare alcun comando git di verifica. La chiusura/ripresa automatica reale funziona solo da una sessione Codex nativa (Mac o PC).
