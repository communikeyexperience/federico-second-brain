#!/usr/bin/env python3
"""
Script di audit qualità per il vault FG SECOND BRAIN.
Ispirato al "gate di qualità" descritto da Giovanni Beggiato (vedi
[[Analisi - Company Brain di Giovanni Beggiato vs FG Second Brain]]),
adattato allo schema di [[Processi e Convenzioni]].

Uso:
    python3 audit_vault.py

Non corregge nulla in automatico: produce solo un referto in italiano,
da leggere e decidere cosa sistemare (coerente con la regola del vault
di non agire su ambiguità senza conferma umana).

Le 6 regole controllate:
1. Frontmatter presente e con almeno il campo `tipo`
2. Lunghezza massima consigliata: 300 righe (solo avviso, non blocca nulla)
3. Minimo 3 wikilink in uscita per nota (esclude cartelle "atomiche per
   design": Glossario Coaching, Templates, indici/_index/README)
4. Zero link rotti (ogni [[wikilink]] deve puntare a una nota/file esistente)
5. Zero note orfane nel grafo (nessuna nota mai linkata da nessun'altra)
6. Un solo componente connesso nel grafo delle note (nessuna "isola")

Nota tecnica: le note vengono identificate per PERCORSO relativo (non per
solo nome-file), perché il vault contiene volutamente più file con lo
stesso nome in cartelle diverse (_index.md in ogni cartella, README.md
in alcune cartelle) — usare solo il nome-file come chiave li farebbe
collassare tutti in uno solo.
"""

import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
# lo script vive in "03 Risorse/Sistema/", il vault è due livelli sopra
VAULT_ROOT = os.path.abspath(os.path.join(ROOT, "..", ".."))

EXCLUDE_DIR_NAMES = {".obsidian", ".claude"}
EXCLUDE_FOLDER_PREFIX = "ELIMINA_"
EXCLUDE_FILE_PREFIX = "ELIMINA_"
EXCLUDE_BASENAMES = {"CLAUDE"}
KNOWN_PLACEHOLDER_TARGETS = {"Progetto X", "Concetto Y", "Area Z", "Nome Cliente"}
EXTRA_VALID_EXTENSIONS = {
    ".base", ".canvas",
    ".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".csv",
    ".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mp3", ".zip", ".key",
}

EXEMPT_FROM_MIN_LINKS = {
    "02 Aree/Coaching - Conoscenza/Glossario",
    "Templates",
}

MAX_LINES = 300
MIN_WIKILINKS = 3
INDEX_BASENAMES = {"_index", "README"}

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def is_excluded_path(rel_dir):
    parts = rel_dir.split(os.sep)
    return any(p in EXCLUDE_DIR_NAMES or p.startswith(EXCLUDE_FOLDER_PREFIX) for p in parts)


def collect_files():
    notes = {}
    other_files = set()
    for dirpath, dirnames, filenames in os.walk(VAULT_ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIR_NAMES and not d.startswith(EXCLUDE_FOLDER_PREFIX))
        rel_dir = os.path.relpath(dirpath, VAULT_ROOT)
        if rel_dir == ".":
            rel_dir = ""
        if is_excluded_path(rel_dir):
            continue
        for f in filenames:
            if f.startswith(EXCLUDE_FILE_PREFIX):
                continue
            rel_path = os.path.join(rel_dir, f) if rel_dir else f
            rel_path = rel_path.replace(os.sep, "/")
            if f.endswith(".md"):
                basename = f[:-3]
                if basename in EXCLUDE_BASENAMES:
                    continue
                key = rel_path[:-3]
                notes[key] = rel_path
            else:
                ext = os.path.splitext(f)[1]
                if ext in EXTRA_VALID_EXTENSIONS:
                    other_files.add(rel_path[: -len(ext)])

    by_basename = defaultdict(list)
    for key in notes:
        base = key.split("/")[-1]
        by_basename[base].append(key)

    other_by_basename = defaultdict(list)
    for key in other_files:
        base = key.split("/")[-1]
        other_by_basename[base].append(key)

    return notes, other_files, by_basename, other_by_basename


