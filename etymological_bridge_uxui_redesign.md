# UX/UI Redesign Brief — “สะพานรากศัพท์ (Etymological Bridge)”
## สำหรับใช้เป็น Prompt / Design Specification ให้ AI Agent สร้างเว็บไซต์ใหม่

> **เป้าหมายหลัก:** Redesign เว็บไซต์ “สะพานรากศัพท์” ของราชบัณฑิตยสถาน ให้ดูเป็นเว็บไซต์ความรู้/พจนานุกรมที่น่าเชื่อถือ เข้าถึงง่าย และมีความเป็นธรรมชาติ มากกว่าหน้าเว็บที่ถูกสร้างด้วย AI โดยตรง  
>
> **หลักคิดสำคัญ:** “Modern แต่ไม่ futuristic, เป็นวิชาการแต่ไม่แข็ง, สวยแต่ไม่ตกแต่งเกินจำเป็น, ใช้ง่ายก่อนโชว์เทคโนโลยี”

---

# 1. CONTEXT

เว็บไซต์นี้เป็นระบบค้นคว้าความสัมพันธ์ทางภาษาศาสตร์เชิงประวัติศาสตร์ โดยเชื่อมโยงคำภาษาไทยกับภาษาบาลี–สันสกฤต และสายภาษา Proto-Indo-European (PIE) รวมถึง English Cognates

ตัวอย่างการค้นหา:

- `บิดา`
- `มารดา`
- `ทันต`
- `วิทยา`
- `ราช`
- `มนุษย์`

ระบบสามารถแสดง:

1. ความหมายของคำ
2. รากศัพท์
3. คำในบาลี/สันสกฤต
4. Proto-Indo-European root
5. English cognates
6. การเปลี่ยนเสียง
7. การเปลี่ยนความหมาย
8. ลำดับเวลา
9. Interactive etymological tree
10. คำศัพท์ที่เกี่ยวข้อง

เว็บไซต์เดิมมีข้อมูลค่อนข้างน่าสนใจ แต่ UI ปัจจุบันมีลักษณะ “AI-generated dashboard” มากเกินไป เช่น:

- dark background หนักมาก
- ใช้สี neon หลายสีพร้อมกัน
- card จำนวนมาก
- gradient / glow เยอะ
- border สีสดจำนวนมาก
- emoji ถูกใช้เป็น icon หลัก
- typography หนาและแน่น
- ข้อมูลสำคัญถูกกลบด้วย decoration
- หน้าตาเหมือน developer demo มากกว่าเว็บไซต์ความรู้ของสถาบันทางภาษา
- ผู้ใช้ใหม่ไม่รู้ว่าควรเริ่มจากตรงไหน
- interactive graph มีความน่าสนใจ แต่มี cognitive load สูง

**Redesign ต้องแก้ปัญหาเหล่านี้โดยไม่ทิ้ง functionality เดิม**

---

# 2. DESIGN DIRECTION

## Visual Personality

ให้เว็บไซต์รู้สึกเหมือน:

> “ห้องสมุดดิจิทัลร่วมสมัยของสถาบันภาษา”

ไม่ใช่:

> “AI dashboard / Cyberpunk knowledge graph”

### Keywords

- Trustworthy
- Academic
- Human
- Calm
- Warm
- Accessible
- Editorial
- Thai cultural identity
- Contemporary
- Minimal
- Educational

### ห้ามให้รู้สึกเหมือน

- AI SaaS dashboard
- Crypto dashboard
- Developer tool
- Cyberpunk interface
- Gaming UI
- Neon futuristic website
- Generic ChatGPT clone

---

# 3. CORE UX PRINCIPLE

## Principle 01 — Search First

ผู้ใช้ส่วนใหญ่ไม่จำเป็นต้องเข้าใจ PIE ก่อน

ดังนั้นเว็บไซต์ควรเริ่มจากคำถามง่าย ๆ:

> “อยากรู้ที่มาของคำว่าอะไร?”

แล้วให้ผู้ใช้ค้นหา

ตัวอย่าง:

```text
ค้นหาคำศัพท์ เช่น “บิดา” “มารดา” “วิทยา”
                         [ ค้นหา ]
```

ไม่ควรเริ่มด้วย graph หรือข้อมูลเชิงเทคนิค

