---
data: "2026-07-22"
tipo: capitale-intellettuale
tags: [zirkonia, anthropic, tos, account, modello-di-business]
---

# Analisi — Modello di gestione account AI per i clienti ZirkonIA

## Il bivio
Nel piano di beta testing ([[ZirkonIA - Piano Beta Testing e Cronoprogramma Matteo]]), Federico ha posto una domanda di fondo: i clienti/beta tester devono aprire e gestire da soli i propri account Claude/Claude Code, oppure Communikey può aprirli e "darli in gestione" dietro una quota mensile, semplificando l'esperienza per un target che ha bassa familiarità tecnologica (coerente con l'ICP dichiarato di ZirkonIA)?

## Cosa dicono i Termini di Servizio di Anthropic (verificato 2026-07-22)
Dai **Consumer Terms of Service** (anthropic.com/legal/consumer-terms, versione effettiva 8 ottobre 2025):

> "You may not share your Account login information, Anthropic API key, or Account credentials with anyone else. You also may not make your Account available to anyone else."

E tra gli usi vietati dei Servizi:

> "To develop any products or services that compete with our Services, including to develop or train any artificial intelligence or machine learning algorithms or models or resell the Services."

**Conclusione diretta**: la versione "informale" del modello B — Communikey apre un account Claude/Claude Code a proprio nome e lo rende disponibile a un cliente pagante — è **esplicitamente vietata** dai Termini consumer. Non è un'area grigia da valutare, è scritta nero su bianco. Un account così userebbe rischierebbe la sospensione.

## La via che invece esiste
I Termini Commerciali (Commercial Terms of Service, per chi usa API key/Console) permettono esplicitamente di costruire prodotti e servizi che "power" (alimentano) prodotti offerti ai propri clienti finali — è la base legale di modelli come "Powered by Claude" e del programma Claude Partner Network / Service Partners che Anthropic stessa promuove per agenzie e system integrator.

**Traduzione pratica per ZirkonIA**: la domanda giusta non è "chi possiede l'account Claude.ai", ma "ZirkonIA è un prodotto proprio costruito sopra l'API (percorso legittimo e scalabile), o è gente che si passa un login di Claude.ai/Claude Code (vietato)?". La prima strada coincide, non a caso, con quanto già ipotizzato in [[ZirkonIA]] → "Architettura MVP — accesso multi-device per early user": un backend (Modulo B/C) che legge il vault, inietta il system prompt/skill, chiama l'API Claude e scrive le risposte nel vault — lì il cliente non ha mai bisogno di un proprio account Claude.ai, perché non ne vede uno: usa l'interfaccia di ZirkonIA.

## Implicazione per la fase attuale (beta tester)
Per Matteo e i primi beta tester, il Modulo B/C via API non esiste ancora (è un "prossimo passo" aperto). Nel frattempo, l'unica strada compatibile con i Termini è: **ogni beta tester apre il proprio account Claude/Claude Code, a proprio nome** — Communikey può ridurre l'attrito facendolo insieme a loro nella stessa sessione di intervista/onboarding (non un problema di regole, solo di assistenza pratica), ma l'account resta legalmente suo.

L'idea di "account gestiti da noi a canone" resta valida come traguardo, ma richiede di costruire prima il Modulo B/C sull'API commerciale — non è qualcosa che si può improvvisare oggi con account consumer.

## Collegamenti
- [[ZirkonIA - Piano Beta Testing e Cronoprogramma Matteo]]
- [[ZirkonIA]]
- [[Punti Aperti]]

Fonti: [Anthropic — Consumer Terms of Service](https://www.anthropic.com/legal/consumer-terms), [Anthropic — Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), [Claude — Service Partners](https://claude.com/partners/services), [Claude — Powered by Claude](https://claude.com/partners/powered-by-claude).
