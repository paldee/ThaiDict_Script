# -*- coding: utf-8 -*-
"""
Thai Word Classifier & Morphological Analyzer
Detects Sanskrit/Pali loanwords vs Native Thai (Kra-Dai) words.
Provides etymological suggestions (e.g. แม่ -> มารดา, พ่อ -> บิดา, หมา -> สุนัข, ฟัน -> ทันต).
"""

import re

# Native Thai words mapped to their formal Sanskrit/Pali equivalents
NATIVE_THAI_MAPPINGS = {
    "แม่": {
        "formal_equivalent": "มารดา",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "'แม่' เป็นคำไทยแท้ แต่คู่เทียบคำทางการในภาษาไทยคือ 'มารดา' ซึ่งมีรากศัพท์เชื่อมโยงกับภาษาอังกฤษ (mother, maternal)"
    },
    "พ่อ": {
        "formal_equivalent": "บิดา",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "'พ่อ' เป็นคำไทยแท้ คู่เทียบคำทางการคือ 'บิดา' ซึ่งมีรากศัพท์เชื่อมโยงกับภาษาอังกฤษ (father, paternal)"
    },
    "พี่ชาย": {
        "formal_equivalent": "ภราดา",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'ภราดา' เชื่อมโยงกับ brother, fraternal"
    },
    "ลูกสาว": {
        "formal_equivalent": "ธิดา",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'ธิดา' เชื่อมโยงกับ daughter"
    },
    "ฟัน": {
        "formal_equivalent": "ทันต",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "'ฟัน' เป็นคำไทยแท้ แต่ในคำประสมทางการใช้ 'ทันต' (ทันตแพทย์) ซึ่งเชื่อมโยงกับ dental, dentist, tooth"
    },
    "จมูก": {
        "formal_equivalent": "นาสา",
        "native_family": "คำยืมเขมร (Austroasiatic) / ขร้า-ไท",
        "note": "คู่เทียบราชาศัพท์/ทางการคือ 'นาสา' เชื่อมโยงกับ nose, nasal"
    },
    "ตา": {
        "formal_equivalent": "เนตร",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'เนตร' (ผู้นำทาง) หรือ 'จักษุ' เชื่อมโยงกับ ocular, eye"
    },
    "เท้า": {
        "formal_equivalent": "บาท",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'บาท' ซึ่งเชื่อมโยงกับ foot, pedal, pedestrian"
    },
    "มือ": {
        "formal_equivalent": "หัตถ์",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'หัตถ์' (หัตถกรรม) เชื่อมโยงกับ surgery"
    },
    "ใจ": {
        "formal_equivalent": "หทัย",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'หทัย/มโน' เชื่อมโยงกับ heart, cardiac, mind"
    },
    "หมา": {
        "formal_equivalent": "สุนัข",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "'หมา' เป็นคำไทยแท้ดั้งเดิม แต่คำทางการคือ 'สุนัข' ซึ่งเชื่อมโยงกับ hound, canine, cynic"
    },
    "ม้า": {
        "formal_equivalent": "อัศวะ",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'อัศวะ' เชื่อมโยงกับ equine, equestrian"
    },
    "วัว": {
        "formal_equivalent": "โค",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'โค' เชื่อมโยงกับ cow, bovine, beef"
    },
    "น้ำ": {
        "formal_equivalent": "วารี",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'วารี' เชื่อมโยงกับ water, hydro-"
    },
    "ไฟ": {
        "formal_equivalent": "อัคนี",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'อัคนี' เชื่อมโยงกับ ignite, ignition, igneous"
    },
    "ลม": {
        "formal_equivalent": "วายุ",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'วายุ/วาต' เชื่อมโยงกับ wind, window, ventilate"
    },
    "ตาย": {
        "formal_equivalent": "มรณะ",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'มรณะ' เชื่อมโยงกับ mortal, murder, immortal"
    },
    "พูด": {
        "formal_equivalent": "วาจา",
        "native_family": "ตระกูลภาษาขร้า-ไท (Kra-Dai)",
        "note": "คู่เทียบคำทางการคือ 'วาจา' เชื่อมโยงกับ voice, vocal, advocate"
    }
}

