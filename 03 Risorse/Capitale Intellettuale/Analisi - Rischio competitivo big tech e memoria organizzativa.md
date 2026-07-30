---
tipo: risorsa
tags: [zirconia, business, analisi-mercato, competitor]
---

# Analisi — Rischio competitivo: big tech e memoria organizzativa

> Nata da una domanda diretta di Federico (2026-07-13/14), a seguito di un'analisi di mercato con roadmap strategica in cui è emerso come rischio concreto: se Microsoft Copilot, Google Gemini, ChatGPT integrano la memoria organizzativa in modo importante, ZirconIA viene tagliato fuori dal mercato o resta uno spazio di differenziazione?

## Stato reale della minaccia (verificato via ricerca, luglio 2026)
Non è ipotetica, è già in corso e in accelerazione parallela su tutti e tre i principali vendor:

- **Microsoft Copilot Memory**: generalmente disponibile da luglio 2025, attiva di default. Roadmap Microsoft 365 prevede un'espansione (personalizzazione basata su work data) con disponibilità generale target **novembre 2026**.
- **Google Gemini Enterprise**: "Memory Bank" + "Memory Profiles" per contesto long-term cross-sessione; funzione "Projects" crea memoria di team persistente che sopravvive al turnover delle persone; si aggancia a Outlook/OneDrive per estrarre insight da email, calendario, documenti.
- **ChatGPT**: Memory in rollout su piani Enterprise e Team (già su Plus/Pro/Business), con controlli admin per governance/retention.

## Perché non è "o dentro o fuori" — la differenza è nel percorso, non nell'esistenza della memoria
La memoria big tech è **passiva e incidentale**: si accumula come sottoprodotto dell'uso quotidiano di un tool per fare altro (scrivere email, generare documenti), pescando frammenti sparsi. Nessuno chiede attivamente al piccolo imprenditore qual è il suo processo decisionale tacito, chi sono le persone chiave, cosa è già successo in passato — e da solo, un imprenditore non produce spontaneamente quella mappa usando Gemini per due anni.

Il protocollo ZirconIA delle 200 domande è l'opposto: **estrazione deliberata**, non accumulo passivo. Stesso principio già emerso nel frame "C-suite personale" del 2026-07-11 (le persone non falliscono gli obiettivi perché il metodo non esiste, ma perché nessuno le tiene sul percorso) applicato ora alla memoria stessa: la capacità tecnica di ricordare esiste già nei tool big tech, manca chi guida il piccolo imprenditore a costruirla bene.

**Altre tre differenze strutturali, non solo di posizionamento marketing**:
1. **Portabilità del dato**: il vault ZirconIA è file markdown reali, posseduti dal cliente, esportabili e leggibili fuori da qualunque abbonamento. La Memory di Copilot/Gemini/ChatGPT resta dentro la piattaforma del vendor — non è un asset portabile se il cliente cambia fornitore.
2. **Layer di skill interconnesse, non solo memoria** — precisazione tecnica (2026-07-15): ZirconIA **non è un database vettoriale** (nessun RAG/embedding — il vault è testo semplice, letto per intero da un modello; RAG/vettoriale servirebbe solo oltre le 2.500+ note, questo vault ne ha meno di 200, vedi [[Glossario]]). Il vantaggio reale non è *come* è indicizzata la memoria, ma il layer separato di skill comportamentali (maieutica, "doppia lente", recap operativo, tono) che dice al modello *come* ragionare sui dati, non solo cosa ricordare. Copilot/Gemini hanno la memoria (i fatti) ma non un equivalente layer di comportamento codificato sopra — restano un LLM generico che ha letto le tue email, non un sistema con un metodo. Da tenere fermo: oggi questo layer di skill vive solo dentro sessioni Claude Code, non ancora nel canale telefono/dispositivo fisico (vedi [[ZirconIA]] → "Architettura MVP") — va ricostruito lì per reggere alla prova con un prospect tecnico.
3. **Delivery come relazione umana**: profilazione, coach, dispositivo fisico dedicato (concetto in ridefinizione, vedi [[ZirconIA]] → "Pivot hardware") — non un toggle in un menu impostazioni. Rende il modello non scalabile come un SaaS puro, ma anche molto più difficile da replicare a colpi di changelog trimestrale da parte di un vendor big tech.

## Angolo cieco — nessuno di questi argomenti è una barriera permanente
- Gemini Enterprise con "Projects" sta già andando oltre la semplice memoria verso agenti che ragionano su quella memoria. Se big tech costruisce una "persona coach" sopra il proprio layer di memoria, anche lo strato maieutico di ZirconIA rischia erosione nel tempo, non solo la memoria grezza.
- L'argomento "targettizziamo il piccolo imprenditore, loro no" va preso con cautela: molte PMI usano già Microsoft 365 Business o Google Workspace Business. Non è la dimensione dell'azienda a proteggere ZirconIA — è che quasi nessun piccolo imprenditore, da solo, configura quella memoria in un sistema strategico coerente senza essere guidato. **Il moat reale è la delivery del metodo, non l'esistenza della capacità tecnica** — va difeso attivamente, non dato per acquisito.
- Coerenza da verificare quando si disegnerà il Modulo B/C (vedi [[ZirconIA]] → "Architettura MVP"): se diventa un backend proprietario poco ispezionabile, l'argomento "i tuoi dati restano tuoi, portabili" si indebolisce.

## Collegamenti
[[ZirconIA]] (posizionamento, decisione coaching permanente, frame C-suite personale, architettura MVP)
