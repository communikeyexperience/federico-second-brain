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

## Procedura operativa
1. Verificare che `STUDIO/.env.local` abbia `VAULT_PATH` puntato alla cartella corretta del brain su questa macchina (`FG second brain mac/WEB FG second brain`) e `VOYAGE_API_KEY` presente. Se manca o è palesemente sbagliato, segnalarlo invece di procedere alla cieca.
2. Eseguire `npm run vault:index` dalla root del repository `STUDIO` (equivalente a `node scripts/build-vault-index.js`).
3. Lo script legge ricorsivamente tutte le note del brain (esclude `.obsidian`, `.claude`, `.git`, `Templates`, `node_modules`, e ogni nota che inizia per `ELIMINA_`), le invia in batch a Voyage AI (modello `voyage-4`) e scrive il risultato in `data/vault-index.json`.
4. Confermare l'esito: verificare che `data/vault-index.json` risulti aggiornato (data/ora di modifica), segnalare eventuali errori (chiave mancante, rate limit — il piano gratuito Voyage è limitato, l'operazione su un brain di ~200 note può richiedere alcuni minuti).
5. Non eseguire `git add`/`commit`/`push` in automatico, anche se il repository ha modifiche da condividere — solo se richiesto esplicitamente. L'indicizzazione locale rigenera un file derivato (rischio contenuto); un push su un repository condiviso ha conseguenze diverse.

## Limite fermo
Non è un'azione a costo zero: consuma crediti/quota Voyage AI e richiede tempo per il rate limit. Eseguirla quando il brain è cambiato in modo sostanziale, non ad ogni modifica minima — se il brain non è cambiato sostanzialmente dall'ultima esecuzione, segnalarlo invece di rilanciare inutilmente.

## Nota per vault-cliente
`VAULT_PATH` e il nome del repository cambiano per ogni cliente — la logica del comando (intento → verifica config → esegui script → conferma esito) resta identica.
