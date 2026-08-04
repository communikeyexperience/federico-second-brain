---
data: "2026-08-04"
tipo: sop
tags: [zirkonia-core, identita-visiva, branding, template, sop]
---

# SOP — Identità Visiva ZirkonIA

## Obiettivo
Da oggi (2026-08-04), ogni prodotto/documento/presentazione rivolto a clienti o prospect di ZirkonIA deve essere **brandizzato**: logo/wordmark, palette e impaginazione coerenti, non più testo semplice o slide neutre. Regola esplicita di Federico, valida per tutti i materiali futuri (landing, protocollo, playbook, pitch, ecc.), non solo per il documento che l'ha generata.

## Quando si applica
Ogni volta che si produce un deliverable **esterno/client-facing** per ZirkonIA (presentazioni, PDF, landing, playbook, materiale di vendita). Non si applica alle note di lavoro interne del vault (restano markdown semplice, sono la fonte di contenuto — vedi "Rapporto con i contenuti sorgente" sotto).

## Il logo — risolto 2026-08-04 (stesso giorno, versione 2)
La prima versione di questa SOP (poche ore prima) proponeva un wordmark tipografico provvisorio "a orecchio", in assenza di un file reale. Federico ha fornito lo stesso giorno i due asset ufficiali — vedi [[Brand Kit ZirkonIA]] per il dettaglio completo:
1. **Icona** — "Z" a sfaccettature cristalline su sfondo a gradiente verde→blu, stile app icon.
2. **Wordmark** — "Zirkon" cromato/argento + "IA" blu, su fondo nero.

Da usare così: il wordmark ufficiale in intestazioni/firme di documento, l'icona come sigillo/badge su copertine o favicon. **Non ricreare il wordmark a testo con CSS** (l'approccio della v1 di questa SOP) — usare sempre i file immagine reali. File da salvare in `03 Risorse/Capitale Intellettuale/Brand/` (consegna manuale da Federico, vedi nota tecnica in [[Brand Kit ZirkonIA]]).

## Palette — corretta 2026-08-04 su asset reali
La palette oro/bronzo/antracite della v1 era una stima "a orecchio" dalla narrativa scritta (zircone, permanenza geologica) — **superata**: ora si usano i valori misurati direttamente sui file di logo forniti da Federico (vedi [[Brand Kit ZirkonIA]] per la fonte di ogni valore), non più un'invenzione plausibile.

| Ruolo | Hex |
|---|---|
| Sfondo primario | `#050607` |
| Sfondo pannelli/card | `#0D0F10` |
| Gradiente brand — verde | `#3BC79B` |
| Gradiente brand — blu | `#3B93BA` |
| Accento "setup/onboarding" (Gantt, badge) | `#3BC79B` (verde) |
| Accento "evoluzione/allineamento" (Gantt, badge) | `#5B90D1` (blu) |
| Testo primario | `#F2F2F4` |
| Testo secondario/muted | `#9A9DA3` |
| Linee/divisori | `#23262A` |

Uso: il verde segna l'avvio (profilazione, consegna), il blu la fase di accompagnamento continuo — stessa logica cromatica del gradiente dell'icona (verde in alto/inizio, blu in basso/maturo), non una scelta arbitraria.

## Tipografia — corretta 2026-08-04
La v1 proponeva un titolo serif ("richiama l'antico") per coerenza con la narrativa geologica scritta — **smentita dagli asset reali**: il wordmark ufficiale è un sans-serif bold, cromato, dal carattere tecnico/cristallino, non "pergamena antica". Correggere di conseguenza:
- **Titoli/headline**: sans bold/geometrico (es. Helvetica Neue Bold, Arial Black o equivalente di sistema) — stesso registro del wordmark.
- **Corpo testo**: sans neutro, peso regolare (es. Helvetica/Arial) — leggibilità, contrasto di peso coi titoli.
- **Numeri/date/dati**: monospace — precisione tecnica, usato nel cronoprogramma.

Font da CDN pubblici restano da evitare nei PDF stampabili (rischio di rendering non riproducibile offline) — usare famiglie di sistema equivalenti.

## Motivi grafici
Linee sottili (verde o blu a seconda della sezione, mai oro/bronzo — palette superata) come separatori, non riquadri pesanti. Molto spazio bianco/vuoto (coerente con la struttura della landing: headline → sub → blocco → sigillo, mai affollata). Il sigillo **"Verba volant, data manent."** chiude ogni documento esterno, sotto il wordmark ufficiale (il file immagine, non testo ricreato), come già previsto per la landing.

## Rapporto con i contenuti sorgente
Le note del vault restano la fonte di verità in markdown semplice (niente branding lì) — la veste grafica si applica solo al momento di produrre il deliverable esterno finale (HTML/PDF), generato a partire dal contenuto della nota sorgente corrispondente. Stesso schema già in uso per SOP (fonte umana) → Skill (controparte eseguibile).

## Collegamenti
- [[Brand Kit ZirkonIA]] — i file reali e la palette misurata
- [[ZirkonIA]] — narrativa di brand, offerta
- [[Report - Sessione Landing ZirkonIA (2026-07-20)]]
- [[SOP - Schema di Gantt]] — standard per cronoprogrammi grafici, applicato insieme a questa
- [[SOP - Tono e Stile ZirkonIA Core]] — controparte per il tono di voce (questa nota copre solo la resa visiva)
- [[Punti Aperti]]