def resolve_target(raw_target, notes, other_files, by_basename, other_by_basename):
    t = raw_target.strip()
    if t.startswith("./"):
        t = t[2:]
    if t in notes:
        return t
    # strip estensioni note (.base, .canvas) prima di confrontare
    t_noext = t
    for ext in EXTRA_VALID_EXTENSIONS:
        if t.endswith(ext):
            t_noext = t[: -len(ext)]
            break
    if t_noext in other_files:
        return "__FILE__:" + t_noext
    base = t.split("/")[-1]
    base_noext = t_noext.split("/")[-1]
    if base in by_basename:
        candidates = by_basename[base]
        if len(candidates) == 1:
            return candidates[0]
        return "__AMBIGUOUS__"
    if base_noext in other_by_basename:
        return "__FILE__:" + base_noext
    return None


def main():
    notes, other_files, by_basename, other_by_basename = collect_files()
    report = []
    report.append(f"# Referto audit vault — {len(notes)} note trovate\n")

    dup_index_readme = {b: paths for b, paths in by_basename.items() if b in INDEX_BASENAMES and len(paths) > 1}
    if dup_index_readme:
        report.append("## ℹ️ File `_index`/`README` in più cartelle (atteso, non è un problema)")
        for b, paths in dup_index_readme.items():
            report.append(f"- **{b}.md** presente in {len(paths)} cartelle (uno per cartella, come da disegno)")
        report.append("")

    other_dup = {b: paths for b, paths in by_basename.items() if b not in INDEX_BASENAMES and len(paths) > 1}
    if other_dup:
        report.append("## ⚠️ Basename duplicati fuori da _index/README (verificare)")
        for b, paths in other_dup.items():
            report.append(f"- **{b}**: " + ", ".join(notes[p] for p in paths))
        report.append("")

    missing_frontmatter = []
    missing_tipo = []
    too_long = []
    outbound_raw = {}

    for key, rel_path in notes.items():
        full_path = os.path.join(VAULT_ROOT, rel_path)
        try:
            c = open(full_path, encoding="utf-8", errors="ignore").read()
        except Exception as e:
            report.append(f"- ERRORE lettura {rel_path}: {e}")
            continue

        n_lines = c.count("\n") + 1
        if n_lines > MAX_LINES:
            too_long.append((key, rel_path, n_lines))

        if not c.startswith("---\n"):
            missing_frontmatter.append((key, rel_path))
        else:
            end = c.find("\n---\n", 4)
            if end == -1:
                missing_frontmatter.append((key, rel_path))
            else:
                fm_text = c[4:end]
                if "tipo:" not in fm_text:
                    missing_tipo.append((key, rel_path))

        outbound_raw[key] = list(set(WIKILINK_RE.findall(c)))

    report.append("## 1. Frontmatter")
    if not missing_frontmatter and not missing_tipo:
        report.append("✅ Tutte le note hanno frontmatter con campo `tipo`.")
    else:
        if missing_frontmatter:
            report.append(f"❌ {len(missing_frontmatter)} note senza frontmatter YAML:")
            for key, rel_path in missing_frontmatter:
                report.append(f"  - {rel_path}")
        if missing_tipo:
            report.append(f"⚠️ {len(missing_tipo)} note con frontmatter ma senza campo `tipo`:")
            for key, rel_path in missing_tipo:
                report.append(f"  - {rel_path}")
    report.append("")

    report.append(f"## 2. Note oltre {MAX_LINES} righe (solo avviso — valutare se spezzare)")
    if not too_long:
        report.append("✅ Nessuna nota supera il limite consigliato.")
    else:
        for key, rel_path, n_lines in sorted(too_long, key=lambda x: -x[2]):
            report.append(f"  - {rel_path} — {n_lines} righe")
    report.append("")

    broken = []
    resolved_links = defaultdict(set)

    for key, targets in outbound_raw.items():
        for raw in targets:
            if raw.strip() in KNOWN_PLACEHOLDER_TARGETS:
                continue
            resolved = resolve_target(raw, notes, other_files, by_basename, other_by_basename)
            if resolved is None:
                broken.append((key, notes[key], raw.strip()))
            elif resolved == "__AMBIGUOUS__":
                continue
            elif resolved.startswith("__FILE__:"):
                continue
            else:
                resolved_links[key].add(resolved)

    report.append("## 4. Link rotti")
    if not broken:
        report.append("✅ Nessun link rotto trovato.")
    else:
        report.append(f"❌ {len(broken)} link rotti:")
        for src_key, src_path, target in sorted(broken, key=lambda x: x[1]):
            report.append(f"  - {src_path}: [[{target}]] non esiste")
    report.append("")

    report.append(f"## 3. Note con meno di {MIN_WIKILINKS} wikilink in uscita")
    report.append("*(escluse le cartelle atomiche per design: Glossario Coaching, Templates, indici/_index/README)*")
    few_links = []
    for key, rel_path in notes.items():
        base = key.split("/")[-1]
        if base in INDEX_BASENAMES:
            continue
        folder = os.path.dirname(rel_path)
        if any(folder == ex or folder.startswith(ex + "/") for ex in EXEMPT_FROM_MIN_LINKS):
            continue
        n = len(resolved_links.get(key, set()))
        if n < MIN_WIKILINKS:
            few_links.append((key, rel_path, n))
    if not few_links:
        report.append("✅ Tutte le note (non esentate) hanno almeno 3 wikilink in uscita.")
    else:
        report.append(f"⚠️ {len(few_links)} note con pochi collegamenti in uscita:")
        for key, rel_path, n in sorted(few_links, key=lambda x: (x[2], x[1])):
            report.append(f"  - {rel_path} — {n} wikilink")
    report.append("")

    inbound_count = defaultdict(int)
    for key, targets in resolved_links.items():
        for t in targets:
            inbound_count[t] += 1

    orphans = []
    for key, rel_path in notes.items():
        base = key.split("/")[-1]
        if base in INDEX_BASENAMES:
            continue
        if inbound_count.get(key, 0) == 0:
            orphans.append((key, rel_path))

    report.append("## 5. Note orfane (zero collegamenti in entrata)")
    if not orphans:
        report.append("✅ Nessuna nota orfana.")
    else:
        report.append(f"❌ {len(orphans)} note orfane:")
        for key, rel_path in sorted(orphans, key=lambda x: x[1]):
            report.append(f"  - {rel_path}")
    report.append("")

    adjacency = defaultdict(set)
    for key, targets in resolved_links.items():
        for t in targets:
            adjacency[key].add(t)
            adjacency[t].add(key)
    all_keys = set(notes.keys())
    visited = set()
    components = []
    for start in all_keys:
        if start in visited:
            continue
        stack = [start]
        comp = set()
        while stack:
            cur = stack.pop()
            if cur in comp:
                continue
            comp.add(cur)
            for nxt in adjacency.get(cur, set()):
                if nxt not in comp:
                    stack.append(nxt)
        visited |= comp
        components.append(comp)

    report.append("## 6. Componenti connesse del grafo")
    if len(components) <= 1:
        report.append("✅ Un solo componente connesso: il grafo è tutto navigabile da un unico punto.")
    else:
        components.sort(key=len, reverse=True)
        report.append(f"⚠️ {len(components)} componenti separate (isole non raggiungibili tra loro):")
        for i, comp in enumerate(components, 1):
            sample = ", ".join(sorted(comp)[:5])
            more = f" (+{len(comp)-5} altre)" if len(comp) > 5 else ""
            report.append(f"  - Componente {i} ({len(comp)} note): {sample}{more}")
    report.append("")

    report.append("---")
    report.append(f"Totale note controllate: {len(notes)}")
    report.append("Referto generato senza modificare nulla nel vault.")

    print("\n".join(report))


if __name__ == "__main__":
    main()