---

## Principle 02 — Progressive Disclosure

อย่าแสดงข้อมูลทุกอย่างพร้อมกัน

แบ่งข้อมูลเป็นระดับ:

### Level 1 — เข้าใจง่าย

- คำศัพท์
- ความหมาย
- ที่มาคร่าว ๆ
- คำที่เกี่ยวข้อง

### Level 2 — เจาะลึก

- รากศัพท์
- ภาษา
- การเปลี่ยนรูป
- cognates

### Level 3 — เชิงวิชาการ

- PIE reconstruction
- phonological law
- semantic development
- historical period
- references

ผู้ใช้ทั่วไปสามารถหยุดที่ Level 1 ได้

นักเรียน/นักวิชาการสามารถกด “ดูรายละเอียดทางภาษา” เพื่ออ่านต่อ

---

## Principle 03 — Content > Decoration

ถ้าต้องเลือกระหว่าง:

- animation
- glow
- gradient
- border
- icon

กับ

- readability
- whitespace
- hierarchy
- source/reference

ให้เลือกอย่างหลังเสมอ

---

# 4. COLOR SYSTEM

## เปลี่ยนจาก Dark Neon → Light Editorial

ใช้พื้นหลังสีอ่อนเป็นหลัก

### Recommended palette

```text
Page background:
#F7F5F0

Main surface:
#FFFFFF

Secondary surface:
#F1EFE9

Primary text:
#252525

Secondary text:
#686868

Muted text:
#929292

Primary accent:
#176B63

Secondary accent:
#B78628

Link:
#176B63

Border:
#E1DED6

Important highlight:
#F5EEDC
```

### ความหมายของสี

#### Deep Green / Teal

ใช้เป็นสีหลัก

สื่อถึง:

- ความรู้
- ความสงบ
- สถาบัน
- ธรรมชาติ
- ความน่าเชื่อถือ

#### Warm Gold

ใช้เพียงเล็กน้อย

สำหรับ:

- PIE root
- historical highlight
- important information
- citation/reference marker

#### หลีกเลี่ยง

- neon cyan
- neon purple
- neon pink
- bright blue
- gradient rainbow
- glowing borders

---

# 5. TYPOGRAPHY

ต้องให้ภาษาไทยอ่านง่ายมาก

## Recommended Thai fonts

เลือกหนึ่งชุด:

### Option A — Noto Sans Thai

เหมาะกับเว็บไซต์ร่วมสมัย

### Option B — IBM Plex Sans Thai

มี personality ทางวิชาการและเทคโนโลยีเล็กน้อย

### Option C — Anuphan

ดูเป็นมิตรและร่วมสมัย

---

## Typography hierarchy

### H1

ประมาณ 40–48px desktop

น้ำหนัก 600–700

### H2

28–32px

### H3

20–24px

### Body

17–18px

line-height 1.7–1.8

### Metadata

14px

### PIE / linguistic notation

ใช้ serif หรือ font ที่อ่าน Latin phonetic symbols ได้ดี เช่น:

```text
*ph₂tḗr
pitŕ
father
patēr
patriot
paternal
```

ไม่ควรใช้ font ที่ decorative

---

# 6. GLOBAL LAYOUT

Desktop:

