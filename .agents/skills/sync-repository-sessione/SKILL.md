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

## Chiusura — procedura
1. `git status` nel repository STUDIO. Se non ci sono modifiche, dirlo e fermarsi (niente commit vuoti).
2. Se ci sono modifiche: `git add -A`, commit con messaggio descrittivo del lavoro fatto in sessione (non generico), poi `git push` sul branch remoto corrente.
3. Riportare in coda al saluto cosa è stato pushato (file + messaggio di commit).
4. Non tocca il brain (sincronizzato via Obsidian Sync, non Git).
5. Non rigenera `data/vault-index.json` in automatico (comando separato: skill `allineamento-brain`) — è comunque escluso dal versionamento (`/data/` in `.gitignore`, si rigenera per macchina).

## Ripresa — procedura
1. `git status` sul repository STUDIO **della macchina in uso in quel momento** (Mac o PC, senza bisogno di saperlo in anticipo).
2. `git pull` dal branch remoto corrente.
3. Confermare in una riga cosa è arrivato di nuovo, se rilevante.
4. Se ci sono conflitti o modifiche locali non salvate che bloccano il pull: fermarsi e segnalarlo, mai forzare (reset/stash automatico) senza richiesta esplicita.

## Limite fermo
Un push su un repository condiviso ha conseguenze reali (possibile deploy automatico se collegato a un hosting). Se ci sono modifiche di codice palesemente a metà/non testate alla chiusura, segnalarlo esplicitamente prima di pushare.

## Nota tecnica — limite confermato (aggiornato 2026-07-20)
Da una sessione Cowork su questo repository, **NESSUN comando git va eseguito**, nemmeno di sola lettura (`git status` incluso): è stato verificato che anche `git status` da solo ricrea `index.lock` e lo lascia bloccato, perché la cartella montata permette di creare file ma non di cancellarli. Non serve essere in fase di add/commit perché il danno si presenti. Conseguenza operativa: questa skill, se invocata da una sessione Cowork, deve SOLO segnalare il limite a Federico e fermarsi — non deve lanciare alcun comando git di verifica, nemmeno per controllare lo stato. La chiusura/ripresa automatica reale funziona solo da una sessione Codex nativa sul Mac, mai da Cowork su questo repository.
