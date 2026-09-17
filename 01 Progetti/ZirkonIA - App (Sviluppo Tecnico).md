---
tipo: progetto
stato: attivo
priorita: alta
cliente: ""
scadenza: ""
percorso_file: "D:\_CLAUDE"
tags: [zirkonia, sviluppo, electron, nextjs, app-desktop]
summary: "Sviluppo tecnico dell'app ZirkonIA (chat + RAG + grafo + dashboard) in D:\_CLAUDE, repo STUDIO — dal 2026-08-06 in corso il packaging come app desktop Windows via Electron."
---

# ZirkonIA — App (Sviluppo Tecnico)

> Questa nota traccia lo sviluppo tecnico dell'applicazione ZirkonIA — distinta dalla parte business/commerciale già documentata in [[ZirkonIA]] e dai quattro pilastri di consegna in [[ZirkonIA - Piano di Consegna (Presentazione, Playbook, Protocollo, Packaging)]]. Il codice **non vive nel vault**: risiede nel repository `STUDIO` (`https://github.com/communikeyexperience/STUDIO.git`), cartella locale `D:\_CLAUDE` — vedi [[Processi e Convenzioni]] → "File esterni al vault" per la regola che impone questo tracciamento.

## Cos'è
Front-end di chat in stile Claude, white-label, interfaccia per un sistema RAG. Stack: Next.js 14 (App Router) + TypeScript + Tailwind CSS. Primo commit del repo: "Primo commit: app ZirkonIA (chat + RAG + grafo + dashboard)". Architettura: il browser parla solo con `/api/chat` (server-side), che fa retrieval RAG + chiama Anthropic in streaming — nessuna API key esposta lato client.

Questo è di fatto il **Modulo B/C** già previsto in [[ZirkonIA]] → "Architettura MVP — accesso multi-device per early user": il backend che serve il "cervello" (skill, tono ZirkonIA Core) da PC/telefono, non solo da sessioni Claude Code legate a un PC.

## Packaging app desktop Windows — in corso (dal 2026-08-06)
Il front-end web viene impacchettato come applicazione desktop nativa per Windows via **Electron**, per una distribuzione installabile senza bisogno che il cliente abbia Node/npm.

**Modifiche in lavorazione** (non ancora committate al 2026-08-06):
- `electron/main.js` — processo principale Electron
- `scripts/prepare-electron-build.js` — copia `public/` e `.next/static/` dentro `.next/standalone/` prima del packaging (il build "standalone" di Next.js non li include automaticamente)
- `next.config.mjs` — aggiunto `output: "standalone"`
- `package.json` — aggiunte dipendenze `electron`, `electron-builder`, `concurrently`, `wait-on`; nuovi script `electron:dev`, `prepare:electron-build`, `dist:win`; config `build` per electron-builder: `appId: com.communikeyexperience.zirkonia`, `productName: "ZirkonIA"`, output in `dist-electron`, target Windows `nsis`

**Stato**: lavoro in corso, non completato — nessun `.exe` ancora generato/testato.

## Dashboard cliente — proposta sistema di livelli/maturità (2026-08-08)
Sessione di ragionamento avviata da Federico sulla dashboard principale (distinta dal grafo, già giudicato di alta qualità): come rappresentare al cliente l'evoluzione del proprio brain su una scala 0-12 mesi, in stile "livelli" ma coerente col posizionamento. Proposta completa, con lessico, soglie e sblocchi ancorati ai derivati reali del prodotto, in [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] — non ancora implementata, solo concept validato lato ragionamento.

## Collegamenti
- [[ZirkonIA]] — area principale, business/prodotto/posizionamento
- [[ZirkonIA - Piano di Consegna (Presentazione, Playbook, Protocollo, Packaging)]]
- [[Strategia - Dashboard Maturità del Brain (Sistema di Livelli)]] — concept per la dashboard, in attesa di sviluppo
- [[ZirkonIA - Dashboard Maturità del Brain (Specifica Tecnica)]] — specifica tecnica pronta per lo sviluppo (formule, schema dati, soglie)
- [[ZirkonIA - Prompt di Implementazione Dashboard Maturità del Brain]] — prompt pronto da incollare, verificato contro lo screenshot reale della dashboard (313 note/133.365 parole/958 collegamenti)
- [[Processi e Convenzioni]] — "File esterni al vault"
