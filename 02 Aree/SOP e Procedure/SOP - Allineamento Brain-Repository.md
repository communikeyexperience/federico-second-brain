---
data: "2026-07-20"
tipo: sop
tags: [zirkonia-core, brain, repository, rag, allineamento]
---

# SOP — Allineamento Brain-Repository

## Obiettivo
Rigenerare l'indice vettoriale RAG di ZirkonIA (`zirkonia-app/data/vault-index.<slug>.json`, un file per brain) a partire dal contenuto aggiornato del brain, così che l'app risponda con contesto aggiornato — **senza dover ricordare o digitare il comando esatto** (`npm run vault:index`). Il comando è **intenzionale**: si attiva riconoscendo l'intento espresso in linguaggio naturale, non una stringa fissa.

## Aggiornamento 2026-09-07 — quando NON serve
L'indice vettoriale serve **solo** se `zirkonia-app/.env.local` ha `RAG_PROVIDER=fg-vault-embeddings`. Con il provider di default `fg-vault` (ricerca lessicale locale nel testo del brain) l'app legge il vault dal vivo e **non esiste nessun indice da rigenerare** — in quel caso dirlo e fermarsi. Se invece serve solo riallineare *quale* brain è collegato su questa postazione (es. dopo aver cambiato macchina), il comando è `npm run brains:bootstrap` — vedi [[SOP - Chiusura e Ripresa Sessione (Sync Repository)]] — non questo.

## Trigger (per intento, non parola esatta)
Qualunque frase che esprima l'intento di sincronizzare/aggiornare l'indice, tra cui almeno: "allinea il brain", "allinea il repository", "aggiorna l'indice", "sincronizza ZirkonIA/lo Studio", "riallinea il brain col repository", "il brain e il repo sono disallineati, sistemalo" — e varianti equivalenti nel significato. In caso di frase ambigua (potrebbe intendere altro), confermare in una riga prima di eseguire.

## Procedura operativa (solo per `fg-vault-embeddings`)
1. **Individuare il percorso del brain per questa postazione**: è il campo per il sistema operativo corrente (`win32`/`darwin`) in `zirkonia-app/brains.config.json`, oppure il `path` del brain attivo in `zirkonia-app/data/active-brain.json` (rigenerato da `npm run brains:bootstrap`). Verificare anche che `VOYAGE_API_KEY` sia presente in `.env.local`. Se un dato manca o è palesemente sbagliato, segnalarlo invece di procedere alla cieca. `.env.local` **non** fissa più `VAULT_PATH`.
2. **Eseguire** `npm run vault:index "<percorso del brain>"` dalla cartella `zirkonia-app` (equivale a `node scripts/build-vault-index.js "<percorso>"`). Passare il percorso come argomento è più affidabile che affidarsi all'ambiente.
3. Lo script legge ricorsivamente tutte le note `.md` del brain (esclude le cartelle di sistema `.obsidian`, `.claude`, `.agents`, `.git`, più `Templates`, `node_modules` e ogni file/cartella che inizia per `.` o per `ELIMINA_`), le invia in batch a Voyage AI (modello `voyage-4`) e scrive `data/vault-index.<slug>.json`.
4. **Confermare l'esito**: verificare che `data/vault-index.<slug>.json` risulti aggiornato (data/ora di modifica) e che il conteggio note sia plausibile. Lo script ora **si ferma con errore se trova 0 note**, così un percorso sbagliato (spazi/NBSP finali, cartella errata, permessi) non produce più un indice vuoto in silenzio — era la causa del malfunzionamento diagnosticato il 2026-09-07. Segnalare eventuali errori (chiave mancante, rate limit — il piano gratuito Voyage è limitato, un brain di ~300 note può richiedere diversi minuti).
5. **Non fare in automatico** `git add`/`commit`/`push`: `data/` è comunque in `.gitignore` (indice locale per postazione, si rigenera per macchina). Un push su un repository condiviso è un'azione a parte, solo se richiesto esplicitamente.

## Limite fermo
Non è un'azione a costo zero: consuma quota Voyage AI e richiede tempo per via del rate limit. Va eseguita quando il brain è cambiato in modo sostanziale (nuove note, skill, decisioni importanti), non ad ogni modifica minima — se il brain non è cambiato sostanzialmente dall'ultima esecuzione, segnalarlo invece di rilanciare inutilmente.

## Nota di riuso
Il percorso del brain e il nome del repository cambiano per ogni cliente/postazione — vivono in `zirkonia-app/brains.config.json` (per sistema operativo). La logica del comando (intento → individua percorso → esegui script → conferma esito) resta identica.

## Collegamenti
- [[SOP - Chiusura e Ripresa Sessione (Sync Repository)]] — `brains:bootstrap` e sync git dei due repository
- [[SOP - Recap Stato]] — stesso principio di riconoscimento per intento, non parola esatta
- [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]] — contesto sull'architettura RAG/embeddings

## Note
