# สะพานรากศัพท์ (Etymological Bridge) 🌉
### โครงการสำหรับการแข่งขัน "เปิดคลังคำ พลิกคลังคิด" (Dictionary Reimagined Hackathon)
**จัดโดย: สำนักงานราชบัณฑิตยสภา (Office of the Royal Society of Thailand - ORST)**

---

## 📖 ภาพรวมโครงการ (Project Overview)
**"สะพานรากศัพท์ (Etymological Bridge)"** คือระบบเปลี่ยนบทบาทพจนานุกรมไทยจากการเป็นเพียง *คลังคำศัพท์ (Word Repository)* ที่เปิดหาความหมาย สู่การเป็น **คลังข้อมูลและปัญญา (Knowledge & Etymological Graph)**

โดยใช้นวัตกรรมทางภาษาศาสตร์เชื่อมโยง **คำยืมบาลี-สันสกฤตในภาษาไทย** เข้ากับ **คำร่วมเชื้อสาย (Cognates) ในภาษาอังกฤษ** ผ่านรากภาษาบรรพบุรุษร่วม **Proto-Indo-European (PIE)** ทำให้คนไทยสามารถเรียนรู้และจดจำคำศัพท์ภาษาอังกฤษระดับสูง (GRE, SAT, Academic English) ได้ง่าย แม่นยำ และเห็นความเชื่อมโยงของภาษาทั่วโลก

---

## 🌟 จุดเด่นของผลงาน (Key Innovations)
1. **พจนานุกรมเป็นมากกว่าพจนานุกรม:** สัมผัสเครือข่ายวิวัฒนาการคำศัพท์ข้ามทวีปกว่า 6,000 ปี
2. **นวัตกรรมการเรียนรู้คำศัพท์ (Cognate Mnemonic):** จำศัพท์ภาษาอังกฤษระดับสูงได้ทันทีจากคำไทยที่คุ้นเคย
   - *มารดา* ↔ *maternal, matriarch, matrix* (ราก PIE: `*méh₂tēr`)
   - *ศูนย์* ↔ *zero, cave, cavity* (ราก PIE: `*ḱewH-`)
   - *ทันต* ↔ *dental, dentist, dandelion* (ราก PIE: `*h₁dónts`)
   - *วิทยา* ↔ *video, vision, wise, idea* (ราก PIE: `*weyd-`)
3. **ความถูกต้องทางภาษาศาสตร์ 100%:** อิงหลัก Historical Linguistics & Grimm's Law ผสานคลังข้อมูลมาตรฐานราชบัณฑิตยสถาน
4. **Interactive Force-Directed Graph:** แผนภาพโครงสร้างสายสัมพันธ์ภาษาศาสตร์แบบไดนามิกด้วย D3.js v7
5. **สารบัญข้อมูลทางการสมบูรณ์แบบ:** รวบรวมและวิเคราะห์ชุดข้อมูลราชบัณฑิตยสภาทั้งหมดไว้ใน [`DATA_SOURCE_CATALOG.md`](DATA_SOURCE_CATALOG.md)

---

## 📂 โครงสร้างไดเรกทอรี (Repository Structure)

```
ThaiDict_Script/
├── DATA_SOURCE_CATALOG.md         ← คู่มือวิเคราะห์สารบัญข้อมูลทางการราชบัณฑิตยสภา 100%
├── requirements.txt               ← รายการไลบรารี Python ที่ต้องใช้งาน
├── etymological-bridge/           ← โค้ดระบบหลัก (Full-Stack Web Application)
│   ├── backend/
│   │   ├── app.py                 ← FastAPI Server & Static Host (Port 8088)
│   │   ├── engine.py              ← Etymology Knowledge Engine & Graph Traversal
│   │   ├── classifier.py          ← ตัวแยกแยะคำยืมบาลี-สันสกฤต vs คำไทยแท้ (Kra-Dai)
│   │   └── ingest_orst.py         ← Data Pipeline สกัดคำจาก DICT_2542/DICT_2554
│   ├── data/
│   │   ├── seed_corpus.py         ← ฐานข้อมูลรากศัพท์ 43 คำหลัก 146 Cognates อังกฤษ
│   │   ├── build_seeds.py         ← Script สร้าง JSON Knowledge Graph
│   │   ├── etymology_seeds.json   ← Knowledge Graph Dataset พร้อมใช้งาน
│   │   └── orst_official_cache.json ← ดัชนีคำทางการ 39,189 คำ
│   └── frontend/
│       ├── index.html             ← หน้าเว็บอินเทอร์แอคทีฟ (Glassmorphic UI)
│       ├── css/
│       │   └── style.css          ← Cosmic Dark Theme & Responsive Styles
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
- **Data Standards:** Office of the Royal Society of Thailand (ORST) Dictionaries (2542, 2554 B.E.)