```text
┌──────────────────────────────────────────────────────────────┐
│ LOGO                         เมนูหลัก        เกี่ยวกับโครงการ │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│                       MAIN CONTENT                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

Maximum content width:

```text
1200–1280px
```

ไม่ควรทำ content กว้างเต็มจอจนอ่านยาก

---

# 7. HEADER REDESIGN

## ปัจจุบัน

Header มี navigation หลายปุ่มติดกันและใช้สี/emoji เยอะ

## ใหม่

ทำให้เรียบเหมือนเว็บไซต์สถาบัน/ฐานข้อมูล

### Header

ซ้าย:

```text
[ตราสัญลักษณ์/ไอคอน]
สะพานรากศัพท์
Etymological Bridge
```

ใต้ชื่ออาจมี subtitle:

```text
ฐานข้อมูลความสัมพันธ์ทางภาษาศาสตร์
```

ขวา:

```text
ค้นคำศัพท์
คำศัพท์ยอดนิยม
เกี่ยวกับโครงการ
```

และปุ่มเล็ก:

```text
TH | EN
```

### Header behavior

- white background
- sticky ได้
- bottom border บาง ๆ
- ไม่มี glow
- ไม่มี glassmorphism หนัก ๆ

---

# 8. HOME PAGE

Home ต้องเป็นหน้าเริ่มต้นที่เข้าใจได้ภายใน 5 วินาที

## Hero

### Headline

```text
คำหนึ่งคำ
มีเรื่องราวยาวไกลกว่าที่คิด
```

หรือ

```text
ค้นหาที่มาของคำ
แล้วเดินทางย้อนกลับไปถึงรากศัพท์
```

### Supporting text

```text
สำรวจความสัมพันธ์ของคำภาษาไทยกับบาลี–สันสกฤต
Proto-Indo-European และคำร่วมเชื้อสายในภาษาอังกฤษ
```

### Search

ให้ search เป็น element ที่ใหญ่ที่สุดบนหน้า

```text
🔎  ค้นหาคำศัพท์ เช่น “บิดา” หรือ “วิทยา”              [ค้นหา]
```

Search bar:

- white
- border 1px
- shadow very subtle
- radius 10–12px
- height 58–64px

ไม่ใช้ neon glow

---

# 9. HOME PAGE — QUICK DISCOVERY

ใต้ search ให้มี:

## คำที่คนสนใจ

แสดงเป็น text links / chips แบบเรียบ

```text
บิดา
มารดา
ราช
วิทยา
มนุษย์
ทันต
```

อย่าใช้ card ใหญ่

---

# 10. HOME PAGE — WHAT IS ETYMOLOGY?

สร้าง section อธิบายระบบแบบสั้นมาก

### Heading

```text
สะพานรากศัพท์คืออะไร?
```

### Content

```text
เราใช้ข้อมูลทางภาษาศาสตร์เพื่อค้นหาความสัมพันธ์
ระหว่างคำที่ดูเหมือนไม่เกี่ยวข้องกัน
และพาเดินทางย้อนกลับไปยังรากศัพท์ในอดีต
```

แสดงเป็น simple 4-step:

```text
ภาษาไทย
   ↓
บาลี / สันสกฤต
   ↓
Proto-Indo-European
   ↓
คำร่วมเชื้อสายในภาษาอื่น
```

ใช้เส้นบาง ๆ และ typography เป็นหลัก

ไม่ต้องใช้ graph ที่ซับซ้อนใน landing page

---

# 11. SEARCH RESULT PAGE

เมื่อค้นหา `บิดา`

ควรได้หน้าที่อ่านเหมือน “dictionary article”

ไม่ใช่ dashboard

## Top section

```text
บิดา

/bi-dā/

คำนาม
```

ใต้คำ:

```text
ความหมาย
ผู้ให้กำเนิดฝ่ายชาย หรือผู้เป็นพ่อ
```

ถ้ามีแหล่งอ้างอิง:

```text
อ้างอิง: พจนานุกรม ฉบับราชบัณฑิตยสถาน
```

---

# 12. ETYMOLOGICAL BRIDGE

นี่คือ feature สำคัญที่สุด

แทนที่จะทำ 4 cards หนา ๆ ให้ใช้ “เส้นทาง” ที่อ่านจากซ้ายไปขวา

```text
ภาษาไทย
บิดา
   │
   ▼
บาลี / สันสกฤต
pitar / pitā
   │
   ▼
Proto-Indo-European
*ph₂tḗr
   │
   ▼
English
father
```

แต่ละ node เป็น simple editorial block

ไม่ใช้ neon border

---

# 13. ETYMOLOGICAL BRIDGE NODE

ตัวอย่าง:

```text
PROTO-INDO-EUROPEAN

*ph₂tḗr

“father”
ประมาณ 4,500–2,500 BCE
```

ด้านข้างมี small information icon

เมื่อ hover/click:

```text
รากศัพท์ที่นักภาษาศาสตร์สร้างขึ้นจากการเปรียบเทียบ
ข้อมูลในภาษาโบราณและภาษาสมัยใหม่
```

---

# 14. ENGLISH COGNATES

แสดงเป็น section:

```text
คำร่วมเชื้อสายในภาษาอังกฤษ
```

Grid 2–4 columns:

```text
father
Old English

