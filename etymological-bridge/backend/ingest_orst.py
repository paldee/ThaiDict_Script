# -*- coding: utf-8 -*-
"""
Ingest ORST (Office of the Royal Society of Thailand) Official Datasets
Extracts dictionary definitions, readings, parts of speech, and specialized domain terms.
"""

import os
import re
import sys
import json
import openpyxl

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


DATA_BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "Data Source-20260914T071736Z-1-001", "Data Source")
)
DICT_2542_PATH = os.path.join(DATA_BASE_DIR, "พจนานุกรม ฉบับราชบัณฑิตยสภาน", "DICT_2542 (ก_ฮ).xlsx")
DICT_2554_PATH = os.path.join(DATA_BASE_DIR, "พจนานุกรม ฉบับราชบัณฑิตยสภาน", "DICT_2554 (ก_ซ).xlsx")
SPECIALIZED_DIR = os.path.join(DATA_BASE_DIR, "พจนานุกรม เฉพาะสาขาวิชา")

OUT_ORST_CACHE = os.path.join(os.path.dirname(__file__), "..", "data", "orst_official_cache.json")


def clean_str(val):
    if val is None:
        return ""
    s = str(val).strip()
    if s.lower() in ("null", "none"):
        return ""
    return s


def parse_dict_2542_definition(def_text):
    """
    Parses DICT 2542 format e.g.:
    '[ทันตะ-] (แบบ) น. ฟัน, งาช้าง เช่น เอกทันต์. (ป., ส.).'
    Extracts reading, pos, definition, etymology tag.
    """
    reading = ""
    pos = ""
    etymology_raw = ""
    cleaned_def = def_text.strip()

    # Match reading inside brackets at start: [xxx]
    read_m = re.match(r"^\[(.*?)\]\s*", cleaned_def)
    if read_m:
        reading = read_m.group(1).strip()
        cleaned_def = cleaned_def[read_m.end():].strip()

    # Match etymology at end or inside parens e.g. (ป., ส.) or (ส.; ป. เนตฺต)
    etym_m = re.findall(r"\(([ปสขจอญชพยฝล]|\s*ป\.\s*|\s*ส\.\s*|บาลี|สันสกฤต)[^\)]*\)", cleaned_def)
    if etym_m:
        etymology_raw = " ".join(etym_m)

    # POS identification (e.g., น., ก., ว., สัน., อุ.)
    pos_m = re.search(r"\b(น\.|ก\.|ว\.|สัน\.|อุ\.|นิ\.|สรรพ\.)", cleaned_def)
    if pos_m:
        pos = pos_m.group(1)

    return {
        "reading": reading,
        "pos": pos,
        "definition": cleaned_def,
        "etymology_raw": etymology_raw
    }


