---
tipo: risorsa
tags: [fagioli, seo, wordpress, log]
progetto: "[[Fagioli - Blog Ristorazione]]"
---
# riccardofagioli.it — Esclusione pagine tecniche dall'indicizzazione

**Data intervento:** 2026-07-28
**Eseguito da:** account `cristianoEfederico` (id 3, ruolo **administrator**)
**Stack:** WordPress + Kadence + Elementor + ElementsKit Lite + Royal Addons + Yoast SEO Premium v24.9 (core 28.1) + Yoast Local SEO

---

## Causa radice

Le URL segnalate in Google Search Console non erano "trovate per sbaglio": **era la sitemap di Yoast a sottoporle attivamente a Google**.

```
sitemap_index.xml  (PRIMA)
├── post-sitemap.xml               ✔ contenuto reale
├── page-sitemap.xml               ✔ contenuto reale
├── elementskit_template-sitemap.xml  ✘ → /?elementskit_template=footer
├── category-sitemap.xml           ✔ contenuto reale
├── post_tag-sitemap.xml           ✔ contenuto reale
├── author-sitemap.xml             ✘ → /author/admin3485/
└── geo-sitemap.xml                ✘ → /locations.kml
```

I feed di categoria non erano in sitemap: Google li trovava dai `<link rel="alternate">` nelle pagine categoria.

**Nota importante:** "Rilevata/Scansionata ma non indicizzata" in GSC è un report *informativo*, non un errore. Quelle URL non erano indicizzate. L'intervento serve a igiene di crawl budget e pulizia del report, non a de-indicizzare.

---

## Modifiche applicate

### 1. Archivi autore → disattivati
`Yoast SEO → Impostazioni → Archivi autore → "Abilita archivi autore" = OFF`

Yoast stesso segnala il caso: blog monoautore ⇒ l'archivio autore duplica la homepage.

- `/author/admin3485/` → **301 verso la homepage**
- `author-sitemap.xml` → **404**, rimosso dal sitemap index

### 2. Feed non necessari → rimossi
`Yoast SEO → Impostazioni → Avanzate → Ottimizzazione della scansione`

Attivati (⇒ 301 verso la pagina padre, non 404):

| Toggle | Stato |
|---|---|
| Rimuovi i feed di categoria | ✅ ON *(richiesto)* |
| Rimuovi i feed dei tag | ✅ ON |
| Rimuovi i feed della tassonomia personalizzata | ✅ ON |
| Rimuovi i feed dei risultati della ricerca | ✅ ON |
| Rimuovi i feed degli autori degli articoli | ✅ ON |
| Rimuovi i feed dei commenti (globali + articoli) | ✅ ON |
| **Rimuovi il feed globale** (`/feed/`) | ❌ **lasciato OFF** |

⚠️ Il feed globale `/feed/` è stato **deliberatamente lasciato attivo**: potrebbe alimentare automazioni esterne (Publer, newsletter RSS-to-email). Disattivarlo solo dopo aver verificato che nessuno lo consumi.

### 3. `locations.kml` → bloccato via robots.txt
**Scelta del cliente:** tenere attivo Yoast Local SEO e bloccare solo il file.

Creato il **robots.txt fisico** (prima era virtuale, generato da Yoast) tramite
`Yoast SEO → Strumenti → Modifica file`, e aggiunta la regola:

```
# START YOAST BLOCK
# ---------------------------
User-agent: *
Disallow:

Sitemap: https://riccardofagioli.it/sitemap_index.xml
# ---------------------------
# END YOAST BLOCK

# --- Esclusioni pagine tecniche (2026-07-28) ---
# File KML generato da Yoast Local SEO (plugin attivo ma non configurato)
User-agent: *
Disallow: /*.kml$
```

### 4. CPT tecnici → esclusi dai risultati di ricerca
`Yoast SEO → Impostazioni → Tipi di contenuto → [CPT] → "Mostra ... nei risultati di ricerca" = OFF`