paternal
Latin

patron
Latin

patriot
Greek
```

แต่ละ card:

- white background
- thin border
- small category label
- word ใหญ่
- explanation สั้น
- ไม่มี colored border รอบ card
- ไม่มี emoji

---

# 15. “ทำไมคำเหล่านี้ถึงเกี่ยวข้องกัน?”

นี่เป็น UX สำคัญมาก

ผู้ใช้ทั่วไปอาจเห็น:

```text
บิดา
father
patriot
paternal
```

แล้วสงสัยว่า:

> “มันเกี่ยวกันได้อย่างไร?”

สร้าง explanation block:

```text
ทำไม “บิดา” ถึงเกี่ยวข้องกับ “father”?

คำเหล่านี้มีความสัมพันธ์ทางประวัติศาสตร์ผ่านรากศัพท์
Proto-Indo-European *ph₂tḗr ซึ่งหมายถึง “father”
โดยแต่ละภาษามีการเปลี่ยนเสียงและรูปคำแตกต่างกันตามกาลเวลา
```

ด้านล่าง:

```text
ดูการเปลี่ยนเสียง →
```

---

# 16. PHONOLOGICAL SOUND LAW

ไม่ควรเปิดเป็น giant card

ใช้ accordion:

```text
การเปลี่ยนเสียง

Grimm’s Law
────────────────────────

PIE *p
↓
Germanic *f

ตัวอย่าง:
*ph₂tḗr → father

[ดูคำอธิบายเพิ่มเติม]
```

เมื่อกดจึงขยายรายละเอียด

---

# 17. SEMANTIC DRIFT

ใช้รูปแบบเดียวกัน:

```text
การเปลี่ยนแปลงความหมาย

ความหมายเดิม
     ↓
ความหมายในภาษาอื่น
     ↓
ความหมายในภาษาอังกฤษปัจจุบัน
```

ไม่จำเป็นต้องมี visualization ซับซ้อน

---

# 18. TIMELINE

หน้า Timeline ควรออกแบบเหมือน historical timeline / museum exhibit

แทนที่จะเป็น vertical neon timeline เดิม

ใช้:

```text
4500 BCE
────────────────────────
Proto-Indo-European
*ph₂tḗr
“father”

        ↓

1500 BCE
────────────────────────
Vedic Sanskrit
pitṛ́
“father”

        ↓

500 BCE
────────────────────────
Pali
pitā
“father”

        ↓

ปัจจุบัน
────────────────────────
Thai
บิดา
```

ใช้เส้นสีเทา + จุดสีเขียว

ใช้ทองเฉพาะจุดที่เป็น PIE

---

# 19. INTERACTIVE TREE

Interactive tree เป็น advanced feature

ไม่ควรเป็น default view ของผู้ใช้ทั่วไป

หน้า tree ควรมี introduction ก่อน:

```text
ดูความสัมพันธ์ของคำในรูปแบบต้นไม้

แผนผังนี้แสดงเส้นทางของคำจากรากศัพท์
ไปยังภาษาต่าง ๆ

[ขยายทั้งหมด] [ย่อทั้งหมด] [รีเซ็ต]
```

จากนั้น graph

---

# 20. INTERACTIVE TREE — VISUAL STYLE

เปลี่ยนจาก:

- neon nodes
- rainbow branches
- glowing borders
- oversized empty canvas

เป็น:

- off-white / very light gray canvas
- dark text
- thin branches
- small colored category markers
- compact nodes
- readable labels

ตัวอย่าง node:

```text
PIE
*ph₂tḗr

father
```

ไม่ต้องใส่ icon ทุก node

---

# 21. TREE COLOR CODING

ใช้เพียง 4 สี:

```text
PIE            Gold
Indic          Green
Germanic       Blue-gray
Latin/Greek    Terracotta
```

แต่ต้องมี legend ที่ชัดเจน

สีไม่ควรเป็นสี neon

---

# 22. WORD DETAIL PAGE

เมื่อ click คำว่า `บิดา`

layout:

```text
┌────────────────────────────────────────────────────┐
│ บิดา                                               │
│ คำนาม                                              │
│                                                    │
│ ผู้ให้กำเนิดฝ่ายชาย                                │
│                                                    │
│ อ้างอิง: ราชบัณฑิตยสถาน                           │
└────────────────────────────────────────────────────┘

