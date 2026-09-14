# สะพานรากศัพท์ (Etymological Bridge) 🌉
### ระบบเชื่อมโยงคำยืมบาลี-สันสกฤตในภาษาไทย ↔ Cognates ภาษาอังกฤษ ผ่าน Proto-Indo-European (PIE)

---

## 📖 ภาพรวมของระบบ (Overview)
**"สะพานรากศัพท์ (Etymological Bridge)"** คือระบบวิเคราะห์และสืบค้นความสัมพันธ์ทางภาษาศาสตร์เชิงประวัติศาสตร์ (Historical Comparative Linguistics) ที่เชื่อมโยง **คำยืมบาลี-สันสกฤตในภาษาไทย** เข้ากับ **คำร่วมเชื้อสาย (Cognates) ในภาษาอังกฤษ** ผ่านรากภาษาบรรพบุรุษร่วม **Proto-Indo-European (PIE)**

ช่วยให้ผู้เรียนและนักวิจัยสามารถเข้าใจความสัมพันธ์ของคำศัพท์ในภาษาไทยกับภาษาตระกูลอินโด-ยูโรเปียน พร้อมทั้งช่วยในการจดจำคำศัพท์ภาษาอังกฤษระดับสูง (GRE, SAT, Academic English) ผ่านคำไทยที่คุ้นเคยในชีวิตประจำวัน

---

## 🌟 จุดเด่นของระบบ (Key Features)
1. **Etymological Chain:** วิเคราะห์สายวิวัฒนาการคำศัพท์ 4 ระดับ (Thai ↔ Sanskrit/Pali ↔ PIE ↔ English)
2. **Cognate Mnemonic:** จดจำคำศัพท์ภาษาอังกฤษระดับสูงได้ทันทีจากคำไทยที่คุ้นเคย:
   - *มารดา* ↔ *maternal, matriarch, matrix* (ราก PIE: `*méh₂tēr`)
   - *ศูนย์* ↔ *zero, cave, cavity* (ราก PIE: `*ḱewH-`)
   - *ทันต* ↔ *dental, dentist, dandelion* (ราก PIE: `*h₁dónts`)
   - *วิทยา* ↔ *video, vision, wise, idea* (ราก PIE: `*weyd-`)
3. **Phonological Law & Semantic Drift:** อธิบายกฎการเปลี่ยนแปลงทางเสียง (เช่น Grimm's Law) และคะแนนการเบี่ยงเบนทางความหมาย
4. **Interactive Force-Directed Graph:** แสดงเครือข่ายความสัมพันธ์ทางภาษาศาสตร์แบบโต้ตอบด้วย D3.js v7
5. **Interactive Learning Quiz:** ระบบแบบทดสอบคำศัพท์เชิงนิรุกติศาสตร์เพื่อส่งเสริมการเรียนรู้

---

## 📂 โครงสร้างไดเรกทอรี (Repository Structure)

```
ThaiDict_Script/
├── requirements.txt               ← รายการไลบรารี Python ที่ต้องใช้งาน
├── etymological-bridge/           ← โค้ดระบบ Prototype หลัก (Full-Stack Web Application)
│   ├── backend/
│   │   ├── app.py                 ← FastAPI REST API Server & Static Host (Port 8088)
│   │   ├── engine.py              ← Etymology Knowledge Engine & Graph Traversal
│   │   ├── classifier.py          ← ตัวแยกแยะคำยืมบาลี-สันสกฤต vs คำไทยแท้ (Kra-Dai)
│   │   └── ingest_orst.py         ← Data Pipeline สกัดคำจาก DICT_2542/DICT_2554
│   ├── data/
│   │   ├── seed_corpus.py         ← ฐานข้อมูลรากศัพท์ 43 คำหลัก 146 Cognates อังกฤษ
│   │   ├── build_seeds.py         ← Script สร้าง JSON Knowledge Graph
│   │   ├── etymology_seeds.json   ← Knowledge Graph Dataset พร้อมใช้งาน
│   │   └── orst_official_cache.json ← ดัชนีคำทางการ 39,189 คำ
│   └── frontend/
│       ├── index.html             ← หน้าเว็บอินเทอร์แอคทีฟ (Glassmorphic Dark Theme)
│       ├── css/
│       │   └── style.css          ← สไตล์ Cosmic Glassmorphism & Responsive Design
│       └── js/
│           ├── app.js             ← Master UI Controller & State Manager
│           ├── d3_graph.js        ← D3.js Force-Directed Interactive Graph
│           └── quiz.js            ← ระบบ Mnemonic Educational Quiz
```

---

## 🚀 วิธีการติดตั้งและรันระบบ (Quickstart)

### 1. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 2. รันเซิร์ฟเวอร์
```bash
cd etymological-bridge/backend
python app.py
```

### 3. เข้าใช้งานระบบ
เปิดเว็บเบราว์เซอร์ที่: **`http://127.0.0.1:8088/`**

---

## 🛠️ Tech Stack
- **Backend:** Python 3.9+, FastAPI, Uvicorn
- **Data & Linguistic Engine:** Python Custom Graph Traverser, Regex Classifier
- **Frontend:** Vanilla HTML5, Modern CSS (Glassmorphism & Responsive Design), Vanilla JavaScript (ES6+)
- **Data Visualization:** D3.js v7 (Force-Directed Simulation Graph)
- **Data Standards:** พจนานุกรม ฉบับราชบัณฑิตยสถาน (พ.ศ. ๒๕๔๒ / ๒๕๕๔)