# Sanskrit & Pali phonetic and morphological heuristic patterns
INDIC_PATTERNS = [
    (r"[ศษ]", "พบพยัญชนะ ศ หรือ ษ ซึ่งมีเฉพาะในภาษาสันสกฤต"),
    (r"[ฤฦ]", "พบสระ ฤ หรือ ฦ ซึ่งเป็นสระเสียงสันสกฤต"),
    (r"(กรรม|ศาสตร์|วิทยา|ภาพ|การ|สถาน|กร|ราช|ทัศน์)$", "ลงท้ายด้วยหน่วยคำยืมสันสกฤต-บาลีมาตรฐาน"),
    (r"[์]", "พบไม้ทัณฑฆาต (การันต์) ซึ่งสะท้อนการยืมคำที่มีตัวสะกดหลายชั้นจากสันสกฤต"),
    (r"(ทธ|ตถ|ปผ|จฉ|ฏฐ)", "พบพยัญชนะซ้อนตามกฎการสะกดภาษาบาลี (พยัญชนะวรรค)")
]


def classify_thai_word(word, seed_words_dict=None, orst_cache=None):
    w = word.strip()
    
    # 1. Direct match in our curated Etymological Bridge Graph
    if seed_words_dict and w in seed_words_dict:
        entry = seed_words_dict[w]
        return {
            "word": w,
            "status": "EXACT_PIE_MATCH",
            "is_indic_loanword": True,
            "origin_type": "คำยืมภาษาสันสกฤต/บาลี (Sanskrit/Pali Loanword)",
            "family": "ตระกูลภาษาอินโด-ยูโรเปียน (Proto-Indo-European / Indo-Aryan)",
            "message": f"พบข้อมูลสมบูรณ์ในระบบ Etymological Bridge! เชื่อมโยงสู่ราก PIE {entry.get('pie_root')} และคำร่วมเชื้อสายในภาษาอังกฤษ",
            "entry": entry
        }

    # 2. Check if it's a native Thai word with a known Indic formal equivalent
    if w in NATIVE_THAI_MAPPINGS:
        mapping = NATIVE_THAI_MAPPINGS[w]
        equiv = mapping["formal_equivalent"]
        entry = seed_words_dict.get(equiv) if seed_words_dict else None
        return {
            "word": w,
            "status": "NATIVE_THAI_WITH_EQUIVALENT",
            "is_indic_loanword": False,
            "origin_type": "คำไทยแท้ (Native Kra-Dai)",
            "family": mapping["native_family"],
            "suggested_word": equiv,
            "message": mapping["note"],
            "entry": entry
        }

    # 3. Check in official ORST dictionary cache if available
    orst_info = None
    if orst_cache and w in orst_cache:
        orst_info = orst_cache[w]
        etym_tag = orst_info.get("orst_etymology_tag", "")
        if "(ส." in etym_tag or "(ป." in etym_tag or "สันสกฤต" in etym_tag or "บาลี" in etym_tag:
            return {
                "word": w,
                "status": "ORST_INDIC_WORD",
                "is_indic_loanword": True,
                "origin_type": "คำยืมสันสกฤต/บาลี (ตามพจนานุกรมราชบัณฑิตยสภา)",
                "family": "ตระกูลภาษาอินโด-อารยัน (Indo-Aryan)",
                "message": f"พจนานุกรมราชบัณฑิตยสภาระบุว่าเป็นคำยืม: {etym_tag}",
                "orst_info": orst_info
            }

    # 4. Phonological heuristics for Indic words
    matched_heuristics = []
    for pattern, desc in INDIC_PATTERNS:
        if re.search(pattern, w):
            matched_heuristics.append(desc)

    if matched_heuristics:
        return {
            "word": w,
            "status": "HEURISTIC_INDIC_CANDIDATE",
            "is_indic_loanword": True,
            "origin_type": "แนวโน้มสูงเป็นคำยืมสันสกฤต/บาลี (Indo-Aryan Candidate)",
            "family": "ตระกูลภาษาอินโด-อารยัน / สันสกฤต-บาลี",
            "message": "ตรวจพบรูปแบบสัทศาสตร์และหน่วยคำสันสกฤต: " + " | ".join(matched_heuristics),
            "orst_info": orst_info
        }

    # 5. Default Native / Other
    return {
        "word": w,
        "status": "UNMAPPED_OR_NATIVE",
        "is_indic_loanword": False,
        "origin_type": "คำไทยทั่วไป / อยู่นอกขอบเขตคลังข้อมูลสาธิต",
        "family": "ตระกูลภาษาขร้า-ไท หรือคำยืมภาษาอื่น",
        "message": "คำนี้ไม่ปรากฏในคลังคำยืมสันสกฤตที่มีสายวิวัฒนาการเชื่อมโยงสู่ PIE ในระบบต้นแบบ ลองค้นหาคำตัวอย่าง เช่น มารดา, ศูนย์, ทันต, วิทยา, บิดา, สุนัข",
        "orst_info": orst_info
    }