ที่มาของคำ
────────────────────────────────────────────────────

บิดา
  ↓
pitā
  ↓
*ph₂tḗr

────────────────────────────────────────────────────

คำร่วมเชื้อสาย

father | paternal | patron | patriot

────────────────────────────────────────────────────

การเปลี่ยนเสียง
[Accordion]

การเปลี่ยนความหมาย
[Accordion]

ลำดับเวลา
[ดู Timeline]

แหล่งข้อมูล
[References]
```

---

# 23. DATA SOURCE / AUTHORITY

เนื่องจากเว็บไซต์พัฒนาให้ราชบัณฑิตยสถาน ต้องสร้าง “ความน่าเชื่อถือ” ให้ชัดเจน

อย่าทำให้ดูเหมือน AI สร้างข้อมูลขึ้นเอง

เพิ่ม source metadata:

```text
แหล่งข้อมูล

พจนานุกรม ฉบับราชบัณฑิตยสถาน
ข้อมูลทางภาษาศาสตร์เชิงประวัติศาสตร์
ข้อมูลรากศัพท์ Proto-Indo-European
ข้อมูลคำร่วมเชื้อสาย
```

และ:

```text
ข้อมูลปรับปรุงล่าสุด: 14 กันยายน 2569
```

ถ้าเป็นข้อมูลที่ผ่านการตรวจสอบ:

```text
✓ ตรวจสอบแล้ว
```

ใช้ badge แบบเรียบ ไม่ใช้ glowing badge

---

# 24. FOOTER

Footer เรียบและเป็นทางการขึ้น

```text
สะพานรากศัพท์
Etymological Bridge

ระบบสืบค้นความสัมพันธ์ทางภาษาศาสตร์
เพื่อการเรียนรู้และค้นคว้า

เกี่ยวกับโครงการ
แหล่งข้อมูล
นโยบายการใช้งาน

© ราชบัณฑิตยสถาน
```

ไม่ต้องใส่สถิติ:

```text
43 คำ
146 cognates
39,189 คำถาม
```

ไว้ใน footer เพราะทำให้เว็บดูเหมือน SaaS dashboard

ถ้าต้องการ statistics ให้แสดงเฉพาะหน้าเกี่ยวกับโครงการ

---

# 25. REMOVE / REDUCE

จาก UI เดิม ให้ลดสิ่งเหล่านี้อย่างชัดเจน:

## REMOVE

- neon glow
- gradient background
- multiple colorful borders
- emoji as primary navigation icons
- huge dark cards
- unnecessary badges
- excessive rounded pills
- dashboard-like metrics
- decorative colored dots everywhere
- giant empty graph canvas
- excessive uppercase English
- AI-looking “system status” elements

## REDUCE

- number of cards
- number of colors
- number of buttons
- number of icons
- animation
- shadow
- border radius

---

# 26. ICONOGRAPHY

ใช้ icon library เช่น Lucide

แต่ใช้เฉพาะเมื่อช่วยสื่อความหมาย

ตัวอย่าง:

- Search → Search
- Timeline → Clock / History
- Tree → GitBranch
- Source → BookOpen
- Info → Info
- External reference → ExternalLink

ไม่ใช้ emoji เช่น:

```text
🔎
🌱
⌛
🎓
📚
```

เป็น navigation หลัก

---

# 27. BUTTON STYLE

Primary:

```text
ค้นหา
```

พื้นเขียวเข้ม ตัวอักษรขาว

Secondary:

```text
ดู Timeline
```

พื้น transparent / white border

Tertiary:

```text
อ่านเพิ่มเติม →
```

เป็น text link

ไม่ทำทุกอย่างเป็น pill button

---

# 28. CARD STYLE

ใช้ card เท่าที่จำเป็น

Card:

```text
background: white
border: 1px solid #E1DED6
border-radius: 10px
box-shadow: very subtle
padding: 24px
```

ห้าม:

```text
border neon
glow
gradient
```

---

# 29. SPACING

เว็บไซต์เดิมมี content แน่นบางจุดและมี empty space ใหญ่ในบางจุด

กำหนด spacing system:

```text
8px
12px
16px
24px
32px
48px
64px
80px
```

Section ระหว่างกัน:

```text
64–96px
```

Card ภายใน:

```text
24–32px
```

---

# 30. RESPONSIVE DESIGN

ต้องออกแบบ mobile ตั้งแต่ต้น

## Mobile

Header:

```text
[Logo]                    [☰]
```

Hero:

```text
คำหนึ่งคำ
มีเรื่องราวยาวไกลกว่าที่คิด