| CPT | Prima | Dopo |
|---|---|---|
| `elementskit-template` (Templates) | index, in sitemap | **noindex**, sitemap 404 *(richiesto)* |
| `elementskit-content` (ElementsKit items) | index | noindex |
| `elementskit_widget` (Widgets) | index | noindex |
| `e-floating-buttons` (Elementi fluttuanti) | index | noindex |
| `wpr_mega_menu` (Royal Mega Menu) | index | noindex |
| `wpr_templates` (Royal Templates) | index | noindex |

Solo il primo era già in sitemap; gli altri 5 sono stati chiusi in via preventiva — stessa classe di problema, sarebbero comparsi appena popolati.

---

## Stato verificato dopo il deploy

```
/?elementskit_template=footer        <meta robots> = noindex, follow   ✅
elementskit_template-sitemap.xml     404                               ✅
/author/admin3485/                   301 → homepage                    ✅
author-sitemap.xml                   404                               ✅
/locations.kml                       bloccato da robots.txt            ✅
/category/*/feed/                    301 → pagina categoria            ✅

REGRESSIONI (nessuna):
homepage                             200                               ✅
/feed/ globale                       200                               ✅
articoli                             index, follow                     ✅
pagine categoria                     index, follow                     ✅
post-sitemap.xml                     24 articoli                       ✅
robots.txt                           nessun blocco su wp-content/wp-includes  ✅
```

Sitemap index finale: `post` · `page` · `category` · `post_tag` · `geo`

---

## ⚠️ Residui noti

1. **`geo-sitemap.xml` continua a esistere e a puntare a `locations.kml`**, che ora è bloccato da robots.txt. In GSC l'URL non sparirà: si **riclassificherà** da "Scansionata ma non indicizzata" a **"Bloccata da robots.txt"**. È la conseguenza diretta di aver tenuto il plugin attivo.
   *Soluzione definitiva se in futuro si vuole pulire del tutto:* disattivare Yoast Local SEO (sparisce sia `geo-sitemap.xml` sia il KML), oppure configurarlo con i dati reali dell'attività.

2. **Titolo del sito WordPress vuoto** (`Impostazioni → Generali → Titolo del sito`). Conseguenza: ogni `<title>` finisce con un trattino orfano — `"Nuove Tendenze Archivi -"`, `"Riccardo Fagioli, Autore presso"`. Yoast segnala anche "Mancano il nome e il logo della tua organizzazione" (impatta i dati strutturati). **Rinviato per scelta del cliente** — da decidere insieme al posizionamento.

3. **robots.txt ora è un file fisico.** Effetto collaterale da ricordare: le regole robots.txt *dinamiche* dei plugin (es. i toggle Yoast "Rimuovi WP-JSON API", "Impedisci il crawling di AdsBot/GPTBot/CCBot") **non verranno più applicate**, perché il file statico è servito da Apache senza passare da WordPress. Se in futuro si attivano quei toggle, aggiungere le regole a mano nel file.

---

## Google Search Console — stato al 2026-07-28

Percorso del pulsante: `Indicizzazione → Pagine` → tabella "Perché le pagine non sono indicizzate" → clic sulla riga del motivo → barra grigia in alto: **"Hai corretto il problema? → CONVALIDA CORREZIONE"**.

⚠️ **La convalida è tutto-o-niente per motivo**: non si possono selezionare singole URL. Quindi va lanciata solo sui report interamente coperti dalle correzioni.

### ✅ "Pagina scansionata, ma attualmente non indicizzata" — CONVALIDA AVVIATA 28/07/26
2 URL, entrambe coperte dal fix:
```
/category/tecnologia-della-ristorazione/feed/
/category/nuove-tendenze/feed/
```
Stato: **IN ATTESA 2 · NON RIUSCITA 0**. Esito atteso in giorni/settimane.

