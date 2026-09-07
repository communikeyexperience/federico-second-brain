---
name: allineamento-brain
description: |
  Rigenera l'indice vettoriale RAG del repository STUDIO (data/vault-index.json)
  a partire dal contenuto aggiornato del brain, così che ZirkonIA risponda con
  contesto aggiornato. Comando intenzionale: si attiva riconoscendo l'intento,
  non una stringa di comando fissa.
  Use when: Federico esprime in linguaggio naturale l'intento di
  sincronizzare/aggiornare l'indice — es. "allinea il brain", "allinea il
  repository", "aggiorna l'indice", "sincronizza ZirkonIA/lo Studio",
  "riallinea il brain col repository", "il brain e il repo sono
  disallineati" — o varianti equivalenti nel significato. Non richiede che
  Federico ricordi o digiti il comando esatto (`npm run vault:index`). In
  caso di frase ambigua, confermare in una riga prima di eseguire.
---

# Allineamento Brain-Repository

Fonte umana: `02 Aree/SOP e Procedure/SOP - Allineamento Brain-Repository.md`.

## Prima di tutto: serve davvero l'indice?
L'indice vettoriale serve **solo** con `RAG_PROVIDER=fg-vault-embeddings` in `zirkonia-app/.env.local`. Con il provider di default `fg-vault` (ricerca lessicale locale nel testo del brain) **non c'è nessun indice da rigenerare**: l'app legge il vault dal vivo. In quel caso dirlo e fermarsi. Se invece serve solo riallineare *quale* brain è collegato su questa postazione, il comando è `npm run brains:bootstrap` (vedi [[SOP - Chiusura e Ripresa Sessione (Sync Repository)]]), non questo.

## Procedura operativa (solo per fg-vault-embeddings)
1. **Individuare il percorso del brain per questa postazione**: è il campo per il sistema operativo corrente (`win32`/`darwin`) in `zirkonia-app/brains.config.json`, oppure il `path` del brain attivo in `zirkonia-app/data/active-brain.json` (rigenerato da `npm run brains:bootstrap`). Verificare anche che `VOYAGE_API_KEY` sia presente in `.env.local`. Se un dato manca o è palesemente sbagliato, segnalarlo invece di procedere alla cieca.
2. **Eseguire** `npm run vault:index "<percorso del brain>"` dalla cartella `zirkonia-app` (equivale a `node scripts/build-vault-index.js "<percorso>"`). Passare il percorso come argomento è più affidabile che affidarsi a `.env.local`, che non fissa più `VAULT_PATH`.
3. Lo script legge ricorsivamente tutte le note `.md` del brain (esclude le cartelle di sistema `.obsidian`, `.claude`, `.agents`, `.git`, più `Templates`, `node_modules` e ogni file/cartella che inizia per `.` o per `ELIMINA_`), le invia in batch a Voyage AI (modello `voyage-4`) e scrive `data/vault-index.<slug>.json` — un file per brain, dove `<slug>` deriva dal percorso.
4. **Confermare l'esito**: verificare che `data/vault-index.<slug>.json` risulti aggiornato (data/ora di modifica) e che il conteggio note sia plausibile (non zero — lo script ora si ferma con errore se trova 0 note, così un percorso sbagliato non produce più un indice vuoto in silenzio). Segnalare eventuali errori (chiave mancante, rate limit — il piano gratuito Voyage è limitato, un brain di ~300 note può richiedere diversi minuti).
5. **Non** eseguire `git add`/`commit`/`push` in automatico: `data/` è comunque in `.gitignore` (indice locale per postazione). Un push su un repository condiviso è un'azione a parte, solo se richiesto esplicitamente.

## Limite fermo
Non è un'azione a costo zero: consuma quota Voyage AI e richiede tempo per il rate limit. Eseguirla quando il brain è cambiato in modo sostanziale, non ad ogni modifica minima — se non è cambiato molto dall'ultima esecuzione, segnalarlo invece di rilanciare inutilmente.

## Nota per vault-cliente
Il percorso del brain e il nome del repository cambiano per ogni cliente/postazione — vivono in `brains.config.json`. La logica del comando (intento → individua percorso → esegui script → conferma esito) resta identica.