[ ค้นหาคำศัพท์... ]

[ค้นหา]
```

Etymological Bridge:

เปลี่ยนจาก horizontal เป็น vertical

```text
ภาษาไทย
  ↓
บาลี / สันสกฤต
  ↓
PIE
  ↓
English
```

Tree:

ให้ scroll horizontally ได้

ห้ามบีบ graph จนอ่านไม่ได้

---

# 31. ACCESSIBILITY

เนื่องจากกลุ่มผู้ใช้กว้าง ต้องให้ความสำคัญกับ accessibility

### Requirements

- contrast ผ่าน WCAG AA
- body text อย่างน้อย 16px
- line-height 1.6+
- keyboard navigation
- visible focus state
- ไม่ใช้สีเป็นตัวบอกข้อมูลเพียงอย่างเดียว
- clickable area อย่างน้อยประมาณ 44px
- tooltip ต้องไม่ใช่ข้อมูลสำคัญเพียงช่องทางเดียว
- mobile readable
- ลด animation ได้เมื่อ `prefers-reduced-motion`

---

# 32. MICROINTERACTION

Animation ควร subtle

ตัวอย่าง:

Search:

```text
focus → border เปลี่ยนเป็น green
```

Card:

```text
hover → ยกขึ้นเล็กน้อย 1–2px
```

Tree:

```text
node selected → highlight แบบ background
```

ไม่ใช้:

- glowing animation
- particles
- floating cards
- animated gradients
- excessive motion

---

# 33. SEARCH UX

Search ต้องรองรับ:

```text
บิดา
บิดา?
บิดา ภาษาอังกฤษ
father
pitā
```

Autocomplete:

```text
บิดา
คำที่เกี่ยวข้อง: พ่อ, บิดา

father
English cognate
```

ถ้าไม่พบ:

```text
ไม่พบคำว่า “xxxxx”

ลองค้นหา:
• คำสะกดใกล้เคียง
• คำภาษาไทย
• คำภาษาอังกฤษ
```

---

# 34. “WOW MOMENT”

เว็บไซต์ยังต้องมี moment ที่ทำให้ผู้ใช้รู้สึกว่า:

> “คำสองคำที่เราไม่เคยคิดว่าจะเกี่ยวกัน จริง ๆ แล้วมีประวัติร่วมกัน”

ตัวอย่าง:

```text
บิดา
      ↘
       *ph₂tḗr → father
      ↗
paternal
```

พร้อมข้อความ:

```text
คำเหล่านี้ไม่ได้เหมือนกันโดยบังเอิญ
แต่มีความสัมพันธ์ทางประวัติศาสตร์ผ่านรากศัพท์ร่วมกัน
```

นี่คือ WOW moment ที่ควรใช้แทน visual effects

---

# 35. HOMEPAGE CONTENT STRUCTURE

ลำดับหน้าแนะนำ:

```text
1. Header

2. Hero
   “คำหนึ่งคำ มีเรื่องราวยาวไกลกว่าที่คิด”

3. Search

4. คำที่น่าสนใจ

5. Etymological Bridge คืออะไร?
   4-step explanation

6. ตัวอย่างคำ
   บิดา / มารดา / วิทยา / ราช

7. How it works
   ค้นหา → เชื่อมโยง → สำรวจ → เรียนรู้

8. Sources / Authority

