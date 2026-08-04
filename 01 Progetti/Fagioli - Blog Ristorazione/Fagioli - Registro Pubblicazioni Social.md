---
tipo: risorsa
tags: [fagioli, social, linkedin, facebook, log]
progetto: "[[Fagioli - Blog Ristorazione]]"
---
# Registro pubblicazioni social — Blog Ristorazione Fagioli

**Aggiornato:** 2026-07-31
**Blog:** riccardofagioli.it — **26 articoli pubblicati**
**Canali:** LinkedIn (profilo personale Riccardo Fagioli) · Facebook (Pagina Codice Iknosys, id `100699946193205`)

> ⚠️ **Attendibilità di questo registro.** La colonna blog è certa (letta dall'API WordPress). Le colonne social sono ricostruite da: registro storico delle sessioni + verifica diretta sul profilo LinkedIn del 31/07 + conferma a voce di Federico (31/07) per le due caselle Facebook che non ero riuscito a verificare. **Nessuna voce resta in sospeso.**
>
> Nota di metodo: **i post social non sono enumerabili via automazione** — LinkedIn virtualizza il feed (tiene in pagina solo 3-5 post per volta), `find_post` di Publer richiede un ID puntuale invece di elencare, e il connettore Facebook Pages ha solo azioni di scrittura. **Questo registro va quindi aggiornato A MANO a ogni pubblicazione**, non è ricostruibile a posteriori.

---

## Riepilogo

| | |
|---|---|
| Articoli sul blog | **26** |
| Pubblicati — tutti e 10 su **entrambi** i canali | **10** |
| **Mai portati sui social** | **16** |

**Il blog produce più in fretta di quanto i contenuti vengano rilanciati.** Il divario è la cosa più importante che dice questo registro.

---

## Pubblicati

| Data | ID | Articolo | LinkedIn | Facebook |
|---|---|---|---|---|
| 26/06 | 721 | La chiave per il successo: il cameriere venditore | ✅ manuale | ✅ `…_992188500379270` |
| 26/06 | 614 | Monitor in cucina (KDS) | ✅ `urn:li:share:7476303555881201664` | ✅ `…_992182317046555` |
| 01–02/07 | 1 | Il boom del vino analcolico | ✅ manuale 02/07 | ✅ `…_996210076643779` |
| ~05/07 | 717 | Food Cost: il numero che ti dice se stai guadagnando | ✅ manuale | ✅ confermato da Federico 31/07 |
| 10/07 | 1129 | Turisti americani in Sardegna | ✅ `urn:li:share:7481280025028136960` | ✅ `…_1003820872549366` |
| 13/07 | 1166 | La "Lettera d'Oro" di 626 School | ✅ manuale (3 tentativi automatici falliti) | ✅ `…_1006349442296509` |
| 17–18/07 | 1265 | Cultura imprenditoriale nella ristorazione | ✅ `urn:li:share:7483932722667765760` | ✅ `…_1010143765250410` |
| ~23–24/07 | 1291 | Pagamenti divisi al ristorante | ✅ verificato sul profilo | ✅ |
| ~28/07 | 1338 | Addio al greenwashing nei menù | ✅ verificato sul profilo | ✅ confermato da Federico 31/07 |
| **31/07** | **1156** | **Clienti con il cane** | ✅ + primo commento a mano | ✅ `…_1020734504191336` |

## Mai pubblicati sui social — 16 articoli

| Data blog | ID | Articolo |
|---|---|---|
| 30/07 | 1394 | Google Business Profile per ristoranti |
| 29/07 | 1386 | Perché i ristoranti chiudono: 3 errori |
| 27/07 | 1347 | Fidelizzare lo staff in sala |
| 25/07 | 1331 | Divise personalizzate per ristoranti |
| 25/07 | 1323 | Overbooking controllato al ristorante |
| 23/07 | 1316 | Allergeni: in regola senza rovinare il menu |
| 19/07 | 1309 | Ristorante indipendente o catena |
| 19/07 | 1298 | La mise en place può aumentare lo scontrino medio |
| 18/07 | 1282 | Chioschi self-service per ristoranti |
| 17/07 | 1271 | Piattaforme di prenotazione: convengono davvero? |
| 11/07 | 1136 | Il tuo menu in PDF sta regalando clienti ai concorrenti |
| 04/07 | 1104 | Food Cost ristorante: calcolarlo con Excel |
| 04/07 | 1096 | GEO: farsi trovare dalle Intelligenze Artificiali |
| 03/07 | 1085 | Sms ed email di promemoria automatici |
| 19/06 | 713 | Menu Engineering *(pubblicato come test il 26/06 e poi eliminato — non conta)* |
| 12/06 | 610 | Gestionale in Cloud vs Tradizionale |

---

## Regole operative (non dimenticarle)

**Il link.** Nel commento LinkedIn e nella card Facebook va SEMPRE il permalink canonico senza data: `https://riccardofagioli.it/<slug>/`. Il vecchio formato `/index.php/AAAA/MM/GG/slug/` è morto. Prima di pubblicare, verificare che l'URL risponda **200 diretto, zero redirect**, e che `canonical` e `og:url` coincidano.

**Slug ≠ titolo.** Su questo blog alcuni slug non corrispondono al contenuto (articoli riscritti mantenendo il vecchio permalink). Fidarsi sempre dell'`og:title`, mai dello slug.

**Il primo commento LinkedIn è da fare a mano.** L'auto-comment di Publer ha fallito 2 volte su 3 tentativi tracciati (turisti americani, clienti con il cane): l'API risponde `success` ma il commento non compare. Verificare sempre sul profilo confrontando l'indicatore "N commenti" del post nuovo con quello degli altri.

**"MCP server connection lost" non significa che il post non sia uscito.** Il 31/07 `create_post` ha dato quell'errore ma il post era stato pubblicato regolarmente. Un retry avrebbe creato un doppione sul profilo di Riccardo. Verificare **sempre** prima di ritentare.

**Facebook** funziona in modo affidabile con l'azione diretta Facebook Pages passando `link_url` (la card la genera Facebook). Publer NON produce la card: posta il link come testo semplice. Aggiungere sempre nelle istruzioni "do NOT ask follow-up questions", altrimenti l'azione a volte chiede conferma invece di eseguire.
