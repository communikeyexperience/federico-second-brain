---
data: "2026-07-20"
tipo: sop
tags: [zirconia-core, brain, repository, git, sync]
---

# SOP — Chiusura e Ripresa Sessione (Sync Repository)

## Obiettivo
Mantenere il repository **STUDIO** allineato tra le macchine di Federico (Mac e PC) senza che lui debba ricordare o digitare comandi git. Ai bordi della sessione di lavoro — chiusura e ripresa — l'allineamento avviene in automatico, riconosciuto per intento.

## Trigger — Chiusura
Segnali di intento a chiudere la sessione: "ci vediamo", "chiudo per oggi", "stacco", "vado", "buonanotte", "a domani", "ho finito per oggi" e varianti equivalenti. **Non** il semplice "ciao" usato come saluto informale a inizio o metà conversazione — rischio di falso trigger, in quel caso non fare nulla. In caso di frase ambigua, confermare in una riga prima di agire.

### Procedura di chiusura
1. Verificare lo stato del repository `STUDIO` (`git status`).
2. Se non ci sono modifiche, dirlo e non fare nulla — niente commit vuoti.
3. Se ci sono modifiche: aggiungerle, creare un commit con messaggio descrittivo che riassume il lavoro della sessione (non un messaggio generico), poi push sul branch remoto corrente.
4. Riportare a Federico, in coda al messaggio di saluto, cosa è stato pushato (file coinvolti + messaggio di commit).
5. **Non tocca il brain stesso** — il brain si sincronizza via Obsidian Sync, non Git (vedi [[Processi e Convenzioni]]). Questo comando riguarda solo il codice/contenuti versionati in STUDIO.
6. **Non rigenera l'indice RAG** (`data/vault-index.json`) automaticamente — resta un comando separato, [[SOP - Allineamento Brain-Repository]], perché consuma crediti Voyage AI. Se il brain è cambiato molto durante la sessione, segnalarlo come nota invece di rilanciarlo in automatico. L'indice è comunque escluso dal versionamento (`/data/` è in `.gitignore` — si rigenera per macchina), quindi non serve comunque per l'allineamento del repository.

## Trigger — Ripresa
Segnali di intento a riprendere il lavoro: "buongiorno", "riprendiamo", "bentornato", "rieccomi", "continuiamo da dove eravamo" e varianti equivalenti.

### Procedura di ripresa
1. Verificare lo stato locale del repository `STUDIO` **su questa macchina** (`git status`) — il comando opera sulla macchina in uso in quel momento, Mac o PC, senza bisogno di saperlo esplicitamente in anticipo.
2. Eseguire il pull dal branch remoto corrente.
3. Se il pull ha successo, confermare in una riga cosa è arrivato di nuovo (se rilevante).
4. Se ci sono conflitti o modifiche locali non salvate che bloccano il pull, **fermarsi e segnalarlo** — non forzare (reset, stash automatico) senza che Federico lo chieda esplicitamente.

## Limite fermo
Un push su un repository condiviso ha conseguenze reali — può innescare un deploy se STUDIO risultasse collegato a un servizio di hosting (oggi non risulta configurato localmente, ma non è verificabile con certezza da qui). Se al momento della chiusura ci sono modifiche di codice palesemente a metà o non testate, segnalarlo esplicitamente prima di pushare invece di pushare silenziosamente codice rotto.

## Nota tecnica — limite confermato il 2026-07-20 (aggiornato)
Da una sessione Cowork (cartella montata da remoto) è possibile **creare** file nella cartella montata (es. `.git/`) ma non **cancellarli**. Prima ipotesi era che il problema riguardasse solo i comandi di scrittura (`add`/`commit`); verificato poi che **anche un semplice `git status` da solo ricrea e lascia bloccato `index.lock`**, perché internamente tenta di scrivere e ripulire un lock come ottimizzazione. Non è un processo esterno che blocca (chiudere editor/GUI git sul Mac non risolve): è un limite strutturale di come Cowork accede alla cartella (verosimilmente permessi sandboxed di macOS di tipo "aggiungi" ma non "elimina" su cartelle come Desktop).

**Conseguenza pratica — regola ferma**: da una sessione Cowork su questo repository **non va lanciato alcun comando git**, nemmeno di sola lettura (`status`, e verosimilmente `pull`/`fetch` per lo stesso motivo). Se viene chiesto di chiudere/riprendere la sessione mentre si opera da Cowork su questo repository, segnalare il limite e fermarsi — non verificare nulla con git, perché la verifica stessa lascia il repository in uno stato bloccato che poi richiede una cancellazione manuale del lock da parte di Federico. La chiusura/ripresa automatica reale funziona solo da una sessione Claude Code nativa sul Mac.

## Collegamenti
- [[SOP - Allineamento Brain-Repository]] — comando distinto per l'indice RAG
- [[Processi e Convenzioni]] — perché il brain usa Obsidian Sync e non Git

## Note