### ❌ "Rilevata, ma attualmente non indicizzata" — NON convalidare
14 URL, di cui solo 3 nostre:
```
/?elementskit_template=footer   ← sistemata
/author/admin3485/              ← sistemata
/locations.kml                  ← sistemata
─────────────────────────────────────────────
/blog/                          ← contenuto vero, NON sistemato
/boom-vino-analcolico/          ← articolo, NON sistemato
/category/burocrazia-facile/
/category/economia-del-ristorante/
/category/gestione-del-personale/
/category/nuove-tendenze/
/category/prenotazioni-efficaci/
...
```
Lanciando la convalida, Google ricontrolla tutte e 14 → fallisce per via delle 11 pagine di contenuto → si resta bloccati fino a fine ciclo. **Non serve**: le 3 URL tecniche migreranno da sole nei bucket sani ("Pagina con reindirizzamento" e "Esclusa in base al tag noindex"), che di conseguenza cresceranno — è il risultato voluto, non un peggioramento.

---

## Fase 2 — Struttura di crawl (2026-07-28)

### Diagnosi: la homepage era un vicolo cieco

Mappa dei link interni **prima** dell'intervento:

```
/  (homepage — riceve tutta l'autorità)
├── /#matador           ancora sulla stessa pagina
├── /#iknosys           ancora sulla stessa pagina
└── /index.php/blog/    ← permalink VECCHIO → 301, per giunta target="_blank"
        └─→ /blog/
             ├── 8 articoli (su 24)
             ├── 4 categorie (su 8)
             └── /index.php/tutti-gli-articoli/  ← altro permalink vecchio → 301
                      └─→ /tutti-gli-articoli/
                           └── tutti e 24 gli articoli
```

Dalla homepage **zero link** verso articoli, categorie o indice. L'hub che linka tutti gli articoli era a **4 salti dietro 2 redirect** → Googlebot non ci arrivava. Da qui il "Rilevata, ma attualmente non indicizzata".

Il tessuto **fra** articoli invece è buono: ogni articolo linka ~10 altri articoli + 5 categorie, e il carosello Depicter genera `<a href>` reali in HTML (non solo JS). Non era rotto il tessuto interno — era rotta l'entrata.

### Categorie orfane (linkate da nessuna pagina hub, solo in sitemap)
```
/category/ai-per-la-ristorazione/
/category/burocrazia-facile/
/category/economia-del-ristorante/
/category/prenotazioni-efficaci/
```
Coincidono con le categorie nel report GSC. Una URL che vive solo in sitemap → "Rilevata ma non scansionata". **Non ancora risolto** (era il punto P5).

### ✅ P1 — Link BLOG nell'header corretto
Il sito **non ha un menu WordPress**: l'header è HTML hardcoded in un elemento Kadence. Corretti **due** theme mod (il secondo trovato solo dopo la verifica):
- `header_html_content` → `/index.php/blog/` **→** `/blog/`, rimosso `target="_blank"`
- `mobile_html_content` (menu mobile) → stessa correzione

`target="_blank"` lasciato sui 3 link esterni (IKNOSYS, CODICE IKNOSYS, BLACK BULL ACADEMY) — lì è corretto.
Applicato via Customizer (`wp.customize(...).set()` + `#save`). **Verificato: homepage ora 0 link stale.**

### ✅ P2 — Pattern sincronizzati corretti
- wp_block **1183** "CTA - Torna all indice articoli"
- wp_block **1238** "Top - Torna all'indice (su immagine)"

`/index.php/tutti-gli-articoli/` → `/tutti-gli-articoli/`. Due modifiche via REST → **propagate a tutti e 24 gli articoli**. Verificato sul front-end.

### ⚠️ SCOPERTA GROSSA — 47 link interni stale non ancora corretti

Scansione REST di tutti i contenuti: **19 articoli su 24 contengono link contestuali "Leggi anche" col VECCHIO permalink a data** `/index.php/2026/MM/GG/slug/`, tutti in 301.

