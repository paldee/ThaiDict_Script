# -*- coding: utf-8 -*-
"""
Etymological Bridge Knowledge Graph Engine
Graph traversal, indexing, semantic search, and D3 visualization data builder.
"""

import os
import sys
import json
import random

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from classifier import classify_thai_word


class EtymologyEngine:
    def __init__(self, data_file=None, orst_cache_file=None):
        base_dir = os.path.dirname(__file__)
        if data_file is None:
            data_file = os.path.abspath(os.path.join(base_dir, "..", "data", "etymology_seeds.json"))
        if orst_cache_file is None:
            orst_cache_file = os.path.abspath(os.path.join(base_dir, "..", "data", "orst_official_cache.json"))

        self.data_file = data_file
        self.orst_cache_file = orst_cache_file

        self.entries = []
        self.word_index = {}
        self.pie_index = {}
        self.english_index = {}
        self.categories = set()
        self.metadata = {}
        self.orst_cache = {}

        self.load_data()

    def load_data(self):
        # Load Knowledge Graph
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.metadata = data.get("metadata", {})
                self.entries = data.get("entries", [])
        else:
            print(f"Warning: Data file not found at {self.data_file}")

        # Indexing
        for entry in self.entries:
            th_word = entry["thai_word"].strip()
            self.word_index[th_word] = entry
            self.categories.add(entry.get("category", "ทั่วไป"))

            pie_root = entry.get("pie_root", "").strip()
            if pie_root:
                if pie_root not in self.pie_index:
                    self.pie_index[pie_root] = []
                self.pie_index[pie_root].append(entry)

            for cognate in entry.get("english_cognates", []):
                en_w = cognate["word"].lower().strip()
                if en_w not in self.english_index:
                    self.english_index[en_w] = []
                self.english_index[en_w].append(entry)

        # Load ORST Cache
        if os.path.exists(self.orst_cache_file):
            try:
                with open(self.orst_cache_file, "r", encoding="utf-8") as f:
                    self.orst_cache = json.load(f)
            except Exception as e:
                print(f"Could not load ORST cache: {e}")

        print(f"Engine loaded: {len(self.entries)} entries, {len(self.pie_index)} PIE roots, {len(self.english_index)} English cognate mappings.")

    def get_stats(self):
        return {
            "total_entries": len(self.entries),
            "total_pie_roots": len(self.pie_index),
            "total_english_cognates": len(self.english_index),
            "total_categories": len(self.categories),
            "categories": sorted(list(self.categories)),
            "orst_official_coverage": f"{len(self.orst_cache):,} คำจากพจนานุกรมและคลังศัพท์เฉพาะทาง"
        }

    def list_all(self, category=None):
        res = []
        for e in self.entries:
            if category and e.get("category") != category:
                continue
            res.append({
                "thai_word": e["thai_word"],
                "category": e.get("category", ""),
                "pali_sanskrit_form": e.get("pali_sanskrit_form", ""),
                "pie_root": e.get("pie_root", ""),
                "pie_meaning": e.get("pie_meaning", ""),
                "cognates_sample": [c["word"] for c in e.get("english_cognates", [])[:3]],
                "orst_pos": e.get("orst_pos", ""),
                "orst_definition": e.get("orst_definition", "")
            })
        return res

    def lookup(self, word):
        w = word.strip()
        # Direct lookup
        if w in self.word_index:
            return self.word_index[w]

        # Case insensitive English word lookup
        low_w = w.lower()
        if low_w in self.english_index:
            return self.english_index[low_w][0]

        return None

    def search(self, query):
        q = query.strip().lower()
        if not q:
            return self.list_all()[:20]

        results = []
        seen = set()

        # 1. Exact Thai match
        if q in self.word_index:
            e = self.word_index[q]
            results.append({"entry": e, "match_type": "Exact Thai Headword", "score": 100})
            seen.add(e["thai_word"])

        # 2. Exact English cognate match
        if q in self.english_index:
            for e in self.english_index[q]:
                if e["thai_word"] not in seen:
                    results.append({"entry": e, "match_type": "Exact English Cognate", "score": 95})
                    seen.add(e["thai_word"])

        # 3. Substring searches
        for e in self.entries:
            tw = e["thai_word"]
            if tw in seen:
                continue

            # Substring Thai
            if q in tw:
                results.append({"entry": e, "match_type": "Thai Substring", "score": 80})
                seen.add(tw)
                continue

            # Check English cognates
            matched_en = [c["word"] for c in e.get("english_cognates", []) if q in c["word"].lower()]
            if matched_en:
                results.append({"entry": e, "match_type": f"English Cognate ({', '.join(matched_en)})", "score": 75})
                seen.add(tw)
                continue

            # Check PIE root or Sanskrit form
            if q in e.get("pie_root", "").lower() or q in e.get("pali_sanskrit_form", "").lower():
                results.append({"entry": e, "match_type": "PIE / Sanskrit Root Match", "score": 70})
                seen.add(tw)
                continue

            # Category
            if q in e.get("category", "").lower():
                results.append({"entry": e, "match_type": "Category Match", "score": 50})
                seen.add(tw)
                continue

        results.sort(key=lambda x: x["score"], reverse=True)
        return [r["entry"] for r in results]

    def classify(self, word):
        return classify_thai_word(word, self.word_index, self.orst_cache)

    def get_d3_graph(self, word):
        entry = self.lookup(word)
        if not entry:
            # Try classify
            cl = self.classify(word)
            if cl.get("entry"):
                entry = cl["entry"]
            else:
                return None

        pie_root = entry.get("pie_root", "*PIE")
        thai_word = entry["thai_word"]
        skt_form = entry.get("pali_sanskrit_form", "Sanskrit")

        nodes = []
        links = []

        # Root Node: PIE (Ancient Ancestor)
        nodes.append({
            "id": "pie_root",
            "name": pie_root,
            "label": f"ราก PIE:\n{pie_root}",
            "type": "pie_root",
            "group": 0,
            "meaning": entry.get("pie_meaning", ""),
            "era": "~4500-2500 BCE",
            "radius": 28
        })

        # Eastern Branch: Indo-Iranian
        nodes.append({
            "id": "branch_indo_iranian",
            "name": "Indo-Iranian Branch",
            "label": "สายอินโด-อิเรเนียน\n(Indo-Iranian)",
            "type": "branch",
            "group": 1,
            "era": "~2000 BCE",
            "radius": 20
        })
        links.append({"source": "pie_root", "target": "branch_indo_iranian", "label": "Eastern (Satem)"})

        # Sanskrit / Indic node
        nodes.append({
            "id": "sanskrit_node",
            "name": skt_form,
            "label": f"สันสกฤต/บาลี:\n{skt_form}",
            "type": "intermediate_lang",
            "group": 1,
            "era": "~1500 BCE",
            "radius": 22
        })
        links.append({"source": "branch_indo_iranian", "target": "sanskrit_node", "label": "Vedic / Classical"})

        # Thai Node (Destination)
        nodes.append({
            "id": "thai_word_node",
            "name": thai_word,
            "label": f"ภาษาไทย: {thai_word}\n({entry.get('orst_read') or thai_word})",
            "type": "thai_leaf",
            "group": 1,
            "pos": entry.get("orst_pos", ""),
            "definition": entry.get("orst_definition", ""),
            "era": "~1300 CE - ปัจจุบัน",
            "radius": 26
        })
        links.append({"source": "sanskrit_node", "target": "thai_word_node", "label": "คำยืมสู่ภาษาไทย (Loanword)"})

        # Western Branches for English Cognates
        # Group cognates by branch
        branch_map = {
            "Germanic": {"id": "branch_germanic", "label": "สายเจอร์แมนิก\n(Germanic)", "group": 2, "era": "~500 BCE"},
            "Italic/Latin": {"id": "branch_italic", "label": "สายอิตาลิก/ละติน\n(Italic/Latin)", "group": 3, "era": "~750 BCE"},
            "Hellenic/Greek": {"id": "branch_hellenic", "label": "สายเฮลเลนิก/กรีก\n(Hellenic/Greek)", "group": 4, "era": "~800 BCE"}
        }

        active_branches = set()

        for idx, cog in enumerate(entry.get("english_cognates", [])):
            orig = cog.get("origin_language", "")
            if "Greek" in orig:
                b_key = "Hellenic/Greek"
            elif "Latin" in orig or "French" in orig:
                b_key = "Italic/Latin"
            else:
                b_key = "Germanic"

            # Add branch node if not added
            b_info = branch_map[b_key]
            if b_key not in active_branches:
                nodes.append({
                    "id": b_info["id"],
                    "name": b_info["label"],
                    "label": b_info["label"],
                    "type": "branch",
                    "group": b_info["group"],
                    "era": b_info["era"],
                    "radius": 20
                })
                links.append({"source": "pie_root", "target": b_info["id"], "label": "Western (Centum)"})
                active_branches.add(b_key)

            # English word leaf node
            cog_id = f"cognate_{idx}_{cog['word']}"
            nodes.append({
                "id": cog_id,
                "name": cog["word"],
                "label": f"{cog['word']}\n[{cog.get('difficulty', '')}]",
                "type": "english_leaf",
                "group": b_info["group"],
                "origin": orig,
                "derivation": cog.get("derivation_path", ""),
                "usage_note": cog.get("usage_note", ""),
                "radius": 22
            })
            links.append({"source": b_info["id"], "target": cog_id, "label": "วิวัฒนาการสู่ภาษาอังกฤษ"})

        return {
            "thai_word": thai_word,
            "pie_root": pie_root,
            "sound_change_law": entry.get("sound_change_law", ""),
            "semantic_drift_note": entry.get("semantic_drift_note", ""),
            "nodes": nodes,
            "links": links
        }

    def generate_quiz(self, num_questions=5):
        """Generates dynamic quiz questions for Learn English via Thai mode."""
        if not self.entries:
            return []

        pool = list(self.entries)
        random.shuffle(pool)
        selected = pool[:num_questions]

        questions = []
        for entry in selected:
            cogs = entry.get("english_cognates", [])
            if not cogs:
                continue
            correct_cog = random.choice(cogs)
            correct_word = correct_cog["word"]

            # Pick 3 wrong options from other words
            wrong_options = []
            for other in pool:
                if other["thai_word"] == entry["thai_word"]:
                    continue
                for oc in other.get("english_cognates", []):
                    if oc["word"] != correct_word and oc["word"] not in wrong_options:
                        wrong_options.append(oc["word"])
                        break
                if len(wrong_options) >= 3:
                    break

            options = wrong_options + [correct_word]
            random.shuffle(options)

            q = {
                "thai_word": entry["thai_word"],
                "pali_sanskrit": entry.get("pali_sanskrit_form", ""),
                "pie_root": entry.get("pie_root", ""),
                "question": f"คำภาษาไทย '{entry['thai_word']}' มีรากศัพท์ร่วม (Cognate) ผ่านตระกูล PIE เดียวกับคำศัพท์ภาษาอังกฤษใด?",
                "options": options,
                "correct_answer": correct_word,
                "explanation": correct_cog.get("usage_note", f"มาจากราก {entry.get('pie_root')} เดียวกัน"),
                "derivation_path": correct_cog.get("derivation_path", ""),
                "difficulty": correct_cog.get("difficulty", "General")
            }
            questions.append(q)

        return questions
