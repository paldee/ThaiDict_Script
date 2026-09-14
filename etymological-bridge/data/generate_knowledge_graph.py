# -*- coding: utf-8 -*-
"""
Generate enriched Etymological Bridge Knowledge Graph
Combines curated linguistic seed corpus with ORST official cache.
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from seed_corpus import ENTRIES

CACHE_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "orst_official_cache.json"))
OUT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "etymology_seeds.json"))


def enrich_entries(entries, cache_file):
    print(f"Reading ORST cache: {cache_file}")
    cache = {}
    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            cache = json.load(f)
        print(f"Loaded {len(cache)} ORST cache entries.")
    else:
        print("Warning: ORST cache not found!")

    enriched = []
    enriched_count = 0
    specialized_count = 0

    for item in entries:
        entry = dict(item)
        word = entry["thai_word"].strip()
        orst = cache.get(word)

        if not orst:
            # Try prefix match or stripping suffixes
            for k, v in cache.items():
                if k.startswith(word) or word.startswith(k):
                    orst = v
                    break

        if orst:
            entry["orst_definition"] = orst.get("thai_definition", "")
            entry["orst_read"] = orst.get("thai_read", "")
            entry["orst_pos"] = orst.get("thai_pos", "")
            entry["orst_edition"] = orst.get("orst_edition", "")
            entry["orst_etymology_tag"] = orst.get("orst_etymology_tag", "")
            entry["orst_sources"] = orst.get("sources", [])
            spec = orst.get("specialized_terms", [])
            entry["specialized_terms"] = spec
            if spec:
                specialized_count += len(spec)
            enriched_count += 1
        else:
            entry["orst_definition"] = "คำศัพท์บาลี-สันสกฤตที่ปรากฏในคลังคำศัพท์ไทย"
            entry["orst_read"] = ""
            entry["orst_pos"] = "น."
            entry["orst_edition"] = "สำนักงานราชบัณฑิตยสภา"
            entry["orst_sources"] = ["ORST Curated"]
            entry["specialized_terms"] = []

        enriched.append(entry)

    print(f"Enriched {enriched_count} / {len(entries)} words with official ORST data.")
    print(f"Total specialized domain mappings matched: {specialized_count}")
    return enriched


def main():
    enriched = enrich_entries(ENTRIES, CACHE_FILE)
    
    # Calculate dataset stats
    pie_roots = set(e["pie_root"] for e in enriched)
    categories = set(e["category"] for e in enriched)
    total_english_cognates = sum(len(e.get("english_cognates", [])) for e in enriched)

    payload = {
        "metadata": {
            "title": "Etymological Bridge Knowledge Graph",
            "subtitle": "สะพานเชื่อมรากศัพท์: ภาษาไทย ↔ สันสกฤต/บาลี ↔ PIE ↔ ภาษาอังกฤษ",
            "curator": "Nextect Dictionary Reimagined Project",
            "institution": "สำนักงานราชบัณฑิตยสภา (Office of the Royal Society of Thailand)",
            "total_thai_words": len(enriched),
            "total_pie_roots": len(pie_roots),
            "total_categories": len(categories),
            "total_english_cognates": total_english_cognates,
            "version": "1.0.0"
        },
        "categories": sorted(list(categories)),
        "entries": enriched
    }

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {OUT_FILE} with {len(enriched)} words and {total_english_cognates} English cognates!")


if __name__ == "__main__":
    main()
