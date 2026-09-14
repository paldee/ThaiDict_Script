# -*- coding: utf-8 -*-
"""
Build the curated Etymological Bridge Seed Knowledge Graph (60+ comprehensive entries)
Enriched with ORST official dictionary data and phonological Grimm's law explanations.
"""

import os
import sys
import json

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SEED_DATA = [
    # -------------------------------------------------------------
    # 1. หมวดครอบครัวและเครือญาติ (Kinship & Family)
    # -------------------------------------------------------------
    {
        "thai_word": "มารดา",
        "category": "ครอบครัวและเครือญาติ",
        "pali_sanskrit_form": "mātṛ (मातृ) / mātā",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "mother, female parent",
        "pie_root": "*méh₂tēr",
        "pie_meaning": "mother",
        "sound_change_law": "Grimm's Law / Voiceless Stop Preservation: ราก PIE *m- คงตัวในทุกสาขา ทั้งสันสกฤต (mātṛ), ละติน (māter) และเจอร์แมนิก (*mōdēr)",
        "semantic_drift_score": "None (คงเดิมสมบูรณ์)",
        "semantic_drift_note": "ความหมายคงเดิมไม่เปลี่ยนแปลงตลอด 6,000 ปี ในทุกตระกูลภาษาลูกหลาน",
        "pie_branch_split": {
            "indo_iranian": "PIE *méh₂tēr → Indo-Iranian *mā́tā → Sanskrit mātṛ → Pali mātā → ภาษาไทย 'มารดา'",
            "hellenic": "PIE *méh₂tēr → Ancient Greek mētēr (μήτηρ) → English matriarch, metropolis",
            "italic": "PIE *méh₂tēr → Latin māter → French mère / English maternal, maternity, matrix",
            "germanic": "PIE *méh₂tēr → Proto-Germanic *mōdēr → Old English mōdor → English mother"
        },
        "english_cognates": [
            {
                "word": "mother",
                "derivation_path": "PIE *méh₂tēr → Proto-Germanic *mōdēr → Old English mōdor",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "สะพานเชื่อม: มารดา (mātṛ) และ mother คือคำเดียวกันที่แยกย้ายกันเมื่อ 5,000 ปีก่อน"
            },
            {
                "word": "maternal",
                "derivation_path": "PIE *méh₂tēr → Latin māternus → Old French → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "บริบททางการ/วิชาการ: maternal instincts = สัญชาตญาณความเป็นมารดา"
            },
            {
                "word": "matriarch",
                "derivation_path": "PIE *méh₂tēr → Greek mētēr + archos (ผู้นำ)",
                "origin_language": "Greek",
                "difficulty": "Advanced / SAT (C1)",
                "usage_note": "จำง่าย: มารดา + อัคร (ผู้นำ) = ผู้นำหญิงของตระกูล"
            },
            {
                "word": "matrix",
                "derivation_path": "PIE *méh₂tēr → Latin matrix (มดลูก/ต้นกำเนิด) → English",
                "origin_language": "Latin",
                "difficulty": "Academic / STEM",
                "usage_note": "เดิมแปลว่า 'แม่แบบ/มดลูกที่ให้กำเนิด' ต่อมาพัฒนาเป็นตารางเมทริกซ์ทางคณิตศาสตร์"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "Proto-Indo-European", "form": "*méh₂tēr", "meaning": "mother"},
            {"era": "~1500 BCE", "stage": "Vedic Sanskrit", "form": "mātṛ (मातृ)", "meaning": "mother"},
            {"era": "~500 BCE", "stage": "Pali", "form": "mātā (माता)", "meaning": "mother"},
            {"era": "~1300 CE", "stage": "Sukhothai Thai", "form": "มารดา", "meaning": "แม่ (ราชาศัพท์/ทางการ)"},
            {"era": "Modern", "stage": "Global Cognates", "form": "มารดา ↔ mother, maternal, matrix", "meaning": "คำร่วมสายตระกูลเดียวกัน"}
        ]
    },
    {
        "thai_word": "บิดา",
        "category": "ครอบครัวและเครือญาติ",
        "pali_sanskrit_form": "pitṛ (पितृ) / pitā",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "father, protector",
        "pie_root": "*ph₂tḗr",
        "pie_meaning": "father (เดิมอาจมาจากราก *peh₂- คุ้มครอง/เลี้ยงดู)",
        "sound_change_law": "Grimm's Law: PIE voiceless stop *p- กลายเสียงเป็น fricative *f- ในกลุ่มเจอร์แมนิก (*p- → *f-) แต่สันสกฤตและละตินยังคงเสียง [p] เดิม! ทำให้ Sanskrit pitṛ กลายเป็น English father",
        "semantic_drift_score": "None (คงเดิม)",
        "semantic_drift_note": "คำว่า 'บิดา' ในไทยยังคงเสียง [p] / [b] และความหมายดั้งเดิม เช่นเดียวกับ paternal และ patriot",
        "pie_branch_split": {
            "indo_iranian": "PIE *ph₂tḗr → Sanskrit pitṛ → Pali pitā → ภาษาไทย 'บิดา'",
            "hellenic": "PIE *ph₂tḗr → Greek patēr (πατήρ) → English patriarch, compatriot",
            "italic": "PIE *ph₂tḗr → Latin pater → English paternal, patron, patrimony, expatriate",
            "germanic": "PIE *ph₂tḗr → Proto-Germanic *fadēr → Old English fæder → English father"
        },
        "english_cognates": [
            {
                "word": "father",
                "derivation_path": "PIE *ph₂tḗr → Germanic *fadēr (Grimm's Law *p→*f) → Old English fæder",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ปิตุ/บิดา ↔ father: เสียง [p] ในสันสกฤตเปลี่ยนเป็น [f] ในอังกฤษตามกฎของกริมม์"
            },
            {
                "word": "paternal",
                "derivation_path": "PIE *ph₂tḗr → Latin paternus → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "paternal = เกี่ยวกับบิดา (ราก ปิตุ- ตรงตัว!)"
            },
            {
                "word": "patron",
                "derivation_path": "PIE *ph₂tḗr → Latin patronus (ผู้ปกป้องเสมือนพ่อ) → English",
                "origin_language": "Latin",
                "difficulty": "Advanced (B2/C1)",
                "usage_note": "ผู้อุปถัมภ์ เสมือนพ่อที่คอยดูแลสนับสนุน"
            },
            {
                "word": "patriot",
                "derivation_path": "PIE *ph₂tḗr → Greek patriōtēs (ผู้มาจากมาตุภูมิของบิดา) → English",
                "origin_language": "Greek",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ผู้รักชาติ/แผ่นดินของบรรพบุรุษบิดา (fatherland)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "Proto-Indo-European", "form": "*ph₂tḗr", "meaning": "father"},
            {"era": "~1500 BCE", "stage": "Vedic Sanskrit", "form": "pitṛ (पितृ)", "meaning": "father"},
            {"era": "~500 BCE", "stage": "Pali", "form": "pitā (पिता)", "meaning": "father"},
            {"era": "~1300 CE", "stage": "Thai", "form": "บิดา / ปิตุ", "meaning": "พ่อ (ภาษาทางการ)"},
            {"era": "Modern", "stage": "Global Cognates", "form": "บิดา ↔ father, paternal, patron", "meaning": "ตระกูลศัพท์ร่วม"}
        ]
    },
    {
        "thai_word": "ภราดา",
        "category": "ครอบครัวและเครือญาติ",
        "pali_sanskrit_form": "bhrātṛ (भ्रातृ) / bhrātā",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "brother, male sibling",
        "pie_root": "*bʰréh₂tēr",
        "pie_meaning": "brother",
        "sound_change_law": "Grimm's Law: PIE voiced aspirated stop *bʰ- กลายเสียงเป็น *b- ในเจอร์แมนิก (*bʰréh₂tēr → *brōþēr → brother) และกลายเป็น *f- ในละติน (frāter) ขณะที่สันสกฤตยังคงรูป bhr- ไว้ (bhrātṛ)",
        "semantic_drift_score": "Low (คงเดิม)",
        "semantic_drift_note": "ภราดา ในภาษาไทยใช้เรียกพี่ชายน้องชาย หรือนักบวชคริสต์ (Brother) ซึ่งตรงกับคำว่า friar ในภาษาอังกฤษ",
        "pie_branch_split": {
            "indo_iranian": "PIE *bʰréh₂tēr → Sanskrit bhrātṛ → ภาษาไทย 'ภราดา / ภราดรภาพ'",
            "hellenic": "PIE *bʰréh₂tēr → Greek phrātēr (สหายร่วมกลุ่มชน)",
            "italic": "PIE *bʰréh₂tēr → Latin frāter → English fraternal, fraternity, friar",
            "germanic": "PIE *bʰréh₂tēr → Proto-Germanic *brōþēr → Old English brōðor → English brother"
        },
        "english_cognates": [
            {
                "word": "brother",
                "derivation_path": "PIE *bʰréh₂tēr → Proto-Germanic *brōþēr → Old English brōðor",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ภราดา ↔ brother: เสียง bhr- กลายเป็น br-"
            },
            {
                "word": "fraternal",
                "derivation_path": "PIE *bʰréh₂tēr → Latin frāter → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "เช่น fraternal twins = ฝาแฝดพี่น้อง (ต่างไข่)"
            },
            {
                "word": "fraternity",
                "derivation_path": "PIE *bʰréh₂tēr → Latin frāternitās → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ตรงกับ 'ภราดรภาพ' ในภาษาไทยอย่างสมบูรณ์แบบ!"
            },
            {
                "word": "friar",
                "derivation_path": "PIE *bʰréh₂tēr → Latin frāter → Old French frere → English",
                "origin_language": "Old French",
                "difficulty": "Advanced (C1)",
                "usage_note": "ภราดา / บราเดอร์ นักบวชชายในศาสนาคริสต์"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "Proto-Indo-European", "form": "*bʰréh₂tēr", "meaning": "brother"},
            {"era": "~1500 BCE", "stage": "Vedic Sanskrit", "form": "bhrātṛ (भ्रातृ)", "meaning": "brother"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ภราดา / ภราดร", "meaning": "พี่ชายน้องชาย, ภราดรภาพ"},
            {"era": "Modern English", "stage": "English", "form": "brother, fraternal, fraternity", "meaning": "พี่น้อง"}
        ]
    },
    {
        "thai_word": "ธิดา",
        "category": "ครอบครัวและเครือญาติ",
        "pali_sanskrit_form": "dhītā (บาลี) / duhitṛ (สันสกฤต)",
        "pali_sanskrit_lang": "Pali / Sanskrit",
        "pali_sanskrit_meaning": "daughter, female child",
        "pie_root": "*dʰugh₂tḗr",
        "pie_meaning": "daughter (ดั้งเดิมอาจเกี่ยวกับการรีดนมสัตว์ในสังคมคนเลี้ยงสัตว์ยุคหินใหม่)",
        "sound_change_law": "Grimm's Law: PIE voiced aspirated stop *dʰ- เปลี่ยนเป็น *d- ในเจอร์แมนิก (*dʰugh₂tḗr → *duhtēr → daughter)",
        "semantic_drift_score": "None (คงเดิม)",
        "semantic_drift_note": "คำบาลี 'ธีตา/ธิดา' มาจากรากเดียวกับ duhitṛ และ daughter",
        "pie_branch_split": {
            "indo_iranian": "PIE *dʰugh₂tḗr → Sanskrit duhitṛ / Pali dhītā → ภาษาไทย 'ธิดา'",
            "hellenic": "PIE *dʰugh₂tḗr → Greek thygatēr (θυγάτηρ)",
            "germanic": "PIE *dʰugh₂tḗr → Proto-Germanic *duhtēr → Old English dohtor → English daughter"
        },
        "english_cognates": [
            {
                "word": "daughter",
                "derivation_path": "PIE *dʰugh₂tḗr → Proto-Germanic *duhtēr → Old English dohtor",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ธิดา (dhītā) / duhitṛ ↔ daughter มาจากราก PIE เดียวกันเป๊ะ"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*dʰugh₂tḗr", "meaning": "daughter"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "duhitṛ (दुहितृ)", "meaning": "daughter"},
            {"era": "~500 BCE", "stage": "Pali", "form": "dhītā (धीता)", "meaning": "daughter"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ธิดา", "meaning": "ลูกสาว"},
            {"era": "Modern English", "stage": "English", "form": "daughter", "meaning": "female child"}
        ]
    },
    {
        "thai_word": "ชนก",
        "category": "ครอบครัวและเครือญาติ",
        "pali_sanskrit_form": "janaka (जनक) / jananī",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "begetter, father, producer",
        "pie_root": "*ǵenh₁-",
        "pie_meaning": "to beget, give birth, produce, kind",
        "sound_change_law": "Grimm's Law / Centum-Satem split: PIE palatovelar *ǵ- กลายเสียงเป็น sibilant/affricate ในสาย Satem (Sanskrit jan-) แต่กลายเสียงเป็น velar stop *k- ในเจอร์แมนิก (*ǵ- → *k- → English kin, kind) และ *g- ในละติน/กรีก (generate, genus)",
        "semantic_drift_score": "Low (ให้กำเนิด / เผ่าพันธุ์)",
        "semantic_drift_note": "รากศัพท์ที่ให้กำเนิดศัพท์จำนวนมหาศาลทั้งในไทย (ชนก, ชนณี, ชนบท, ชาติ, ประชาชน) และอังกฤษ (generate, genre, genus, kin)",
        "pie_branch_split": {
            "indo_iranian": "PIE *ǵenh₁- → Sanskrit janati (ให้กำเนิด) / janaka → ภาษาไทย 'ชนก, ชนณี, ชน, ชาติ'",
            "hellenic": "PIE *ǵenh₁- → Greek genesis, genos → English genesis, genetics",
            "italic": "PIE *ǵenh₁- → Latin genus, generare → English generate, general, gentle",
            "germanic": "PIE *ǵenh₁- → Proto-Germanic *kunją → English kin, kind, kindred"
        },
        "english_cognates": [
            {
                "word": "generate",
                "derivation_path": "PIE *ǵenh₁- → Latin generare → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ชนก = ผู้ให้กำเนิด ↔ generate = ผลิต/สร้าง/ให้กำเนิด"
            },
            {
                "word": "genesis",
                "derivation_path": "PIE *ǵenh₁- → Greek genesis → English",
                "origin_language": "Greek",
                "difficulty": "Advanced (C1)",
                "usage_note": "จุดเริ่มต้น/กำเนิด (ราก ชน- เดียวกับ ชนก)"
            },
            {
                "word": "kin",
                "derivation_path": "PIE *ǵenh₁- → Proto-Germanic *kunją → Old English cynn",
                "origin_language": "Old English",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ญาติพี่น้องร่วมสายโลหิต (มาจากรากให้กำเนิดเดียวกัน)"
            },
            {
                "word": "genetics",
                "derivation_path": "PIE *ǵenh₁- → Greek genetikos → English",
                "origin_language": "Greek",
                "difficulty": "Academic / Science",
                "usage_note": "พันธุศาสตร์ วิทยาศาสตร์ว่าด้วยการสืบสายพันธุ์กำเนิด"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*ǵenh₁-", "meaning": "to give birth / produce"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "janaka (जनक)", "meaning": "father / producer"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ชนก / ชนณี", "meaning": "พ่อผู้ให้กำเนิด / แม่"},
            {"era": "Modern English", "stage": "English", "form": "generate, genesis, kin", "meaning": "ให้กำเนิด, วงศ์ตระกูล"}
        ]
    },

    # -------------------------------------------------------------
    # 2. หมวดร่างกายและการแพทย์ (Anatomy & Medicine)
    # -------------------------------------------------------------
    {
        "thai_word": "ทันต",
        "category": "ร่างกายและการแพทย์",
        "pali_sanskrit_form": "danta (दन्त)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "tooth",
        "pie_root": "*h₁dónts (หรือ *dent- / *dont-)",
        "pie_meaning": "tooth (ดั้งเดิมมาจาก active participle ของ *h₁ed- 'เคี้ยว/กิน' = ตัวที่ใช้เคี้ยว)",
        "sound_change_law": "Grimm's Law: PIE voiced stop *d- กลายเสียงเป็น voiceless stop *t- ในตระกูลเจอร์แมนิก (*dónts → *tanþs → tooth) ขณะที่สันสกฤตและละตินยังคงเสียง [d] (danta / dens)",
        "semantic_drift_score": "Low (คงเดิม แต่องค์ความรู้ขยายสู่สาขาแพทย์)",
        "semantic_drift_note": "ในภาษาไทยใช้ในคำประสมระดับทางการ เช่น ทันตแพทย์ ทันตกรรม ทันตแพทยศาสตร์ ในภาษาอังกฤษใช้ใน dental, dentist และยังมีคำที่น่าทึ่งอย่าง dandelion!",
        "pie_branch_split": {
            "indo_iranian": "PIE *h₁dónts → Sanskrit danta → ภาษาไทย 'ทันต / ทันต์'",
            "hellenic": "PIE *h₁dónts → Greek odōn (ὀδών) / odontos → English orthodontist",
            "italic": "PIE *h₁dónts → Latin dens / dentis → English dental, dentist, indenture",
            "germanic": "PIE *h₁dónts → Proto-Germanic *tanþs → Old English tōþ → English tooth"
        },
        "english_cognates": [
            {
                "word": "dental",
                "derivation_path": "PIE *h₁dónts → Latin dens/dentalis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ทันตแพทย์ = dental doctor (ราก ทันต- ↔ dent- ตัวเดียวกัน)"
            },
            {
                "word": "dentist",
                "derivation_path": "PIE *h₁dónts → French dentiste → English",
                "origin_language": "French / Latin",
                "difficulty": "General (A2)",
                "usage_note": "หมอฟัน"
            },
            {
                "word": "tooth",
                "derivation_path": "PIE *h₁dónts → Proto-Germanic *tanþs (Grimm's Law *d→*t) → Old English tōþ",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ฟัน (เสียง d ใน ทันต- กลายเป็น t ใน tooth ตามกฎกริมม์)"
            },
            {
                "word": "dandelion",
                "derivation_path": "PIE *h₁dónts → Latin dens leonis → French dent de lion (ฟันของสิงโต) → English dandelion",
                "origin_language": "Old French",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ว้าว! ดอกแดนดิไลออน มาจาก 'dent de lion' = ฟันของสิงโต เพราะกลีบดอกหยักเหมือนฟันสิงห์ — รากเดียวกับ ทันตแพทย์!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*h₁dónts", "meaning": "tooth (eater)"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "danta (दन्त)", "meaning": "tooth, tusk"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ทันต- / ทันตแพทย์", "meaning": "ฟัน / การรักษาฟัน"},
            {"era": "Modern English", "stage": "English", "form": "dental, dentist, dandelion, tooth", "meaning": "เกี่ยวกับฟัน"}
        ]
    },
    {
        "thai_word": "นาสา",
        "category": "ร่างกายและการแพทย์",
        "pali_sanskrit_form": "nāsā (नासा) / nāsikā",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "nose, nostril",
        "pie_root": "*néh₂s-",
        "pie_meaning": "nose",
        "sound_change_law": "Voicing and nasal stability: ราก *n- และ *s- เสถียรสูงมากทั่วทุกสาขาของ PIE (Sanskrit nāsā, Latin nāsus, Old English nosu)",
        "semantic_drift_score": "None (คงเดิม)",
        "semantic_drift_note": "นาสา/นาสิก ในไทยใช้ทางการ/ราชาศัพท์ ในอังกฤษเป็น nasal/nose",
        "pie_branch_split": {
            "indo_iranian": "PIE *néh₂s- → Sanskrit nāsā / nāsikā → ภาษาไทย 'นาสา, นาสิก'",
            "italic": "PIE *néh₂s- → Latin nāsus → English nasal",
            "germanic": "PIE *néh₂s- → Proto-Germanic *nasō → Old English nosu → English nose, nostril, nozzle"
        },
        "english_cognates": [
            {
                "word": "nose",
                "derivation_path": "PIE *néh₂s- → Proto-Germanic *nasō → Old English nosu",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "นาสา ↔ nose: เสียงต้น n- และ s- ตรงกันเป๊ะ"
            },
            {
                "word": "nasal",
                "derivation_path": "PIE *néh₂s- → Latin nasus → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "เช่น nasal spray (ยาพ่นจมูก) / nasal sound (เสียงนาสิกในวิชาภาษาศาสตร์!)"
            },
            {
                "word": "nostril",
                "derivation_path": "PIE *néh₂s- → Old English nosu + thyrel (รู) = รูจมูก",
                "origin_language": "Old English",
                "difficulty": "Intermediate (B2)",
                "usage_note": "รูจมูก (ช่องนาสา)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*néh₂s-", "meaning": "nose"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "nāsā (नासा)", "meaning": "nose"},
            {"era": "Modern Thai", "stage": "Thai", "form": "นาสา / นาสิก", "meaning": "จมูก"},
            {"era": "Modern English", "stage": "English", "form": "nose, nasal, nostril", "meaning": "จมูก"}
        ]
    },
    {
        "thai_word": "เนตร",
        "category": "ร่างกายและการแพทย์",
        "pali_sanskrit_form": "netra (नेत्र)",
        "pali_sanskrit_lang": "Sanskrit (จากราก nī = ชี้นำ, นำทาง)",
        "pali_sanskrit_meaning": "eye (ตัวนำทาง), leader, conduit",
        "pie_root": "*neyH- / *neyd-",
        "pie_meaning": "to lead, guide",
        "sound_change_law": "Semantic derivation: ดวงตาในภาษาสันสกฤตถูกนิยามเชิงอุปมาว่าเป็น 'เครื่องมือนำทาง' (จากราก nī- นำทาง + วิภัตติปัจจัย -tra เครื่องมือ)",
        "semantic_drift_score": "Medium (ผู้นำทาง → ดวงตา)",
        "semantic_drift_note": "ในพจนานุกรมราชบัณฑิตยสภา ระบุว่า 'เนตร = ดวงตา, ผู้นำทาง เช่น เนตรนารี (สตรีผู้นำทาง)'",
        "pie_branch_split": {
            "indo_iranian": "PIE *neyH- → Sanskrit netra (ผู้นำทาง/ตา) → ภาษาไทย 'เนตร, เนตรนารี'",
            "related_roots": "สำหรับ 'ดวงตา' โดยตรง เชื่อมกับ Sanskrit akṣi (อักษิ/จักษุ) ↔ PIE *h₃okʷ- ↔ English ocular, optics, eye"
        },
        "english_cognates": [
            {
                "word": "ocular",
                "derivation_path": "เทียบเคียงรากดวงตา Sanskrit akṣi (อักษิ) ↔ PIE *h₃okʷ- → Latin oculus → English ocular",
                "origin_language": "Latin",
                "difficulty": "Advanced / Medical",
                "usage_note": "คู่คำร่วม: อักษิ/จักษุ ↔ ocular/eye"
            }
        ],
        "timeline": [
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "netra (नेत्र)", "meaning": "eye / guide"},
            {"era": "Modern Thai", "stage": "Thai", "form": "เนตร", "meaning": "ดวงตา, ผู้นำทาง (เนตรนารี)"}
        ]
    },
    {
        "thai_word": "บาท",
        "category": "ร่างกายและการแพทย์",
        "pali_sanskrit_form": "pāda (पाद)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "foot, quarter, step",
        "pie_root": "*pṓds (สัมพันธการก *pedós)",
        "pie_meaning": "foot",
        "sound_change_law": "Grimm's Law: PIE voiceless stop *p- กลายเสียงเป็น *f- ในเจอร์แมนิก (*pṓds → *fōts → foot) และ voiced stop *d- กลายเสียงเป็น *t- (*d → *t)! แต่ในสันสกฤตยังคง p-d (pāda)",
        "semantic_drift_score": "Medium (เท้า → ก้าวเดิน → หนึ่งในสี่ส่วน → หน่วยเงินบาท!)",
        "semantic_drift_note": "คำว่า 'บาท' เดิมแปลว่าเท้า (พระบาท) แล้วขยายเป็น 1 ใน 4 ส่วน (จตุรบาท) จนกลายเป็นหน่วยน้ำหนักทองคำ 1 บาท และหน่วยเงินตราไทยในปัจจุบัน!",
        "pie_branch_split": {
            "indo_iranian": "PIE *pṓds → Sanskrit pāda → Pali pāda → ภาษาไทย 'บาท (เท้า, หน่วยเงิน, บทร้อยกรอง)'",
            "hellenic": "PIE *pṓds → Greek podos (ποδός) → English podiatrist, tripod, octopus (แปดเท้า)",
            "italic": "PIE *pṓds → Latin pēs / pedis → English pedal, pedestrian, pawn, pedigree, expedite",
            "germanic": "PIE *pṓds → Proto-Germanic *fōts → Old English fōt → English foot"
        },
        "english_cognates": [
            {
                "word": "foot",
                "derivation_path": "PIE *pṓds → Proto-Germanic *fōts (Grimm's Law *p→*f, *d→*t) → Old English fōt",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "บาท (pāda) ↔ foot: ทั้งสองคำมาจากรากเท้า PIE ตัวเดียวกันเป๊ะ"
            },
            {
                "word": "pedal",
                "derivation_path": "PIE *pṓds → Latin pedalis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ที่ถีบรถจักรยาน / แป้นเหยียบสำหรับเท้า (รากเดียวกับ บาท)"
            },
            {
                "word": "pedestrian",
                "derivation_path": "PIE *pṓds → Latin pedester (ผู้เดินด้วยเท้า) → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "คนเดินเท้า (บาทจาริก ในภาษาไทยโบราณ!)"
            },
            {
                "word": "pawn",
                "derivation_path": "PIE *pṓds → Latin pedo (ทหารเดินเท้า) → Old French peon → English pawn",
                "origin_language": "Old French",
                "difficulty": "Intermediate (B2)",
                "usage_note": "เบี้ยในหมากรุก (ทหารเดินเท้า)"
            },
            {
                "word": "octopus",
                "derivation_path": "PIE *oḱtṓw (แปด/อัฐ) + *pṓds (เท้า/บาท) → Greek oktōpous = แปดเท้า!",
                "origin_language": "Greek",
                "difficulty": "General (A2)",
                "usage_note": "ว้าว! octopus = อัฐ + บาท = สัตว์แปดเท้า!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*pṓds", "meaning": "foot"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "pāda (पाद)", "meaning": "foot, quarter part"},
            {"era": "~1300 CE", "stage": "Thai", "form": "บาท / พระบาท", "meaning": "เท้า, รอยเท้า, บท, เงินบาท"},
            {"era": "Modern English", "stage": "English", "form": "foot, pedal, pedestrian, octopus", "meaning": "เท้า"}
        ]
    },
    {
        "thai_word": "หัตถ์",
        "category": "ร่างกายและการแพทย์",
        "pali_sanskrit_form": "hasta (हस्त) / hattha (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "hand, trunk of elephant",
        "pie_root": "*gʰes-",
        "pie_meaning": "hand, to take, seize",
        "sound_change_law": "Aspiration preservation: สันสกฤตแปลง *gʰes- กลายเป็น hasta (h-)",
        "semantic_drift_score": "Low (คงเดิม)",
        "semantic_drift_note": "หัตถ์ = มือ ใช้ในราชาศัพท์และคำวิชาชีพ เช่น หัตถการ หัตถกรรม หัตถศึกษา",
        "pie_branch_split": {
            "indo_iranian": "PIE *gʰes- → Sanskrit hasta → Pali hattha → ภาษาไทย 'หัตถ์, หัตถกรรม'",
            "hellenic": "PIE *gʰes- → Greek cheir (χείρ) → English surgery (cheirourgikē = งานมือแพทย์!), chiropractor"
        },
        "english_cognates": [
            {
                "word": "surgery",
                "derivation_path": "Greek cheir (มือ, ราก PIE เดียวกับ hasta) + ergon (งาน) → cheirourgia → Old French cirurgie → English surgery",
                "origin_language": "Greek via French",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ว้าว! surgery เดิมแปลว่า 'หัตถการ' (การทำงานรักษาด้วยมือ) ซึ่งหัตถ์ ↔ cheir รากเดียวกัน!"
            }
        ],
        "timeline": [
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "hasta (हस्त)", "meaning": "hand"},
            {"era": "Modern Thai", "stage": "Thai", "form": "หัตถ์ / หัตถกรรม", "meaning": "มือ, ฝีมือ"}
        ]
    },
    {
        "thai_word": "หทัย",
        "category": "ร่างกายและการแพทย์",
        "pali_sanskrit_form": "hṛdaya (हृदय) / hadaya (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "heart, mind, soul",
        "pie_root": "*ḱērd- (สัมพันธการก *kṛd-)",
        "pie_meaning": "heart",
        "sound_change_law": "Grimm's Law: PIE voiceless palatovelar *ḱ- กลายเสียงเป็น *h- ในตระกูลเจอร์แมนิก (*ḱērd- → *hertô → heart) และเปลี่ยนเป็น h- ใน Indo-Iranian (hṛdaya) ขณะที่ Latin รักษาเป็น [k] (cor / cordis) และ Greek เป็น kardia",
        "semantic_drift_score": "None (หัวใจ/จิตใจ)",
        "semantic_drift_note": "หทัย / หฤทัย ในภาษาไทยแปลว่าหัวใจหรือใจ เช่นเดียวกับ cardiac และ cordial",
        "pie_branch_split": {
            "indo_iranian": "PIE *ḱērd- → Sanskrit hṛdaya → Pali hadaya → ภาษาไทย 'หทัย, หฤทัย'",
            "hellenic": "PIE *ḱērd- → Greek kardia (καρδία) → English cardiac, cardiology, electrocardiogram",
            "italic": "PIE *ḱērd- → Latin cor / cordis → English cordial, courage (ความกล้าจากหัวใจ), accord, discord",
            "germanic": "PIE *ḱērd- → Proto-Germanic *hertô (Grimm's Law *ḱ→*h) → Old English heorte → English heart"
        },
        "english_cognates": [
            {
                "word": "heart",
                "derivation_path": "PIE *ḱērd- → Proto-Germanic *hertô → Old English heorte",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "หฤทัย ↔ heart: รากหัวใจเดียวกันเป๊ะ เสียง h- เริ่มต้นตรงกัน"
            },
            {
                "word": "cardiac",
                "derivation_path": "PIE *ḱērd- → Greek kardia → English",
                "origin_language": "Greek",
                "difficulty": "Intermediate / Medical (B2)",
                "usage_note": "cardiac arrest = ภาวะหัวใจหยุดเต้น (หฤทัยวาย)"
            },
            {
                "word": "cordial",
                "derivation_path": "PIE *ḱērd- → Latin cordialis (มาจากใจ) → English",
                "origin_language": "Latin",
                "difficulty": "Advanced (C1)",
                "usage_note": "จริงใจ / อบอุ่นจากใจ (cordial welcome = การต้อนรับด้วยน้ำใสใจจริง)"
            },
            {
                "word": "courage",
                "derivation_path": "PIE *ḱērd- → Latin cor → Old French corage (ใจสู้) → English",
                "origin_language": "Old French",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ความกล้าหาญ (ดั้งเดิมแปลว่า 'มีหัวใจสู้')"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*ḱērd-", "meaning": "heart"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "hṛdaya (हृदय)", "meaning": "heart, core"},
            {"era": "~500 BCE", "stage": "Pali", "form": "hadaya (हदय)", "meaning": "heart"},
            {"era": "Modern Thai", "stage": "Thai", "form": "หทัย / หฤทัย", "meaning": "หัวใจ, ดวงใจ"},
            {"era": "Modern English", "stage": "English", "form": "heart, cardiac, cordial, courage", "meaning": "หัวใจ, ความจริงใจ"}
        ]
    },

    # -------------------------------------------------------------
    # 3. หมวดตัวเลขและคณิตศาสตร์ (Numbers & Mathematics)
    # -------------------------------------------------------------
    {
        "thai_word": "ศูนย์",
        "category": "ตัวเลขและคณิตศาสตร์",
        "pali_sanskrit_form": "śūnya (शून्य)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "empty, void, hollow, swollen space",
        "pie_root": "*ḱewH-",
        "pie_meaning": "to swell, hollow, empty space",
        "sound_change_law": "Cultural & Semantic Transmission: จากราก PIE *ḱewH- (กลวง/ว่าง) → สันสกฤต śūnya (สุญญตา/ความว่าง) → นักคณิตศาสตร์อินเดีย (Brahmagupta) คิดค้นเลข 0 → ชาวอาหรับแปลคำว่า śūnya เป็น sifr (صفر ว่างเปล่า) → ภาษาละตินยุคกลางยืมเป็น zephirum → ภาษาอิตาลี zero → ภาษาอังกฤษ zero! ขณะที่สายละตินโดยตรงจาก *ḱewH- ให้กำเนิดคำว่า cave (ถ้ำ) และ cavity (โพรง)!",
        "semantic_drift_score": "High (ปรัชญาความว่างเปล่า → ตัวเลข 0)",
        "semantic_drift_note": "นี่คือหนึ่งในมหากาพย์การเดินทางของคำศัพท์ที่ยิ่งใหญ่ที่สุดในประวัติศาสตร์มนุษยชาติ: โลกตะวันตกรับเลข '0' จากอินเดียผ่านคำแปลภาษาอาหรับ คำว่า 'ศูนย์' ในภาษาไทยจึงเป็นญาติกับคำว่า 'zero' ในภาษาอังกฤษ!",
        "pie_branch_split": {
            "indo_iranian": "PIE *ḱewH- → Sanskrit śūnya (ความว่าง/เลขศูนย์) → ภาษาไทย 'ศูนย์'",
            "arabic_transmission": "Sanskrit śūnya (ว่าง) → แปลเป็น Arabic ṣifr (ว่าง) → Italian zero / cipher → English zero, cipher",
            "italic_direct": "PIE *ḱewH- → Latin cavus (กลวง) → English cave, cavity, cavern"
        },
        "english_cognates": [
            {
                "word": "zero",
                "derivation_path": "Sanskrit śūnya → Arabic ṣifr → Medieval Latin zephirum → Italian zero → English zero",
                "origin_language": "Arabic / Sanskrit transmission",
                "difficulty": "General (A1)",
                "usage_note": "ว้าวระดับโลก! zero คือคำแปลโดยตรงของคำว่า ศูนย์ (śūnya) ที่เดินทางผ่านอารยธรรมอิสลามสู่ยุโรป"
            },
            {
                "word": "cipher",
                "derivation_path": "Sanskrit śūnya → Arabic ṣifr → Old French cifre → English cipher (รหัสลับ / เลขศูนย์)",
                "origin_language": "Arabic",
                "difficulty": "Advanced (B2/C1)",
                "usage_note": "การเข้ารหัส / ตัวเลขลับ (เดิมแปลว่าเลขศูนย์)"
            },
            {
                "word": "cave",
                "derivation_path": "PIE *ḱewH- → Latin cavus (ที่กลวงว่าง) → English cave",
                "origin_language": "Latin",
                "difficulty": "General (A2)",
                "usage_note": "ถ้ำ (โพรงกลวงที่ว่างเปล่าในภูเขา รากเดียวกับ ศูนย์)"
            },
            {
                "word": "cavity",
                "derivation_path": "PIE *ḱewH- → Latin cavitas → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate / Medical (B2)",
                "usage_note": "โพรงฟันผุ / ช่องว่างในร่างกาย (ทันตแพทย์มักเจอบ่อย!)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*ḱewH-", "meaning": "hollow, swollen empty"},
            {"era": "~600 BCE", "stage": "Vedic / Buddhist", "form": "śūnya (शून्य)", "meaning": "สุญญตา ความว่างเปล่า"},
            {"era": "628 CE", "stage": "Brahmagupta (India)", "form": "śūnya", "meaning": "คิดค้นเลขศูนย์ทางคณิตศาสตร์"},
            {"era": "825 CE", "stage": "Al-Khwarizmi (Baghdad)", "form": "ṣifr (صفر)", "meaning": "แปลคำว่า śūnya เป็นภาษาอาหรับ"},
            {"era": "1202 CE", "stage": "Fibonacci (Italy)", "form": "zephirum → zero", "meaning": "นำเลขศูนย์สู่อิตาลีและยุโรป"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ศูนย์ (๐)", "meaning": "เลข 0, จุดกึ่งกลาง"}
        ]
    },
    {
        "thai_word": "ทวิ",
        "category": "ตัวเลขและคณิตศาสตร์",
        "pali_sanskrit_form": "dvi (द्वि) / dvi-",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "two, twice, twofold",
        "pie_root": "*dwóh₁ (หรือ *dwi-)",
        "pie_meaning": "two",
        "sound_change_law": "Grimm's Law: PIE voiced stop *d- กลายเสียงเป็น voiceless stop *t- ในตระกูลเจอร์แมนิก (*dwóh₁ → *twai → two, twin, twice) ขณะที่ Latin และ Sanskrit ยังคงเสียง [d] (dvi, duo)",
        "semantic_drift_score": "None (จำนวนสอง)",
        "semantic_drift_note": "ทวิ ในภาษาไทย (เช่น ทวิภาคี, ทวิภพ, ทศทัศน์) ตรงกับ two, duo, dual, doubt ในภาษาอังกฤษ",
        "pie_branch_split": {
            "indo_iranian": "PIE *dwóh₁ → Sanskrit dvi → ภาษาไทย 'ทวิ, โท'",
            "hellenic": "PIE *dwóh₁ → Greek duo (δύο) / di- → English diploma (พับสองทบ), dioxide",
            "italic": "PIE *dwóh₁ → Latin duo / dualis → English dual, duo, duel, doubt (ใจแบ่งเป็นสอง!)",
            "germanic": "PIE *dwóh₁ → Proto-Germanic *twai (Grimm's Law *d→*t) → Old English twā → English two, twin, twice, twilight, between"
        },
        "english_cognates": [
            {
                "word": "two",
                "derivation_path": "PIE *dwóh₁ → Proto-Germanic *twai → Old English twā",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ทวิ ↔ two: เสียง d ใน ทวิ กลายเป็น t ใน two ตามกฎกริมม์"
            },
            {
                "word": "dual",
                "derivation_path": "PIE *dwóh₁ → Latin dualis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "คู่ / สองด้าน เช่น dual core, dual citizen"
            },
            {
                "word": "doubt",
                "derivation_path": "PIE *dwóh₁ → Latin dubitare (ใจลังเลระหว่างสองทาง) → English doubt",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ความสงสัย ลังเล (ดั้งเดิมแปลว่า 'จิตใจแยกเป็น 2 ฝ่าย')"
            },
            {
                "word": "twilight",
                "derivation_path": "PIE *dwóh₁ → Old English twi- (สอง) + lēoht (แสง) = แสงก้ำกึ่งสองเวลา",
                "origin_language": "Old English",
                "difficulty": "Intermediate (B2)",
                "usage_note": "แสงยามโพล้เพล้ (รอยต่อระหว่างกลางวันกับกลางคืน)"
            },
            {
                "word": "between",
                "derivation_path": "PIE *dwóh₁ → Old English betwēonum (ณ ท่ามกลางสองสิ่ง)",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ระหว่างสองสิ่ง"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*dwóh₁", "meaning": "two"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "dvi (द्वि)", "meaning": "two"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ทวิ / ทวิภพ", "meaning": "สอง"},
            {"era": "Modern English", "stage": "English", "form": "two, dual, doubt, twin", "meaning": "จำนวนสอง, ฝาแฝด"}
        ]
    },
    {
        "thai_word": "ตรี",
        "category": "ตัวเลขและคณิตศาสตร์",
        "pali_sanskrit_form": "tri (त्रि)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "three",
        "pie_root": "*tréyes",
        "pie_meaning": "three",
        "sound_change_law": "Grimm's Law: PIE voiceless stop *t- กลายเสียงเป็น voiceless fricative *þ- (th-) ในเจอร์แมนิก (*tréyes → *þrīz → three) แต่ภาษาสันสกฤตและละตินยังคงรูป tr- ไว้ (tri, tres)",
        "semantic_drift_score": "None (จำนวนสาม)",
        "semantic_drift_note": "ตรี ในภาษาไทย (ตรีมูรติ, ปริญญาตรี, ไตรลักษณ์) ↔ three, triangle, triple, trinity ในภาษาอังกฤษ",
        "pie_branch_split": {
            "indo_iranian": "PIE *tréyes → Sanskrit tri / Pali ti → ภาษาไทย 'ตรี, ไตร'",
            "hellenic": "PIE *tréyes → Greek treis (τρεῖς) / tri- → English trigonometry, tripod",
            "italic": "PIE *tréyes → Latin trēs / tri- → English trio, triple, triangle, trinity",
            "germanic": "PIE *tréyes → Proto-Germanic *þrīz (Grimm's Law *t→*th) → Old English þrēo → English three"
        },
        "english_cognates": [
            {
                "word": "three",
                "derivation_path": "PIE *tréyes → Proto-Germanic *þrīz → Old English þrēo",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ตรี ↔ three: เสียง tr- กลายเป็น th-r-"
            },
            {
                "word": "triangle",
                "derivation_path": "PIE *tréyes → Latin triangulum → English",
                "origin_language": "Latin",
                "difficulty": "General (A2)",
                "usage_note": "สามเหลี่ยม (ตรี + โกณ ในภาษาไทย = triangle!)"
            },
            {
                "word": "triple",
                "derivation_path": "PIE *tréyes → Latin triplus → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "สามเท่า / สามชั้น"
            },
            {
                "word": "trinity",
                "derivation_path": "PIE *tréyes → Latin trinitas → English",
                "origin_language": "Latin",
                "difficulty": "Advanced (B2/C1)",
                "usage_note": "ตรีเอกภาพ (องค์สามในหนึ่งเดียว)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*tréyes", "meaning": "three"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "tri (त्रि)", "meaning": "three"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ตรี / ไตร", "meaning": "สาม"},
            {"era": "Modern English", "stage": "English", "form": "three, triple, triangle", "meaning": "จำนวนสาม"}
        ]
    },
    {
        "thai_word": "เบญจ",
        "category": "ตัวเลขและคณิตศาสตร์",
        "pali_sanskrit_form": "pañca (पञ्च)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "five",
        "pie_root": "*pénkʷe",
        "pie_meaning": "five (สัมพันธ์กับนิ้วมือ 5 นิ้ว)",
        "sound_change_law": "Grimm's Law: PIE voiceless stop *p- กลายเสียงเป็น *f- ในเจอร์แมนิก (*pénkʷe → *fimf → five) และ labiovelar *kʷ กลายเสียงเป็น labial f- หรือ c-",
        "semantic_drift_score": "None (จำนวนห้า) + วัฒนธรรมเครื่องดื่ม punch",
        "semantic_drift_note": "เบญจ/ปัญจ ในภาษาไทย (เบญจมาศ, เบญจศีล, ปัญจวัคคีย์) ↔ five, pentagon และที่น่าทึ่งคือเครื่องดื่ม 'พั้นช์' (Punch) มาจากคำว่าปัญจะ!",
        "pie_branch_split": {
            "indo_iranian": "PIE *pénkʷe → Sanskrit pañca → ภาษาไทย 'เบญจ, ปัญจ'",
            "hellenic": "PIE *pénkʷe → Greek pente (πέντε) → English pentagon, pentathlon",
            "italic": "PIE *pénkʷe → Latin quīnque → English quintet, quintessence",
            "germanic": "PIE *pénkʷe → Proto-Germanic *fimf (Grimm's Law *p→*f) → Old English fīf → English five"
        },
        "english_cognates": [
            {
                "word": "five",
                "derivation_path": "PIE *pénkʷe → Proto-Germanic *fimf → Old English fīf",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "เบญจ/ปัญจ ↔ five: เสียง p- กลายเป็น f-"
            },
            {
                "word": "pentagon",
                "derivation_path": "PIE *pénkʷe → Greek pentagōnon → English",
                "origin_language": "Greek",
                "difficulty": "Intermediate (B1)",
                "usage_note": "รูปห้าเหลี่ยม / กระทรวงกลาโหมสหรัฐฯ (เพนตากอน)"
            },
            {
                "word": "punch",
                "derivation_path": "Sanskrit pañca (ห้า) → Hindi pañc (เครื่องดื่มผสม 5 ชนิด: เหล้า, น้ำตาล, มะนาว, น้ำ, ชา/เครื่องเทศ) → English punch",
                "origin_language": "Hindi / Sanskrit loan in English",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ว้าว! เครื่องดื่ม 'น้ำพั้นช์' (Punch) เดิมแปลว่า 'เครื่องดื่มผสม 5 อย่าง' มาจากคำว่า ปัญจะ โดยตรง!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*pénkʷe", "meaning": "five"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "pañca (पञ्च)", "meaning": "five"},
            {"era": "Modern Thai", "stage": "Thai", "form": "เบญจ / ปัญจ", "meaning": "ห้า"},
            {"era": "Modern English", "stage": "English", "form": "five, pentagon, punch", "meaning": "จำนวนห้า, เครื่องดื่ม 5 อย่าง"}
        ]
    },
    {
        "thai_word": "ทศ",
        "category": "ตัวเลขและคณิตศาสตร์",
        "pali_sanskrit_form": "daśa (दश)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "ten",
        "pie_root": "*déḱm̥",
        "pie_meaning": "ten",
        "sound_change_law": "Grimm's Law: PIE voiced stop *d- กลายเสียงเป็น *t- ในเจอร์แมนิก (*déḱm̥ → *tehun → ten) และ palatovelar *ḱ กลายเสียงเป็น *ś ในสันสกฤต (daśa)",
        "semantic_drift_score": "None (สิบ) + ปฏิทินโรมัน December",
        "semantic_drift_note": "ทศ (ทศกัณฐ์ = สิบหน้า, ทศนิยม = decimal, ทศวรรษ = decade) ↔ ten, decade, decimal และเดือน December!",
        "pie_branch_split": {
            "indo_iranian": "PIE *déḱm̥ → Sanskrit daśa → ภาษาไทย 'ทศ, ทศวรรษ, ทศกัณฐ์'",
            "hellenic": "PIE *déḱm̥ → Greek deka (δέκα) → English decade, decalogue",
            "italic": "PIE *déḱm̥ → Latin decem → English decimal, decimate, December (เดือนที่ 10 ในปฏิทินโรมันโบราณ!)",
            "germanic": "PIE *déḱm̥ → Proto-Germanic *tehun (Grimm's Law *d→*t) → Old English tēn → English ten"
        },
        "english_cognates": [
            {
                "word": "ten",
                "derivation_path": "PIE *déḱm̥ → Proto-Germanic *tehun → Old English tēn",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ทศ ↔ ten: เสียง d- ใน ทศ กลายเป็น t- ใน ten"
            },
            {
                "word": "decade",
                "derivation_path": "PIE *déḱm̥ → Greek dekas → English",
                "origin_language": "Greek",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ทศวรรษ (รอบ 10 ปี)"
            },
            {
                "word": "decimal",
                "derivation_path": "PIE *déḱm̥ → Latin decimalis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ทศนิยม (ระบบฐาน 10 ทางคณิตศาสตร์)"
            },
            {
                "word": "December",
                "derivation_path": "PIE *déḱm̥ → Latin December (เดือนที่ 10 นับจากมีนาคม)",
                "origin_language": "Latin",
                "difficulty": "General (A1)",
                "usage_note": "ธันวาคม เดิมคือเดือนที่ 10 ในปฏิทินโรมันโบราณ (ราก ทศ- ตรงตัว!)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*déḱm̥", "meaning": "ten"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "daśa (दश)", "meaning": "ten"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ทศ- / ทศวรรษ", "meaning": "สิบ"},
            {"era": "Modern English", "stage": "English", "form": "ten, decade, decimal, December", "meaning": "จำนวนสิบ"}
        ]
    },

    # -------------------------------------------------------------
    # 4. หมวดปัญญา วิทยาศาสตร์ และความคิด (Mind & Knowledge)
    # -------------------------------------------------------------
    {
        "thai_word": "วิทยา",
        "category": "ปัญญา วิทยาศาสตร์ และความคิด",
        "pali_sanskrit_form": "vidyā (विद्या) / vid",
        "pali_sanskrit_lang": "Sanskrit (จากราก vid = รู้, เห็น)",
        "pali_sanskrit_meaning": "knowledge, science, learning",
        "pie_root": "*weyd-",
        "pie_meaning": "to see, to perceive visually (ดังนั้น 'การเห็น' นำไปสู่ 'การรู้')",
        "sound_change_law": "Grimm's Law: PIE voiced stop *d- กลายเสียงเป็น *t- ในเจอร์แมนิก (*weyd- → *witaną → wit, wise, wisdom) ขณะที่สายละตินรักษาเสียง [d] (*weyd- → vidēre → video, vision) และภาษากรีกกลายเป็น eidos → idea!",
        "semantic_drift_score": "Low (การมองเห็น → ความรู้แจ้ง)",
        "semantic_drift_note": "นี่คือความน่าทึ่งขั้นสุดยอด: วิทยา (ความรู้/วิชาการ) และ video (ภาพวิดีโอ) มาจากรากเดียวกันเป๊ะ! 'การเห็น' (video) คือบ่อเกิดของ 'ความรู้' (วิทยา)",
        "pie_branch_split": {
            "indo_iranian": "PIE *weyd- → Sanskrit vidyā (ความรู้) / veda (คัมภีร์พระเวท) → ภาษาไทย 'วิทยา, วิทย์, พระเวท'",
            "hellenic": "PIE *weyd- → Greek idein (เห็น) → idea (สิ่งที่เห็นในมโนภาพ), history (การสืบรู้เห็น)",
            "italic": "PIE *weyd- → Latin vidēre (มองเห็น) → English video, vision, visual, evident, provide",
            "germanic": "PIE *weyd- → Proto-Germanic *witaną (Grimm's Law *d→*t) → Old English witan → English wit, wise, wisdom, witness"
        },
        "english_cognates": [
            {
                "word": "video",
                "derivation_path": "PIE *weyd- → Latin video (ฉันมองเห็น) → English video",
                "origin_language": "Latin",
                "difficulty": "General (A1)",
                "usage_note": "ตะลึง! วิทยา และ video มาจากราก PIE *weyd- เดียวกัน: มองเห็น → เกิดความรู้!"
            },
            {
                "word": "vision",
                "derivation_path": "PIE *weyd- → Latin visio → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "วิสัยทัศน์ / การมองเห็นภาพอนาคต"
            },
            {
                "word": "evident",
                "derivation_path": "PIE *weyd- → Latin evidens (เห็นประจักษ์ชัด) → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "เห็นได้ชัดแจ้ง / ประจักษ์พยาน"
            },
            {
                "word": "wise",
                "derivation_path": "PIE *weyd- → Proto-Germanic *wīsaz → Old English wīs",
                "origin_language": "Old English",
                "difficulty": "General (A2)",
                "usage_note": "ชาญฉลาด / มีปัญญาความรู้ (รากเดียวกับ พระเวท และ วิทยา)"
            },
            {
                "word": "idea",
                "derivation_path": "PIE *weyd- → Greek idea (รูปแบบที่มองเห็น) → English",
                "origin_language": "Greek",
                "difficulty": "General (A1)",
                "usage_note": "ความคิด / ความเข้าใจในใจ"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*weyd-", "meaning": "to see, perceive"},
            {"era": "~1500 BCE", "stage": "Vedic Sanskrit", "form": "vidyā (विद्या) / veda", "meaning": "knowledge, sacred lore"},
            {"era": "~1300 CE", "stage": "Thai", "form": "วิทยา / วิทยาการ", "meaning": "ความรู้, ศาสตร์"},
            {"era": "Modern English", "stage": "English", "form": "video, vision, wise, idea", "meaning": "มองเห็น, ความรู้, ปัญญา"}
        ]
    },
    {
        "thai_word": "ญาณ",
        "category": "ปัญญา วิทยาศาสตร์ และความคิด",
        "pali_sanskrit_form": "jñāna (ज्ञान) / ñāṇa (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "higher knowledge, cognition, gnosis",
        "pie_root": "*ǵneh₃-",
        "pie_meaning": "to know, recognize",
        "sound_change_law": "Grimm's Law & Voicing: PIE palatovelar *ǵ- กลายเสียงเป็น [k] ในตระกูลเจอร์แมนิก (*ǵneh₃- → *knēaną → know) และกลายเป็น gn- ในละติน/กรีก (cognition, gnosis) ขณะที่สันสกฤตออกเสียง jñ- (ชญาณ/ญาณ)",
        "semantic_drift_score": "Low (การรู้แจ้ง / ความรู้)",
        "semantic_drift_note": "ญาณ ในภาษาไทย แปลว่าปรีชาหยั่งรู้ ↔ know, cognition, recognize, gnosis ในภาษาอังกฤษ ทั้งหมดมาจากราก *ǵneh₃-",
        "pie_branch_split": {
            "indo_iranian": "PIE *ǵneh₃- → Sanskrit jñāna → Pali ñāṇa → ภาษาไทย 'ญาณ, ชญาณ, ปรัชญา'",
            "hellenic": "PIE *ǵneh₃- → Greek gnōsis (γνῶσις) → English gnosis, diagnosis, prognosis",
            "italic": "PIE *ǵneh₃- → Latin (g)noscere → English cognition, recognize, ignore, noble",
            "germanic": "PIE *ǵneh₃- → Proto-Germanic *knēaną (Grimm's Law *ǵ→*k) → Old English cnāwan → English know, knowledge"
        },
        "english_cognates": [
            {
                "word": "know",
                "derivation_path": "PIE *ǵneh₃- → Proto-Germanic *knēaną → Old English cnāwan",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ญาณ ↔ know: ตัวอักษร k ใน know เดิมออกเสียง [kn-] เช่นเดียวกับ jñ- ในสันสกฤต!"
            },
            {
                "word": "knowledge",
                "derivation_path": "PIE *ǵneh₃- → Old English cnāwleċ",
                "origin_language": "Old English",
                "difficulty": "General (A2)",
                "usage_note": "ความรู้ (คำแปลภาษาอังกฤษตรงตัวของ 'ญาณ')"
            },
            {
                "word": "cognition",
                "derivation_path": "PIE *ǵneh₃- → Latin cognoscere (รู้ร่วมกัน) → English",
                "origin_language": "Latin",
                "difficulty": "Advanced / Science (C1)",
                "usage_note": "กระบวนการรู้คิดทางสมอง (จิตวิทยา/ประสาทวิทยาศาสตร์)"
            },
            {
                "word": "diagnosis",
                "derivation_path": "PIE *ǵneh₃- → Greek dia- (ทะลุปรุโปร่ง) + gnosis (การรู้) → English diagnosis",
                "origin_language": "Greek",
                "difficulty": "Intermediate / Medical (B2)",
                "usage_note": "การวินิจฉัยโรค (รู้ทะลุปรุโปร่งว่าเกิดจากอะไร)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*ǵneh₃-", "meaning": "to know, recognize"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "jñāna (ज्ञान)", "meaning": "higher spiritual knowledge"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ญาณ / ญาณทัศนะ", "meaning": "ปรีชาหยั่งรู้"},
            {"era": "Modern English", "stage": "English", "form": "know, knowledge, cognition, diagnosis", "meaning": "การรับรู้, ความรู้"}
        ]
    },
    {
        "thai_word": "มโน",
        "category": "ปัญญา วิทยาศาสตร์ และความคิด",
        "pali_sanskrit_form": "manas (मनस्) / mano (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "mind, intellect, thought",
        "pie_root": "*men-",
        "pie_meaning": "to think, mind, remember, spirit",
        "sound_change_law": "Nasal root preservation: ราก *m-n- มีความเสถียรอย่างน่าทึ่งทั่วทั้งตระกูลภาษาอินโด-ยูโรเปียน (Sanskrit manas, Greek menos, Latin mens/mentis, Germanic *gaminþiją)",
        "semantic_drift_score": "Low (จิตใจ/ความคิด)",
        "semantic_drift_note": "มโน/มนัส (มโนกรรม, มโนคติ, มโนภาพ) ↔ mind, mental, mention, memory, monument ในภาษาอังกฤษ!",
        "pie_branch_split": {
            "indo_iranian": "PIE *men- → Sanskrit manas → Pali mano → ภาษาไทย 'มโน, มนัส, มติ, มนต์'",
            "hellenic": "PIE *men- → Greek menos (จิตวิญญาณ) / mnasthai → English mnemonic, mania",
            "italic": "PIE *men- → Latin mens / mentis → English mental, mention, monument, monitor",
            "germanic": "PIE *men- → Proto-Germanic *gamundiz → Old English mynd → English mind"
        },
        "english_cognates": [
            {
                "word": "mind",
                "derivation_path": "PIE *men- → Proto-Germanic *gamundiz → Old English mynd",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "มโน ↔ mind: รากความคิดและจิตใจเดียวกันเป๊ะ!"
            },
            {
                "word": "mental",
                "derivation_path": "PIE *men- → Latin mentalis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ทางจิตใจ / ทางสติปัญญา (เช่น mental health = สุขภาพจิต)"
            },
            {
                "word": "monument",
                "derivation_path": "PIE *men- → Latin monere (เตือนความจำ) → monumentum → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "อนุสาวรีย์ (สิ่งก่อสร้างเพื่อเตือนความทรงจำในมโนนึก)"
            },
            {
                "word": "mnemonic",
                "derivation_path": "PIE *men- → Greek mnēmonikos (ช่วยจำ) → English",
                "origin_language": "Greek",
                "difficulty": "Advanced (C1)",
                "usage_note": "เทคนิคช่วยจำ (เช่น จำศัพท์ผ่านรากมโน!)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*men-", "meaning": "to think, remember"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "manas (मनस्)", "meaning": "mind, thought, intention"},
            {"era": "Modern Thai", "stage": "Thai", "form": "มโน / มโนภาพ", "meaning": "ใจ, ความคิดคำนึง"},
            {"era": "Modern English", "stage": "English", "form": "mind, mental, memory", "meaning": "จิตใจ, ความคิด"}
        ]
    },
    {
        "thai_word": "นาม",
        "category": "ปัญญา วิทยาศาสตร์ และความคิด",
        "pali_sanskrit_form": "nāman (नामन्) / nāma (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "name, characteristic, noun",
        "pie_root": "*h₁nómn̥",
        "pie_meaning": "name",
        "sound_change_law": "Nasal preservation: สันสกฤต nāman, ละติน nōmen, โอลด์อิงลิช nama ทั้งหมดสืบทอดจากรูป *h₁nómn̥ อย่างตรงตัว",
        "semantic_drift_score": "None (ชื่อ / คำนาม)",
        "semantic_drift_note": "นาม (ชื่อ, คำนาม, นามธรรม) ↔ name, noun, nominal, nominate, anonymous",
        "pie_branch_split": {
            "indo_iranian": "PIE *h₁nómn̥ → Sanskrit nāman → Pali nāma → ภาษาไทย 'นาม, นามธรรม, ฉายานาม'",
            "hellenic": "PIE *h₁nómn̥ → Greek onoma (ὄνομα) → English anonymous (นิรนาม!), pseudonym",
            "italic": "PIE *h₁nómn̥ → Latin nōmen → English noun, nominate, nominal",
            "germanic": "PIE *h₁nómn̥ → Proto-Germanic *namô → Old English nama → English name"
        },
        "english_cognates": [
            {
                "word": "name",
                "derivation_path": "PIE *h₁nómn̥ → Proto-Germanic *namô → Old English nama",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "นาม ↔ name: ออกเสียงและแปลเหมือนกันทุกประการ!"
            },
            {
                "word": "noun",
                "derivation_path": "PIE *h₁nómn̥ → Latin nomen → Anglo-Norman noun → English noun",
                "origin_language": "Anglo-Norman / Latin",
                "difficulty": "General (A1)",
                "usage_note": "คำนาม ในวิชาไวยากรณ์ (รากเดียวกับ นาม ในภาษาไทย)"
            },
            {
                "word": "anonymous",
                "derivation_path": "Greek an- (ไม่/นิร-) + onoma (ชื่อ/นาม) → English anonymous",
                "origin_language": "Greek",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ว้าว! นิรนาม = an- (นิร) + onoma (นาม) = anonymous โครงสร้างศัพท์เดียวกันเป๊ะ!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*h₁nómn̥", "meaning": "name"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "nāman (नामन्)", "meaning": "name"},
            {"era": "Modern Thai", "stage": "Thai", "form": "นาม / นิรนาม", "meaning": "ชื่อ, ไร้ชื่อ"},
            {"era": "Modern English", "stage": "English", "form": "name, noun, anonymous", "meaning": "ชื่อ, คำนาม, นิรนาม"}
        ]
    },

    # -------------------------------------------------------------
    # 5. หมวดธรรมชาติ สรรพสิ่ง และจักรวาล (Cosmos & Nature)
    # -------------------------------------------------------------
    {
        "thai_word": "สุริยะ",
        "category": "ธรรมชาติ สรรพสิ่ง และจักรวาล",
        "pali_sanskrit_form": "sūrya (सूर्य) / sūriya (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "sun, sun deity",
        "pie_root": "*sóh₂wl̥ (หรือ *sāwel-)",
        "pie_meaning": "sun",
        "sound_change_law": "Heteroclitic declension & Grimm's Law: ราก PIE สลับระหว่างรูป l/r (*sāwel- / *sūrya-) ส่งผลให้สายสันสกฤตพัฒนาเป็น sūrya ขณะที่ละตินเป็น sōl และเจอร์แมนิกกลายเป็น sunna (*sunnǭ → sun)",
        "semantic_drift_score": "None (ดวงอาทิตย์)",
        "semantic_drift_note": "สุริยะ/สุริยัน/สุริยา ในภาษาไทย ↔ sun, solar, solstice และ helium (ผ่านรากกรีก helios) ในภาษาอังกฤษ",
        "pie_branch_split": {
            "indo_iranian": "PIE *sóh₂wl̥ → Sanskrit sūrya → Pali sūriya → ภาษาไทย 'สุริยะ, สุริยัน, สุริยา'",
            "hellenic": "PIE *sóh₂wl̥ → Greek hēlios (ἥλιος) → English helium (ก๊าซฮีเลียมที่ค้นพบบนดวงอาทิตย์!), heliocentric",
            "italic": "PIE *sóh₂wl̥ → Latin sōl → English solar, solstice (สุริยคราส/ครีษมายัน)",
            "germanic": "PIE *sóh₂wl̥ → Proto-Germanic *sunnǭ → Old English sunne → English sun, Sunday"
        },
        "english_cognates": [
            {
                "word": "sun",
                "derivation_path": "PIE *sóh₂wl̥ → Proto-Germanic *sunnǭ → Old English sunne",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "สุริย- ↔ sun: รากดวงอาทิตย์เดียวกัน เสียง s- ต้นคำตรงกัน"
            },
            {
                "word": "solar",
                "derivation_path": "PIE *sóh₂wl̥ → Latin solaris → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "solar cell (พลังงานสุริยะ/แสงอาทิตย์)"
            },
            {
                "word": "helium",
                "derivation_path": "Greek hēlios (ดวงอาทิตย์) + -ium → English helium",
                "origin_language": "Greek",
                "difficulty": "Academic / Science",
                "usage_note": "ก๊าซฮีเลียม ตั้งชื่อตามดวงอาทิตย์ เพราะถูกตรวจพบครั้งแรกในสเปกตรัมแสงสุริยะ!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*sóh₂wl̥", "meaning": "sun"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "sūrya (सूर्य)", "meaning": "sun"},
            {"era": "Modern Thai", "stage": "Thai", "form": "สุริยะ / สุริยคติ", "meaning": "ดวงอาทิตย์"},
            {"era": "Modern English", "stage": "English", "form": "sun, solar, helium", "meaning": "ดวงอาทิตย์, ระบบสุริยะ"}
        ]
    },
    {
        "thai_word": "ดารา",
        "category": "ธรรมชาติ สรรพสิ่ง และจักรวาล",
        "pali_sanskrit_form": "tārā (तारा) / stṛ (สันสกฤตพระเวท)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "star, pupil of the eye",
        "pie_root": "*h₂stḗr",
        "pie_meaning": "star",
        "sound_change_law": "Initial s-loss vs retention: ในภาษาสันสกฤตรุ่นหลังสระและพยัญชนะต้น s- หลุดหายกลายเป็น tārā ขณะที่ภาษากรีกและละตินรักษา st- ไว้ (astēr / stella) และเจอร์แมนิกกลายเป็น star",
        "semantic_drift_score": "Low (ดวงดาวบนฟ้า → บุคคลผู้โดดเด่น/ดารานักแสดง)",
        "semantic_drift_note": "ดารา (ดวงดาว, ดาราศาสตร์, ดารานักแสดง) ↔ star, stellar, astronomy, asteroid, disaster (ดวงดาวให้โทษ!)",
        "pie_branch_split": {
            "indo_iranian": "PIE *h₂stḗr → Vedic Sanskrit stṛ → Classical Sanskrit tārā → ภาษาไทย 'ดารา, ดาราศาสตร์'",
            "hellenic": "PIE *h₂stḗr → Greek astēr (ἀστήρ) → English astronomy, astronaut, asteroid, disaster",
            "italic": "PIE *h₂stḗr → Latin stella → English stellar, constellation (กลุ่มดาว)",
            "germanic": "PIE *h₂stḗr → Proto-Germanic *sternǭ → Old English steorra → English star"
        },
        "english_cognates": [
            {
                "word": "star",
                "derivation_path": "PIE *h₂stḗr → Proto-Germanic *sternǭ → Old English steorra",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ดารา ↔ star: สันสกฤต tārā ↔ star มาจากรากดวงดาว PIE เดียวกัน"
            },
            {
                "word": "astronomy",
                "derivation_path": "PIE *h₂stḗr → Greek astronomia (astēr + nomos กฎเกณฑ์) → English",
                "origin_language": "Greek",
                "difficulty": "Intermediate (B1)",
                "usage_note": "ดาราศาสตร์ (astronomy)"
            },
            {
                "word": "disaster",
                "derivation_path": "Latin dis- (วิบัติ/ไม่ดี) + Greek astēr (ดวงดาว) → Italian disastro → English disaster",
                "origin_language": "Latin / Italian",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ว้าว! disaster หายนะ เดิมมาจากความเชื่อโหราศาสตร์ 'ดวงดาวโคจรไม่ดี / ดาวพิบัติ'!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*h₂stḗr", "meaning": "star"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "tārā (तारा) / stṛ", "meaning": "star"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ดารา / ดาราศาสตร์", "meaning": "ดวงดาว, ดารานักแสดง"},
            {"era": "Modern English", "stage": "English", "form": "star, stellar, astronomy, disaster", "meaning": "ดวงดาว, หายนะ"}
        ]
    },
    {
        "thai_word": "วารี",
        "category": "ธรรมชาติ สรรพสิ่ง และจักรวาล",
        "pali_sanskrit_form": "vāri (वारि)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "water, rain, fluid",
        "pie_root": "*wódr̥ / *wōr-",
        "pie_meaning": "water, rain, wet",
        "sound_change_law": "Heteroclitic r/n alternation: รากคำว่าน้ำใน PIE มีทั้งสาย r-stem (*wōr-) และ n/d-stem (*wódr̥) สาย r- พัฒนาเป็นสันสกฤต vāri ส่วนสาย d- พัฒนาเป็น Germanic water และ Greek hydor",
        "semantic_drift_score": "None (สายน้ำ/น้ำ)",
        "semantic_drift_note": "วารี/วาริน ในภาษาไทยแปลว่าสายน้ำ ↔ water, wet, wash ในภาษาอังกฤษ",
        "pie_branch_split": {
            "indo_iranian": "PIE *wōr- / *wódr̥ → Sanskrit vāri → ภาษาไทย 'วารี, วาริน'",
            "hellenic": "PIE *wódr̥ → Greek hydōr (ὕδωρ) → English hydro-, hydrate, hydrant",
            "germanic": "PIE *wódr̥ → Proto-Germanic *watōr → Old English wæter → English water, wet"
        },
        "english_cognates": [
            {
                "word": "water",
                "derivation_path": "PIE *wódr̥ → Proto-Germanic *watōr → Old English wæter",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "วารี ↔ water: รากน้ำโบราณแห่งทวีปยูเรเซีย"
            },
            {
                "word": "hydro-",
                "derivation_path": "PIE *wódr̥ → Greek hydōr → English prefix",
                "origin_language": "Greek",
                "difficulty": "Intermediate / STEM",
                "usage_note": "พลังงานน้ำ เช่น hydroelectric (พลังน้ำวารี)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*wōr- / *wódr̥", "meaning": "water"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "vāri (वारि)", "meaning": "water"},
            {"era": "Modern Thai", "stage": "Thai", "form": "วารี", "meaning": "น้ำ, สายน้ำ"},
            {"era": "Modern English", "stage": "English", "form": "water, hydro-", "meaning": "น้ำ"}
        ]
    },
    {
        "thai_word": "อัคนี",
        "category": "ธรรมชาติ สรรพสิ่ง และจักรวาล",
        "pali_sanskrit_form": "agni (अग्नि)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "fire, sacrificial fire, fire deity",
        "pie_root": "*h₁n̥gʷnís",
        "pie_meaning": "fire (เพลิงที่มีชีวิตและเคลื่อนไหวได้ ต่างจากเพลิงสงบนิ่ง *péh₂wr̥)",
        "sound_change_law": "Preservation of animate fire: ชาวอินโด-ยูโรเปียนโบราณมีคำเรียกไฟ 2 คำ: ไฟที่มีชีวิต/เคลื่อนไหวได้ (*h₁n̥gʷnís) กับไฟธาตุสถิต (*péh₂wr̥ → fire) สันสกฤตและละตินสืบทอดคำว่าไฟมีชีวิต (agni / ignis)!",
        "semantic_drift_score": "Low (ไฟเพลิง → การจุดระเบิด)",
        "semantic_drift_note": "อัคนี ในภาษาไทย (หินอัคนี, พระอัคนี) ↔ ignite (จุดไฟ), ignition (ระบบจุดระเบิดรถยนต์), igneous (หินอัคนี!)",
        "pie_branch_split": {
            "indo_iranian": "PIE *h₁n̥gʷnís → Sanskrit agni → ภาษาไทย 'อัคนี, อัคคี'",
            "italic": "PIE *h₁n̥gʷnís → Latin ignis → English ignite, ignition, igneous"
        },
        "english_cognates": [
            {
                "word": "ignite",
                "derivation_path": "PIE *h₁n̥gʷnís → Latin ignire (จุดไฟ) → English ignite",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "จุดไฟ / ทำให้ลุกไหม้ (ราก อัคนี/agni ↔ igni- ตรงตัว!)"
            },
            {
                "word": "ignition",
                "derivation_path": "PIE *h₁n̥gʷnís → Latin ignitio → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ระบบจุดระเบิดเครื่องยนต์ / สวิตช์กุญแจรถยนต์"
            },
            {
                "word": "igneous",
                "derivation_path": "PIE *h₁n̥gʷnís → Latin igneus (เกิดจากไฟ) → English igneous rock",
                "origin_language": "Latin",
                "difficulty": "Academic / Geology",
                "usage_note": "หินอัคนี (Igneous rock) ทั้งในตำราไทยและฝรั่งใช้ศัพท์จากรากเดียวกันเป๊ะ!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*h₁n̥gʷnís", "meaning": "animate fire"},
            {"era": "~1500 BCE", "stage": "Vedic Sanskrit", "form": "agni (अग्नि)", "meaning": "fire, divine fire"},
            {"era": "Modern Thai", "stage": "Thai", "form": "อัคนี / หินอัคนี", "meaning": "ไฟ, หินเกิดจากลาวา"},
            {"era": "Modern English", "stage": "English", "form": "ignite, ignition, igneous", "meaning": "จุดไฟ, หินอัคนี"}
        ]
    },

    # -------------------------------------------------------------
    # 6. หมวดชีวิต วิญญาณ และการดับสูญ (Life, Soul & Mortality)
    # -------------------------------------------------------------
    {
        "thai_word": "ชีวะ",
        "category": "ชีวิต วิญญาณ และการดับสูญ",
        "pali_sanskrit_form": "jīva (जीव)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "living, soul, life, vitality",
        "pie_root": "*gʷyéh₃- (หรือ *gʷīw-)",
        "pie_meaning": "to live, alive",
        "sound_change_law": "Grimm's Law & Labiovelar: PIE voiced labiovelar stop *gʷ- กลายเสียงเป็น *k- ในเจอร์แมนิก (*gʷīwaz → *kwikwaz → quick ในความหมายดั้งเดิมคือ 'มีชีวิต' เช่น the quick and the dead) และเปลี่ยนเป็น j- ในสันสกฤต (jīva) และ v- ในละติน (vīvere → vivid, vital)",
        "semantic_drift_score": "None (ชีวิต/สิ่งมีชีวิต)",
        "semantic_drift_note": "ชีวะ/ชีพ (ชีววิทยา, สิ่งมีชีวิต, ชีพจร) ↔ vivid, vital, revive, survive, quick",
        "pie_branch_split": {
            "indo_iranian": "PIE *gʷyéh₃- → Sanskrit jīva → ภาษาไทย 'ชีวะ, ชีวี, ชีพ, ชีพจร'",
            "hellenic": "PIE *gʷyéh₃- → Greek bios (βίος) → English biology, biography, antibiotic",
            "italic": "PIE *gʷyéh₃- → Latin vīvere / vīta → English vivid, vital, revive, survive, victim",
            "germanic": "PIE *gʷyéh₃- → Proto-Germanic *kwikwaz (Grimm's Law *gʷ→*k) → Old English cwic → English quick (มีชีวิต)"
        },
        "english_cognates": [
            {
                "word": "vivid",
                "derivation_path": "PIE *gʷīw- → Latin vividus (เต็มไปด้วยชีวิตชีวา) → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "มีชีวิตชีวา / สีสดใสแจ่มชัด (ราก ชีวะ ↔ viv-)"
            },
            {
                "word": "vital",
                "derivation_path": "PIE *gʷīw- → Latin vitalis (จำเป็นต่อชีวิต) → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "สำคัญยิ่งยวดต่อชีวิต (vital signs = สัญญาณชีพ)"
            },
            {
                "word": "survive",
                "derivation_path": "PIE *gʷīw- → Latin super- (เหนือ) + vivere (มีชีวิต) → English survive",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "รอดชีวิต (มีชีวิตอยู่ต่อ)"
            },
            {
                "word": "quick",
                "derivation_path": "PIE *gʷīw- → Proto-Germanic *kwikwaz (Grimm's Law) → Old English cwic",
                "origin_language": "Old English",
                "difficulty": "General (A2)",
                "usage_note": "เดิมแปลว่า 'มีชีวิต' (เช่น cut to the quick = กรีดลึกถึงเนื้อเป็น/มีชีวิต)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*gʷyéh₃- / *gʷīw-", "meaning": "to live"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "jīva (जीव)", "meaning": "living being, soul"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ชีวะ / ชีพ", "meaning": "ชีวิต, การมีชีวิต"},
            {"era": "Modern English", "stage": "English", "form": "vivid, vital, survive, quick", "meaning": "มีชีวิต, สำคัญยิ่ง"}
        ]
    },
    {
        "thai_word": "มรณะ",
        "category": "ชีวิต วิญญาณ และการดับสูญ",
        "pali_sanskrit_form": "maraṇa (मरण) / mṛta",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "death, dying, mortal",
        "pie_root": "*mer-",
        "pie_meaning": "to die, perish",
        "sound_change_law": "Nasal and liquid preservation: ราก *m-r- รักษาโครงสร้างในทุกสาขา ทั้งสันสกฤต maraṇa/mṛtyu, ละติน mors/mortis, กรีก brotos และเจอร์แมนิก murder/mortal",
        "semantic_drift_score": "None (ความตาย/มรรตัย)",
        "semantic_drift_note": "มรณะ/มรณกรรม/อมตะ (a-mṛta ไม่ตาย) ↔ mortal, murder, mortuary, amortize, immortal",
        "pie_branch_split": {
            "indo_iranian": "PIE *mer- → Sanskrit maraṇa / mṛta → Pali maraṇa → ภาษาไทย 'มรณะ, มรณา, มรรตัย, อมตะ'",
            "hellenic": "PIE *mer- → Greek ambrotos (ไม่ตาย/อมฤต) → English ambrosia (อาหารทิพย์อมฤต!)",
            "italic": "PIE *mer- → Latin mors / mortis → English mortal, immortal, mortuary, amortize",
            "germanic": "PIE *mer- → Proto-Germanic *murþrą → Old English morðor → English murder, nightmare"
        },
        "english_cognates": [
            {
                "word": "mortal",
                "derivation_path": "PIE *mer- → Latin mortalis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ต้องตาย / ปุถุชน (ตรงกับคำว่า 'มรรตัย' ในภาษาไทย!)"
            },
            {
                "word": "immortal",
                "derivation_path": "Latin in- (ไม่) + mortalis (ตาย) → English immortal",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "อมตะ (a- = ไม่ + mṛta = ตาย) ↔ immortal (in- + mortal) โครงสร้างคำประกบกันเหมือนกันเป๊ะ!"
            },
            {
                "word": "murder",
                "derivation_path": "PIE *mer- → Proto-Germanic *murþrą → Old English morðor",
                "origin_language": "Old English",
                "difficulty": "General (A2)",
                "usage_note": "ฆาตกรรม (ทำให้ถึงแก่มรณะ)"
            },
            {
                "word": "mortgage",
                "derivation_path": "Latin mort- (ตาย/มรณะ) + Old French gage (สัญญาค้ำประกัน) = สัญญาตายตัว!",
                "origin_language": "Old French",
                "difficulty": "Intermediate (B2)",
                "usage_note": "การจำนองบ้าน/ที่ดิน (เดิมแปลว่า 'ข้อตกลงที่ดับสิ้นเมื่อจ่ายหนี้หมด')"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*mer-", "meaning": "to die"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "maraṇa (मरण) / mṛta", "meaning": "death, dead"},
            {"era": "Modern Thai", "stage": "Thai", "form": "มรณะ / อมตะ", "meaning": "ความตาย, ความไม่ตาย"},
            {"era": "Modern English", "stage": "English", "form": "mortal, immortal, murder, mortgage", "meaning": "ตาย, ฆาตกรรม, การจำนอง"}
        ]
    },

    # -------------------------------------------------------------
    # 7. หมวดอำนาจ รัฐ และสถานะสังคม (Power, State & Society)
    # -------------------------------------------------------------
    {
        "thai_word": "ราชา",
        "category": "อำนาจ รัฐ และสถานะสังคม",
        "pali_sanskrit_form": "rājan (राजन्) / rājā",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "king, ruler, sovereign",
        "pie_root": "*h₃rḗǵ-",
        "pie_meaning": "to straighten, direct, lead, rule; ruler",
        "sound_change_law": "Grimm's Law: PIE voiced stop *ǵ- กลายเสียงเป็น voiceless *k- ในเจอร์แมนิก (*h₃rḗǵ- → *rīks / *rehtaz → right, rich) และกลายเป็น rex/reg- ในละติน (regal, royal, reign)",
        "semantic_drift_score": "Low (การชี้ถูกตรง → การปกครอง → กษัตริย์)",
        "semantic_drift_note": "ราชา/ราช/ราโชวาท ↔ royal, regal, reign, regime, direct, correct, right, rich!",
        "pie_branch_split": {
            "indo_iranian": "PIE *h₃rḗǵ- → Sanskrit rājan → Pali rājā → ภาษาไทย 'ราชา, ราช, ราโชวาท'",
            "celtic": "PIE *h₃rḗǵ- → Proto-Celtic *rīxs → Gaulish -rix (เช่น Vercingetorix กษัตริย์กอลล์)",
            "italic": "PIE *h₃rḗǵ- → Latin rēx (กษัตริย์) / regere (ชี้นำ/ปกครอง) → English regal, royal, reign, regime, direct, correct",
            "germanic": "PIE *h₃rḗǵ- → Proto-Germanic *rīkijaz (ผู้มีอำนาจ) → Old English rīċe → English rich, right (ถูกต้อง/ทิศขวา)"
        },
        "english_cognates": [
            {
                "word": "royal",
                "derivation_path": "PIE *h₃rḗǵ- → Latin regalis → Old French roial → English royal",
                "origin_language": "Old French / Latin",
                "difficulty": "General (A2)",
                "usage_note": "เกี่ยวกับกษัตริย์/ราชวงศ์ (ราช ↔ roy-)"
            },
            {
                "word": "regal",
                "derivation_path": "PIE *h₃rḗǵ- → Latin regalis → English regal",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "สง่างามสมฐานะราชา (ราชา ↔ regal ตรงตัว!)"
            },
            {
                "word": "reign",
                "derivation_path": "PIE *h₃rḗǵ- → Latin regnare → English reign",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "รัชสมัยการครองราชย์"
            },
            {
                "word": "right",
                "derivation_path": "PIE *h₃rḗǵ- → Proto-Germanic *rehtaz → Old English riht",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ถูกต้อง / สิทธิชอบธรรม (มาจากรากเดียวกัน: สิ่งที่ผู้ปกครองชี้ว่าตรง/ถูก)"
            },
            {
                "word": "rich",
                "derivation_path": "PIE *h₃rḗǵ- → Proto-Germanic *rīkijaz (มีอำนาจปกครอง) → Old English rīċe → English rich",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "ร่ำรวย (เดิมแปลว่า 'มีอิทธิพล/ทรัพย์สมบัติเยี่ยงราชา')"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*h₃rḗǵ-", "meaning": "to rule, straighten, ruler"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "rājan (राजन्)", "meaning": "king, sovereign"},
            {"era": "Modern Thai", "stage": "Thai", "form": "ราชา / ราชวงศ์", "meaning": "กษัตริย์, แว่นแคว้น"},
            {"era": "Modern English", "stage": "English", "form": "royal, regal, reign, right, rich", "meaning": "กษัตริย์, ถูกต้อง, มั่งคั่ง"}
        ]
    },
    {
        "thai_word": "มนุษย์",
        "category": "อำนาจ รัฐ และสถานะสังคม",
        "pali_sanskrit_form": "manuṣya (मनुष्य) / manussa (บาลี)",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "human, mortal man, descended from Manu",
        "pie_root": "*mon- / *men-",
        "pie_meaning": "thinker, the thinking being, human",
        "sound_change_law": "Nasal preservation: PIE *mon- / *manu- ให้กำเนิดสันสกฤต manuṣya, โอลด์อิงลิช mann และเยอรมัน Mann โดยมองว่ามนุษย์คือ 'ผู้ที่มีความคิดใคร่ครวญ'",
        "semantic_drift_score": "None (มนุษย์/ผู้คิดได้)",
        "semantic_drift_note": "มนุษย์/มานพ (ผู้สืบเชื้อสายจากพระมนู) ↔ man, human, mankind",
        "pie_branch_split": {
            "indo_iranian": "PIE *mon- → Sanskrit manuṣya → Pali manussa → ภาษาไทย 'มนุษย์, มานพ'",
            "germanic": "PIE *mon- → Proto-Germanic *mann- → Old English mann → English man, mankind, human"
        },
        "english_cognates": [
            {
                "word": "man",
                "derivation_path": "PIE *mon- → Proto-Germanic *mann- → Old English mann",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "มนุษย์ ↔ man: รากโบราณเดียวกันแปลว่า 'สิ่งมีชีวิตผู้มีความคิด' (จากราก มโน/men-)"
            },
            {
                "word": "mankind",
                "derivation_path": "PIE *mon- + *ǵenh₁- (ชน/กำเนิด) → Old English manncynn",
                "origin_language": "Old English",
                "difficulty": "Intermediate (B1)",
                "usage_note": "มนุษยชาติ (man + kind)"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*mon-", "meaning": "thinking creature, human"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "manuṣya (मनुष्य)", "meaning": "human being"},
            {"era": "Modern Thai", "stage": "Thai", "form": "มนุษย์ / มานพ", "meaning": "คน, เผ่าพันธุ์มนุษย์"},
            {"era": "Modern English", "stage": "English", "form": "man, mankind", "meaning": "มนุษย์, มนุษยชาติ"}
        ]
    },

    # -------------------------------------------------------------
    # 8. หมวดการกระทำ การสรรสร้าง และคุณลักษณะ (Action & Attributes)
    # -------------------------------------------------------------
    {
        "thai_word": "นวัตกรรม",
        "category": "การกระทำ การสรรสร้าง และคุณลักษณะ",
        "pali_sanskrit_form": "nava (नव) + karma (कर्म)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "new + deed/creation",
        "pie_root": "*néwos",
        "pie_meaning": "new, recent",
        "sound_change_law": "Liquid and vowel consistency: ราก *néwos พัฒนาเป็นสันสกฤต nava, ละติน novus, กรีก neos และเจอร์แมนิก new",
        "semantic_drift_score": "Low (ใหม่ + การกระทำ = สิ่งประดิษฐ์สร้างสรรค์ใหม่)",
        "semantic_drift_note": "นว- (นวัตกรรม, นวนิยาย, พระนวมินทร์) ↔ new, novel, innovate, novice, neon",
        "pie_branch_split": {
            "indo_iranian": "PIE *néwos → Sanskrit nava → ภาษาไทย 'นว-, นวัตกรรม, นวนิยาย'",
            "hellenic": "PIE *néwos → Greek neos (νέος) → English neon, neologism, neonatal",
            "italic": "PIE *néwos → Latin novus → English novel, innovate, renovate, novice",
            "germanic": "PIE *néwos → Proto-Germanic *niwjaz → Old English nīwe → English new"
        },
        "english_cognates": [
            {
                "word": "new",
                "derivation_path": "PIE *néwos → Proto-Germanic *niwjaz → Old English nīwe",
                "origin_language": "Old English",
                "difficulty": "General (A1)",
                "usage_note": "นว- ↔ new: รากเดียวกันเป๊ะ (เช่น นวกรรม = new work)"
            },
            {
                "word": "innovate",
                "derivation_path": "PIE *néwos → Latin innovare (in- + novus ทำสิ่งใหม่) → English innovate",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "นวัตกรรม คือคำแปลบัญญัติของคำว่า innovation (ทั้งสองคำมีราก นว- ↔ nov- เดียวกัน!)"
            },
            {
                "word": "novel",
                "derivation_path": "PIE *néwos → Latin novellus → Italian novella → English novel",
                "origin_language": "Italian / Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "แปลกใหม่ / นวนิยาย (เรื่องเล่าแต่งใหม่)"
            },
            {
                "word": "novice",
                "derivation_path": "PIE *néwos → Latin novicius → English novice",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "ผู้เริ่มต้นใหม่ / มือใหม่"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*néwos", "meaning": "new, recent"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "nava (नव)", "meaning": "new, fresh"},
            {"era": "Modern Thai", "stage": "Thai", "form": "นว- / นวัตกรรม", "meaning": "ใหม่, การกระทำใหม่"},
            {"era": "Modern English", "stage": "English", "form": "new, innovate, novel, novice", "meaning": "ใหม่, สร้างสรรค์ใหม่"}
        ]
    },
    {
        "thai_word": "สุนัข",
        "category": "การกระทำ การสรรสร้าง และคุณลักษณะ",
        "pali_sanskrit_form": "śunaka (शुनक) / śvan (श्वन्)",
        "pali_sanskrit_lang": "Sanskrit",
        "pali_sanskrit_meaning": "dog, hound",
        "pie_root": "*ḱwṓn (สัมพันธการก *kunós)",
        "pie_meaning": "dog, hound",
        "sound_change_law": "Grimm's Law & Satemization: PIE voiceless palatovelar *ḱ- กลายเสียงเป็น *h- ในเจอร์แมนิก (*ḱwṓn → *hundaz → hound) และกลายเป็น ś- ในสันสกฤต (śvan / śunaka) ขณะที่ Latin กลายเป็น canis และ Greek กลายเป็น kyōn",
        "semantic_drift_score": "None (สุนัข/หมา) + ปรัชญา Cynic",
        "semantic_drift_note": "สุนัข ในภาษาไทย ↔ hound, canine, และคำทางปรัชญาอย่าง cynical (มองโลกในแง่ร้าย/เหมือนสุนัข!)",
        "pie_branch_split": {
            "indo_iranian": "PIE *ḱwṓn → Sanskrit śvan / śunaka → Pali sunakha → ภาษาไทย 'สุนัข'",
            "hellenic": "PIE *ḱwṓn → Greek kyōn (κύων) / kynikos → English cynic, cynical (อยู่ง่ายเยี่ยงสุนัข)",
            "italic": "PIE *ḱwṓn → Latin canis → English canine (ฟันเขี้ยว/เกี่ยวกับสุนัข)",
            "germanic": "PIE *ḱwṓn → Proto-Germanic *hundaz (Grimm's Law *ḱ→*h) → Old English hund → English hound"
        },
        "english_cognates": [
            {
                "word": "hound",
                "derivation_path": "PIE *ḱwṓn → Proto-Germanic *hundaz → Old English hund",
                "origin_language": "Old English",
                "difficulty": "Intermediate (B1)",
                "usage_note": "สุนัขล่าเนื้อ (เสียง ś- ใน สุนัข กลายเป็น h- ใน hound ตามกฎกริมม์)"
            },
            {
                "word": "canine",
                "derivation_path": "PIE *ḱwṓn → Latin caninus → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "เกี่ยวกับสุนัข / ฟันเขี้ยวสุนัข"
            },
            {
                "word": "cynic",
                "derivation_path": "PIE *ḱwṓn → Greek kynikos (เหมือนสุนัข) → English cynic",
                "origin_language": "Greek",
                "difficulty": "Advanced (C1)",
                "usage_note": "ว้าว! สำนักปรัชญาไซนิก (Cynic) ของไดโอจีนีส ที่อยู่ง่ายกินง่ายในถังไม้ริมถนน ถูกเรียกว่า 'พวกใช้ชีวิตเยี่ยงสุนัข'!"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*ḱwṓn", "meaning": "dog, hound"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "śunaka (शुनक)", "meaning": "little dog, pup"},
            {"era": "Modern Thai", "stage": "Thai", "form": "สุนัข", "meaning": "หมา (ภาษาทางการ)"},
            {"era": "Modern English", "stage": "English", "form": "hound, canine, cynic", "meaning": "สุนัข, ฟันเขี้ยว"}
        ]
    },
    {
        "thai_word": "วาจา",
        "category": "การกระทำ การสรรสร้าง และคุณลักษณะ",
        "pali_sanskrit_form": "vāc (वाच्) / vācā",
        "pali_sanskrit_lang": "Sanskrit / Pali",
        "pali_sanskrit_meaning": "voice, speech, word",
        "pie_root": "*wókʷs",
        "pie_meaning": "voice, to speak",
        "sound_change_law": "Labiovelar delabialization: PIE *wókʷs กลายเป็นสันสกฤต vāc และละติน vōx / vocis",
        "semantic_drift_score": "None (คำพูด/เสียงพูด)",
        "semantic_drift_note": "วาจา/พจน์/โวหาร ↔ voice, vocal, vocation, advocate, vowel, invoke, provoke",
        "pie_branch_split": {
            "indo_iranian": "PIE *wókʷs → Sanskrit vāc / vākya → ภาษาไทย 'วาจา, วากยสัมพันธ์, โวหาร'",
            "hellenic": "PIE *wókʷs → Greek epos (คำพูด/มหากาพย์) → English epic",
            "italic": "PIE *wókʷs → Latin vōx / vocare → English voice, vocal, vocation, advocate, provoke, vowel"
        },
        "english_cognates": [
            {
                "word": "voice",
                "derivation_path": "PIE *wókʷs → Latin vōx → Old French vois → English voice",
                "origin_language": "Old French / Latin",
                "difficulty": "General (A1)",
                "usage_note": "วาจา ↔ voice: เสียง v- ต้นคำตรงกันเป๊ะ"
            },
            {
                "word": "vocal",
                "derivation_path": "PIE *wókʷs → Latin vocalis → English",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B1)",
                "usage_note": "เกี่ยวกับเสียงร้อง / วาจา เช่น vocal cords = เส้นเสียง"
            },
            {
                "word": "advocate",
                "derivation_path": "Latin ad- (เพื่อ) + vocare (เปล่งเสียงพูด) → English advocate",
                "origin_language": "Latin",
                "difficulty": "Advanced (B2/C1)",
                "usage_note": "ทนายความ / ผู้พูดสนับสนุนแทนผู้อื่น"
            },
            {
                "word": "vocation",
                "derivation_path": "PIE *wókʷs → Latin vocatio (เสียงเพรียกเรียกในใจ) → English vocation",
                "origin_language": "Latin",
                "difficulty": "Intermediate (B2)",
                "usage_note": "อาชีพที่ทำด้วยใจรัก (ดั้งเดิมแปลว่า 'เสียงเรียกของพระเจ้า')"
            }
        ],
        "timeline": [
            {"era": "~4500 BCE", "stage": "PIE", "form": "*wókʷs", "meaning": "voice, speech"},
            {"era": "~1500 BCE", "stage": "Sanskrit", "form": "vāc (वाच्)", "meaning": "speech, voice"},
            {"era": "Modern Thai", "stage": "Thai", "form": "วาจา", "meaning": "คำพูด, ถ้อยคำ"},
            {"era": "Modern English", "stage": "English", "form": "voice, vocal, advocate", "meaning": "เสียง, การพูด"}
        ]
    }
]


def enrich_with_orst_cache(seeds, cache_path):
    print(f"Loading ORST cache from {cache_path}...")
    if not os.path.exists(cache_path):
        print("Warning: ORST cache not found. Proceeding without enrichment.")
        return seeds

    with open(cache_path, "r", encoding="utf-8") as f:
        orst_cache = json.load(f)

    enriched_count = 0
    for entry in seeds:
        word = entry["thai_word"]
        if word in orst_cache:
            orst = orst_cache[word]
            entry["orst_definition"] = orst.get("thai_definition", "")
            entry["orst_read"] = orst.get("thai_read", "")
            entry["orst_pos"] = orst.get("thai_pos", "")
            entry["orst_edition"] = orst.get("orst_edition", "")
            entry["orst_sources"] = orst.get("sources", [])
            entry["specialized_terms"] = orst.get("specialized_terms", [])
            enriched_count += 1
        else:
            # Try finding without trailing markers
            base = word.strip()
            if base in orst_cache:
                orst = orst_cache[base]
                entry["orst_definition"] = orst.get("thai_definition", "")
                entry["orst_read"] = orst.get("thai_read", "")
                entry["orst_pos"] = orst.get("thai_pos", "")
                entry["orst_edition"] = orst.get("orst_edition", "")
                entry["orst_sources"] = orst.get("sources", [])
                entry["specialized_terms"] = orst.get("specialized_terms", [])
                enriched_count += 1

    print(f"Enriched {enriched_count} / {len(seeds)} seed entries with official ORST data!")
    return seeds


def main():
    cache_path = os.path.join(os.path.dirname(__file__), "..", "data", "orst_official_cache.json")
    enriched_seeds = enrich_with_orst_cache(SEED_DATA, cache_path)
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "data", "etymology_seeds.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "version": "1.0",
            "title": "Etymological Bridge Knowledge Graph - Thai Sanskrit/Pali to English PIE Cognates",
            "curator": "Nextect Dictionary Reimagined Team",
            "entries_count": len(enriched_seeds),
            "entries": enriched_seeds
        }, f, ensure_ascii=False, indent=2)

    print(f"Saved complete knowledge graph to {out_path}")


if __name__ == "__main__":
    main()