| Post ID | slug | link stale |
|---|---|---|
| 1271 | piattaforme-prenotazione-ristoranti | 5 |
| 1282 | chioschi-self-service-ristoranti-scontrino-medio | 4 |
| 1265 | cultura-imprenditoriale-ristorazione-accoglienza | 4 |
| 1166 | marketing-per-ristoratori-lettera-oro-626 | 4 |
| 1309 | ristorante-indipendente-vs-catena | 3 |
| 1156 | clienti-con-il-cane… | 3 |
| 1129 | turisti-americani-sardegna | 3 |
| 1104 | food-cost-ristorante | 3 |
| 713 | menu-engineering… | 3 |
| 1298, 1291, 1136, 717, 1 (boom-vino-analcolico) | | 2 ciascuno |
| 1096, 1085, 721, 614, 610 | | 1 ciascuno |

**Totale: 47 link.** In più, la pagina `/blog/` (id 176) ne ha **6** dentro `_elementor_data`.

Sono i link interni contestuali aggiunti nelle sessioni SEO precedenti, scritti col formato permalink dell'epoca. Ogni click di Googlebot passa da un redirect → spreco di crawl budget e diluizione del link equity, proprio sul cluster che dovremmo rafforzare.

### ✅ P2-bis — 47 link stale CORRETTI (2026-07-28)

Trasformazione: `/index.php/AAAA/MM/GG/slug/` → URL reale letto dal campo `link` di `/wp/v2/posts` (**mai ricostruito a mano**).

**Metodo con rete di sicurezza** — prima un giro a vuoto per verificare che ogni slug corrispondesse a un articolo esistente, poi l'applicazione con questa invariante:

```js
const norm = s => s.replace(/https?:\/\/riccardofagioli\.it[^"'\s<>]*/g,'URL');
// applica SOLO se norm(before) === norm(after)
// → garantisce che cambino gli URL e nient'altro del testo
```

Risultato: **47/47 sostituiti su 19 articoli, invariante rispettata su tutti, 0 non applicati.**
Backup dei contenuti originali in `window.__backup` (volatile, perso a fine sessione).

**Caso particolare risolto:** nell'articolo 717 un link puntava allo slug `cassa-in-cloud-vs-gestionale-tradizionale`, che **non esiste più** — l'articolo è stato rinominato in `gestionale-in-cloud-vs-gestionale-tradizionale` (id 610). Quel link faceva **due redirect in fila** (`/index.php/…` → `/2026/03/11/…` → slug nuovo). Rimappato direttamente su 610.

**Verifica front-end:** 0 link stale residui in tutti e 19 gli articoli; 23 target interni distinti testati → **tutti 200 diretti, 0 redirect**.

⚠️ **Badge Yoast stale**: dopo edit REST del `content` il punteggio nella lista admin non si ricalcola. In questo caso è innocuo — sono cambiati solo gli `href`, non il testo né il numero di link, quindi non c'è nulla da ricalcolare. Se si vuole comunque rinfrescare: riaprire l'articolo nel block editor e `savePost()`.

### ⏳ Ancora da fare: 6 link stale nella pagina `/blog/` (id 176)
Vivono dentro `_elementor_data`. Vale il divieto assoluto: **si edita e si salva SOLO da Elementor, mai da Gutenberg** (ha già rotto il contenuto 2 volte in passato).

---

## 🔜 Lavoro separato da fare: perché `/blog/` e gli articoli non vengono scansionati

Emerso durante la verifica: `/blog/` e l'articolo `/boom-vino-analcolico/` sono **"Rilevati ma mai scansionati"** da Google, insieme a 5 pagine categoria. Non è un problema tecnico di indicizzazione — è il problema di **autorità/contenuto** che il brief indicava di trattare a parte. Un articolo che Google non degna nemmeno di una scansione è un segnale più serio delle 4 URL tecniche messe insieme. Da affrontare in una sessione dedicata (link interni, link in entrata, profondità di crawl, qualità/unicità dei contenuti).

**Non toccare** le pagine `/category/...` né gli articoli: sono contenuto legittimo, il loro problema è di autorità/contenuto ed è un lavoro separato.