9. Footer
```

ไม่ควรเอา Timeline และ Tree มาอยู่ในหน้าแรกเต็ม ๆ

---

# 36. INFORMATION ARCHITECTURE

Navigation:

```text
หน้าหลัก
ค้นหาคำ
ต้นไม้รากศัพท์
เส้นเวลา
คำร่วมเชื้อสาย
เกี่ยวกับโครงการ
```

แต่หน้าแรกควรนำไปสู่ “ค้นหาคำ” มากที่สุด

---

# 37. PAGE TYPES

Agent ต้องสร้างอย่างน้อย 5 หน้า/สถานะ:

## Page 01 — Home

จุดเริ่มต้นสำหรับผู้ใช้ทั่วไป

## Page 02 — Search Result

ค้นหา `บิดา`

## Page 03 — Word Detail

รายละเอียดคำว่า `บิดา`

## Page 04 — Interactive Tree

สำรวจความสัมพันธ์ของรากศัพท์

## Page 05 — Timeline

ดูวิวัฒนาการตามช่วงเวลา

---

# 38. DESIGN LANGUAGE EXAMPLE

### Old style

```text
🌐 *ph₂tḗr
[PIE ROOT]

╔════════════════════╗
║ father             ║
║ Old English        ║
╚════════════════════╝
```

### New style

```text
Proto-Indo-European

*ph₂tḗr

“father”

ประมาณ 4,500–2,500 ปีก่อนคริสตกาล
```

เรียบกว่า แต่ดูเป็นแหล่งความรู้มากกว่า

---

# 39. DATA PRESENTATION

ข้อมูลภาษาศาสตร์ควรมี hierarchy:

```text
คำศัพท์
↓
ชนิดคำ
↓
ความหมาย
↓
ภาษา
↓
รูปคำเดิม
↓
ความสัมพันธ์
↓
หลักฐาน
```

อย่าให้ metadata เช่น:

```text
~1500 BCE
Latin
Intermediate B2
```

ใหญ่กว่าคำศัพท์

---

# 40. B2 / A1 LABEL

ถ้ายังต้องมี CEFR เช่น:

```text
General (A1)
Intermediate (B2)
Advanced (B2/C1)
```

ให้ทำเป็น metadata ขนาดเล็ก

ไม่ควรเด่นกว่าข้อมูล etymology

เพราะเป็นข้อมูลเสริม ไม่ใช่ core content

---

# 41. TECHNICAL UI REQUIREMENTS

ถ้า agent สร้างด้วย React / Next.js / Tailwind:

### Components

```text
Header
SearchBar
SearchSuggestions
WordHeader
DefinitionBlock
EtymologyPath
LanguageNode
CognateList
PhonologyAccordion
SemanticAccordion
Timeline
EtymologyTree
SourceList
Footer
```

ควรออกแบบเป็น reusable components

---

# 42. INTERACTION STATES

ทุก component ที่ interactive ต้องมี:

```text
default
hover
focus
active
selected
disabled
loading
empty
error
```

ตัวอย่าง Search:

```text
default:
ค้นหาคำศัพท์...

focus:
border green

loading:
กำลังค้นหา...

empty:
ไม่พบข้อมูล