def extract_orst_data():
    results = {}

    # 1. Load DICT_2542 (Full coverage ก-ฮ)
    print(f"Loading DICT_2542 from: {DICT_2542_PATH}")
    if os.path.exists(DICT_2542_PATH):
        wb_2542 = openpyxl.load_workbook(DICT_2542_PATH, read_only=True)
        ws_2542 = wb_2542.active
        rows = ws_2542.iter_rows(values_only=True)
        next(rows)  # skip header: ('number', 'K_W', 'M_W', 'D_T')
        
        for r in rows:
            if not r or len(r) < 4:
                continue
            raw_kw = clean_str(r[1])
            mw = clean_str(r[2])
            dt = clean_str(r[3])
            
            # Words can be comma separated like 'ก็,ก็ ๑'
            kws = [k.strip() for k in raw_kw.split(",") if k.strip()]
            parsed = parse_dict_2542_definition(dt)
            
            for word in kws:
                # remove numeral suffix if any e.g. 'ก็ ๑' -> 'ก็'
                base_word = re.sub(r"\s+[๐-๙\d]+$", "", word).strip()
                if not base_word:
                    continue
                if base_word not in results:
                    results[base_word] = {
                        "thai_word": base_word,
                        "main_word": mw,
                        "thai_read": parsed["reading"],
                        "thai_pos": parsed["pos"],
                        "thai_definition": parsed["definition"],
                        "orst_etymology_tag": parsed["etymology_raw"],
                        "orst_edition": "พจนานุกรม ฉบับราชบัณฑิตยสถาน พ.ศ. ๒๕๔๒",
                        "sources": ["DICT_2542"],
                        "specialized_terms": []
                    }
        print(f"Loaded {len(results)} base words from DICT_2542.")

    # 2. Enrich with DICT_2554 (ก-ซ with more detailed metadata)
    print(f"Loading DICT_2554 from: {DICT_2554_PATH}")
    if os.path.exists(DICT_2554_PATH):
        wb_2554 = openpyxl.load_workbook(DICT_2554_PATH, read_only=True)
        ws_2554 = wb_2554.active
        rows_2554 = ws_2554.iter_rows(values_only=True)
        next(rows_2554)  # header
        
        count_54 = 0
        for r in rows_2554:
            if not r or len(r) < 7:
                continue
            hw = clean_str(r[1])
            if not hw:
                continue
            base_hw = re.sub(r"\s+[๐-๙\d]+$", "", hw).strip()
            read_54 = clean_str(r[3])
            pos_54 = clean_str(r[5])
            def_54 = clean_str(r[6])
            
            etym_list = []
            if len(r) > 11 and clean_str(r[11]):
                etym_list.append(clean_str(r[11]))
            if len(r) > 14 and clean_str(r[14]):
                etym_list.append(clean_str(r[14]))
            etym_54 = "; ".join(etym_list)

            if base_hw in results:
                entry = results[base_hw]
                if read_54: entry["thai_read"] = read_54
                if pos_54: entry["thai_pos"] = pos_54
                if def_54: entry["thai_definition"] = def_54
                if etym_54: entry["orst_etymology_tag"] = etym_54
                entry["orst_edition"] = "พจนานุกรม ฉบับราชบัณฑิตยสถาน พ.ศ. ๒๕๕๔"
                if "DICT_2554" not in entry["sources"]:
                    entry["sources"].append("DICT_2554")
            else:
                results[base_hw] = {
                    "thai_word": base_hw,
                    "main_word": base_hw,
                    "thai_read": read_54,
                    "thai_pos": pos_54,
                    "thai_definition": def_54,
                    "orst_etymology_tag": etym_54,
                    "orst_edition": "พจนานุกรม ฉบับราชบัณฑิตยสถาน พ.ศ. ๒๕๕๔",
                    "sources": ["DICT_2554"],
                    "specialized_terms": []
                }
            count_54 += 1
        print(f"Enriched {count_54} entries from DICT_2554.")

    # 3. Load Specialized Dictionaries (Medical, Philosophy, Psychology)
    specialized_files = [
        ("ศัพท์แพทย์.xlsx", "การแพทย์/กายวิภาคศาสตร์"),
        ("ศัพท์ปรัชญา.xlsx", "ปรัชญา"),
        ("ศัพท์จิตวิทยา.xlsx", "จิตวิทยา")
    ]
    
    for fname, domain in specialized_files:
        fpath = os.path.join(SPECIALIZED_DIR, fname)
        if not os.path.exists(fpath):
            continue
        print(f"Loading specialized terms from {fname}...")
        wb_spec = openpyxl.load_workbook(fpath, read_only=True)
        ws_spec = wb_spec.active
        rows_spec = ws_spec.iter_rows(values_only=True)
        next(rows_spec)  # header
        
        spec_count = 0
        for r in rows_spec:
            if not r or len(r) < 3:
                continue
            en_term = clean_str(r[1])
            th_term = clean_str(r[2])
            explanation = clean_str(r[8]) if len(r) > 8 else ""
            if not en_term or not th_term:
                continue
            
            # Map Thai terms
            for th_sub in re.split(r"[,;]\s*", th_term):
                clean_th = th_sub.strip()
                if not clean_th:
                    continue
                # Add to words that contain this root
                spec_entry = {
                    "english_term": en_term,
                    "thai_term": clean_th,
                    "domain": domain,
                    "explanation": explanation
                }
                # Check direct match or substring
                if clean_th in results:
                    results[clean_th]["specialized_terms"].append(spec_entry)
                spec_count += 1
        print(f"Processed {spec_count} terms from {fname}.")

    # Save cache
    os.makedirs(os.path.dirname(OUT_ORST_CACHE), exist_ok=True)
    with open(OUT_ORST_CACHE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Successfully cached {len(results)} ORST entries to {OUT_ORST_CACHE}")
    return results


if __name__ == "__main__":
    extract_orst_data()
