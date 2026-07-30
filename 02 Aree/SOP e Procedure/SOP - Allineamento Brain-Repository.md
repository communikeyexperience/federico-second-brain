---
data: "2026-07-20"
tipo: sop
tags: [zirconia-core, brain, repository, rag, allineamento]
---

# SOP — Allineamento Brain-Repository

## Obiettivo
Rigenerare l'indice vettoriale del repository **STUDIO** (`data/vault-index.json`) a partire dal contenuto aggiornato del brain, così che ZirkonIA (l'app di chat/RAG in `STUDIO`) risponda con contesto aggiornato — **senza dover ricordare o digitare il comando esatto** (`npm run vault:index`). Il comando è **intenzionale**: si attiva riconoscendo l'intento espresso in linguaggio naturale, non una stringa fissa.

## Trigger (per intento, non parola esatta)
Qualunque frase che esprima l'intento di sincronizzare/aggiornare l'indice, tra cui almeno: "allinea il brain", "allinea il repository", "aggiorna l'indice", "sincronizza ZirkonIA/lo Studio", "riallinea il brain col repository", "il brain e il repo sono disallineati, sistemalo" — e varianti equivalenti nel significato. In caso di frase ambigua (potrebbe intendere altro), confermare in una riga prima di eseguire.

## Procedura operativa
1. **Verificare la configurazione**: `STUDIO/.env.local` deve avere `VAULT_PATH` puntato alla cartella corretta del brain su questa macchina (`FG second brain mac/WEB FG second brain`) e `VOYAGE_API_KEY` presente. Se manca o è palesemente sbagliato, segnalarlo invece di procedere alla cieca.
2. **Eseguire** `npm run vault:index` dalla root del repository `STUDIO` (equivalente a `node scripts/build-vault-index.js`).
3. Lo script legge ricorsivamente tutte le note del brain (esclude `.obsidian`, `.claude`, `.git`, `Templates`, `node_modules`, e ogni nota che inizia per `ELIMINA_`), le invia in batch a Voyage AI (modello `voyage-4`) e scrive il risultato in `data/vault-index.json`.
4. **Confermare l'esito**: verificare che `data/vault-index.json` risulti aggiornato (data/ora di modifica), e segnalare eventuali errori (chiave mancante, rate limit — il piano gratuito Voyage è limitato, l'operazione su un brain di ~200 note può richiedere alcuni minuti).
5. **Non fare in automatico**: se il repository ha modifiche da condividere (es. l'indice va committato/pushato su GitHub per un deploy), non eseguire `git add`/`commit`/`push` senza che sia l'intento esplicito del messaggio — l'indicizzazione locale è a rischio contenuto (rigenera un file derivato), un push su un repository condiviso è un'azione con conseguenze diverse.

## Limite fermo
Non è un'azione a costo zero: consuma crediti/quota Voyage AI e richiede tempo per via del rate limit. Va eseguita quando il brain è cambiato in modo sostanziale (nuove note, skill, decisioni importanti), non ad ogni modifica minima — se il brain non è cambiato sostanzialmente dall'ultima esecuzione, segnalarlo invece di rilanciare inutilmente.

## Nota di riuso
Nello starter kit clonabile per un vault-cliente, `VAULT_PATH` e il nome del repository cambiano — la logica del comando (intento → verifica config → esegui script → conferma esito) resta identica.

## Collegamenti
- [[SOP - Recap Stato]] — stesso principio di riconoscimento per intento, non parola esatta
- [[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]] — contesto sull'architettura RAG/embeddings

## Note