error:
ไม่สามารถโหลดข้อมูลได้
```

---

# 43. DO NOT FAKE DATA

หาก frontend demo ต้องใช้ mock data ให้ระบุอย่างชัดเจนใน source code

ไม่สร้างข้อมูลอ้างอิงปลอมโดยทำเหมือนเป็นข้อมูลจากราชบัณฑิตยสถาน

หากมี citation:

```text
แหล่งข้อมูล
[ชื่อแหล่งข้อมูล]
[ปี]
[ลิงก์/รายละเอียด]
```

---

# 44. TONE OF VOICE

ภาษาในเว็บ:

## ใช้

```text
ค้นหาที่มาของคำ
ดูความสัมพันธ์
อ่านเพิ่มเติม
ดูหลักฐาน
ดูตามลำดับเวลา
คำร่วมเชื้อสาย
รากศัพท์
ความหมาย
แหล่งข้อมูล
```

## หลีกเลี่ยง

```text
Explore the Knowledge Graph
AI-powered Linguistic Intelligence
Discover Amazing Connections
Semantic Engine
Neural Linguistic Network
```

เพราะทำให้เว็บไซต์ดูเป็น AI product มากเกินไป

---

# 45. BRANDING

ชื่อหลัก:

```text
สะพานรากศัพท์
```

English:

```text
Etymological Bridge
```

Tagline ที่แนะนำ:

```text
เชื่อมคำจากวันนี้
ย้อนรอยไปถึงรากภาษา
```

หรือ:

```text
จากคำหนึ่งคำ สู่เรื่องราวของภาษา
```

เลือกแบบที่ดูเป็นสถาบันมากที่สุด

---

# 46. VISUAL REFERENCE DIRECTION

Agent ควรตีความ visual direction ใกล้เคียง:

- modern digital archive
- contemporary museum website
- academic library
- premium dictionary
- editorial magazine
- cultural institution website

ไม่ใช่:

- AI dashboard
- SaaS landing page
- futuristic interface
- cyberpunk
- gaming UI

---

# 47. FINAL DESIGN TEST

หลังสร้างเสร็จ ให้ agent ตรวจสอบเว็บไซต์ด้วยคำถาม:

### Q1

ผู้ใช้ใหม่รู้หรือไม่ว่าต้องเริ่มจากตรงไหน?

→ ต้องตอบว่า “ค้นหาคำศัพท์”

### Q2

ผู้ใช้มองเห็นคำศัพท์และความหมายภายใน 3 วินาทีหรือไม่?

→ ต้องเห็น

### Q3

ผู้ใช้เข้าใจว่า `บิดา → pitā → *ph₂tḗr → father` เกี่ยวกันอย่างไรหรือไม่?

→ ต้องเข้าใจได้โดยไม่ต้องอ่าน technical explanation ทั้งหมด

### Q4

หน้าเว็บดูเหมือนเว็บไซต์ของสถาบันทางภาษา หรือ AI-generated demo?

→ ต้องเป็นสถาบันทางภาษา

### Q5

สีทั้งหมดมีเหตุผลหรือไม่?

→ ถ้าสีไหนไม่มีหน้าที่ ให้เอาออก

### Q6

ถ้าปิด animation ทั้งหมด เว็บยังดูดีหรือไม่?

→ ต้องดูดี

### Q7

ถ้าลบ card ออกครึ่งหนึ่ง ข้อมูลยังเข้าใจง่ายขึ้นหรือไม่?

→ ถ้าใช่ ให้ลด card

---

# 48. CRITICAL INSTRUCTION FOR THE DESIGN AGENT

**อย่าพยายามรักษาหน้าตาเดิมเอาไว้**

นี่คือ **UX/UI redesign จริง** ไม่ใช่การเปลี่ยนสีจาก dark เป็น light

ให้รักษา:

- ข้อมูล
- functionality
- search
- etymological bridge
- tree
- timeline
- cognates
- phonological explanation
- semantic explanation
- source/reference

แต่ **เปลี่ยนวิธีนำเสนอใหม่ทั้งหมด**

---

# 49. OVERALL VISUAL TARGET

เว็บไซต์สุดท้ายควรให้ความรู้สึกประมาณนี้:

```text
ราชบัณฑิตยสถาน
        +
Modern Digital Archive
        +
Dictionary
        +
Interactive Learning
```

ผลลัพธ์ที่ต้องการ:

> เมื่อเปิดเว็บ ผู้ใช้ควรรู้สึกว่า  
> “นี่คือฐานความรู้ด้านภาษาอย่างเป็นทางการที่ถูกออกแบบมาอย่างดี”
>
> ไม่ใช่  
> “นี่คือเว็บที่ AI สร้างขึ้นมาเพื่อโชว์ว่าทำ interactive ได้”

---

# 50. IMPLEMENTATION PRIORITY

หากเวลาจำกัด ให้ทำตามลำดับ:

### P0 — Must Have

1. Header
2. Home
3. Search
4. Word Result
5. Etymological Bridge
6. Source / citation
7. Responsive mobile

### P1 — Important

8. Cognates
9. Phonological Law
10. Semantic Drift
11. Timeline

### P2 — Advanced

12. Interactive Tree
13. Advanced filtering
14. Learning / quiz features
15. Statistics

**อย่าใช้เวลาไปกับ animation ก่อน P0 เสร็จ**

---

# 51. ONE-SENTENCE DESIGN BRIEF

> **Redesign “Etymological Bridge” as a calm, trustworthy, editorial-style digital language archive for the Royal Institute of Thailand — prioritizing search, readability, linguistic evidence, and natural storytelling over neon visuals, excessive cards, dashboards, and AI-looking decoration.**
