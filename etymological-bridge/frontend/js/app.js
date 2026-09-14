// ==========================================================================
// Master Application Logic for Etymological Bridge
// ==========================================================================

let activeEntry = null;
let allWordsCache = [];
let categoriesCache = [];

// Expose globally for inline onclick
window.loadWord = loadWord;


document.addEventListener("DOMContentLoaded", async () => {
  setupTabs();
  setupSearch();
  setupChips();
  initD3Graph();
  initQuizSystem();

  await loadInitialData();
  loadWord("มารดา"); // Default initial showcase word
});

// Setup Navigation Tabs
function setupTabs() {
  const tabs = document.querySelectorAll(".nav-tab");
  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      tabs.forEach(t => t.classList.remove("active"));
      tab.classList.add("active");

      const targetId = tab.getAttribute("data-tab");
      document.querySelectorAll(".tab-pane").forEach(pane => pane.classList.remove("active"));
      document.getElementById(targetId).classList.add("active");

      // Redraw D3 graph if opening graph tab to ensure dimensions
      if (targetId === "tab-graph" && activeEntry) {
        fetchGraph(activeEntry.thai_word);
      }
    });
  });
}

// Quick Chip Handlers
function setupChips() {
  const chips = document.querySelectorAll(".chip-btn");
  chips.forEach(chip => {
    chip.addEventListener("click", () => {
      const word = chip.getAttribute("data-word");
      document.getElementById("searchInput").value = word;
      loadWord(word);
    });
  });
}

// Initial Data Loading
async function loadInitialData() {
  try {
    const [statsRes, wordsRes, catRes] = await Promise.all([
      fetch("/api/stats"),
      fetch("/api/words"),
      fetch("/api/categories")
    ]);

    if (statsRes.ok) {
      const stats = await statsRes.json();
      document.getElementById("statThaiCount").innerText = stats.total_entries;
      document.getElementById("statCognateCount").innerText = stats.total_english_cognates;
    }

    if (wordsRes.ok) {
      allWordsCache = await wordsRes.json();
    }

    if (catRes.ok) {
      categoriesCache = await catRes.json();
      renderCategoryFilters(categoriesCache);
      renderCatalogueGrid(allWordsCache);
    }
  } catch (err) {
    console.warn("Using local fallback data:", err);
  }
}

// Search & Autocomplete
function setupSearch() {
  const input = document.getElementById("searchInput");
  const suggestions = document.getElementById("searchSuggestions");
  const clearBtn = document.getElementById("clearSearchBtn");
  const actionBtn = document.getElementById("searchActionBtn");

  input.addEventListener("input", async () => {
    const val = input.value.trim();
    clearBtn.style.display = val ? "block" : "none";

    if (!val) {
      suggestions.style.display = "none";
      return;
    }

    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(val)}`);
      if (res.ok) {
        const matches = await res.json();
        renderSuggestions(matches.slice(0, 6));
      }
    } catch (e) {
      // Offline fallback filter
      const matches = allWordsCache.filter(w => 
        w.thai_word.includes(val) || 
        w.cognates_sample.some(c => c.toLowerCase().includes(val.toLowerCase()))
      );
      renderSuggestions(matches.slice(0, 6));
    }
  });

  clearBtn.addEventListener("click", () => {
    input.value = "";
    clearBtn.style.display = "none";
    suggestions.style.display = "none";
    input.focus();
  });

  actionBtn.addEventListener("click", () => {
    const val = input.value.trim();
    if (val) loadWord(val);
  });

  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      const val = input.value.trim();
      if (val) {
        suggestions.style.display = "none";
        loadWord(val);
      }
    }
  });

  // Close suggestions if clicked outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".search-box-wrapper")) {
      suggestions.style.display = "none";
    }
  });
}

function renderSuggestions(matches) {
  const container = document.getElementById("searchSuggestions");
  if (!matches || matches.length === 0) {
    container.style.display = "none";
    return;
  }

  container.innerHTML = "";
  matches.forEach(m => {
    const item = document.createElement("div");
    item.className = "suggestion-item";
    const sample = (m.cognates_sample || (m.english_cognates ? m.english_cognates.map(c => c.word) : [])).slice(0, 3).join(", ");
    item.innerHTML = `
      <div>
        <span class="sugg-thai">${m.thai_word}</span>
        <span class="sugg-root">${m.pie_root || ""}</span>
      </div>
      <div class="sugg-cognates">↔ ${sample}</div>
    `;
    item.onclick = () => {
      document.getElementById("searchInput").value = m.thai_word;
      container.style.display = "none";
      loadWord(m.thai_word);
    };
    container.appendChild(item);
  });
  container.style.display = "block";
}

// Load and Display Word
async function loadWord(word) {
  const banner = document.getElementById("classificationBanner");
  banner.style.display = "none";

  // Switch to explorer tab if not active
  const explorerTab = document.querySelector("[data-tab='tab-explorer']");
  if (explorerTab && !explorerTab.classList.contains("active")) {
    explorerTab.click();
  }

  try {
    const res = await fetch(`/api/etymology/${encodeURIComponent(word)}`);
    if (!res.ok) throw new Error("Fetch failed");
    const data = await res.json();

    if (data.classification) {
      handleClassificationBanner(data.classification);
    }

    if (data.found && data.entry) {
      activeEntry = data.entry;
      renderActiveWord(data.entry);
      fetchGraph(data.entry.thai_word);
      const card = document.getElementById("wordHeroCard");
      if (card) {
        card.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    } else {
      showNotFoundBanner(word);
    }
  } catch (err) {
    console.error("Load word error:", err);
  }
}


function handleClassificationBanner(cl) {
  const banner = document.getElementById("classificationBanner");
  banner.style.display = "flex";

  if (cl.status === "NATIVE_THAI_WITH_EQUIVALENT") {
    banner.className = "classification-banner native";
    banner.innerHTML = `
      <div class="banner-icon">🌿</div>
      <div>
        <div class="banner-title">${cl.origin_type}: "${cl.word}" (${cl.family})</div>
        <div class="banner-body">${cl.message}</div>
        <button class="banner-action-btn" onclick="loadWord('${cl.suggested_word}')">
          ดูการเชื่อมโยงคำว่า "${cl.suggested_word}" สู่ภาษาอังกฤษ ➔
        </button>
      </div>
    `;
  } else if (cl.is_indic_loanword) {
    banner.className = "classification-banner indic";
    banner.innerHTML = `
      <div class="banner-icon">📜</div>
      <div>
        <div class="banner-title">${cl.origin_type}: "${cl.word}"</div>
        <div class="banner-body">${cl.message}</div>
      </div>
    `;
  } else {
    banner.className = "classification-banner native";
    banner.innerHTML = `
      <div class="banner-icon">💡</div>
      <div>
        <div class="banner-title">${cl.origin_type}</div>
        <div class="banner-body">${cl.message}</div>
      </div>
    `;
  }
}

function showNotFoundBanner(word) {
  const banner = document.getElementById("classificationBanner");
  banner.style.display = "flex";
  banner.className = "classification-banner native";
  banner.innerHTML = `
    <div class="banner-icon">🔍</div>
    <div>
      <div class="banner-title">คำว่า "${word}" อยู่นอกขอบเขตคลังข้อมูลสาธิตปัจจุบัน</div>
      <div class="banner-body">
        ระบบต้นแบบมีคลังคำสาธิตมากกว่า 40 คำหลัก ลองคลิกเลือกคำยอดนิยมด้านบน เช่น 
        <strong>มารดา, ศูนย์, ทันต, วิทยา, บิดา, สุนัข</strong>
      </div>
    </div>
  `;
}

// Render Word in Explorer Tab
function renderActiveWord(entry) {
  // Hero section
  document.getElementById("entryThaiWord").innerText = entry.thai_word;
  document.getElementById("entryThaiRead").innerText = entry.orst_read ? `[${entry.orst_read}]` : "";
  document.getElementById("entryThaiPos").innerText = entry.orst_pos || "น.";
  document.getElementById("entryCategory").innerText = entry.category || "ทั่วไป";
  document.getElementById("entryOriginLang").innerText = entry.pali_sanskrit_lang || "Sanskrit / Pali";
  document.getElementById("entryOrstDefinition").innerText = entry.orst_definition || "-";
  document.getElementById("entryOrstEdition").innerText = entry.orst_edition || "สำนักงานราชบัณฑิตยสภา";
  document.getElementById("entryPieRoot").innerText = entry.pie_root || "*PIE";
  document.getElementById("entryPieMeaning").innerText = `ความหมายดั้งเดิม: "${entry.pie_meaning || ''}" (~4,500 ปีก่อนคริสตกาล)`;

  // 4-Tier Flow
  document.getElementById("flowThaiWord").innerText = entry.thai_word;
  document.getElementById("flowThaiDetail").innerText = `คำยืมบาลี-สันสกฤต (${entry.orst_pos || 'น.'})`;
  document.getElementById("flowSanskritWord").innerText = entry.pali_sanskrit_form || "-";
  document.getElementById("flowSanskritMeaning").innerText = `ความหมายเดิม: "${entry.pali_sanskrit_meaning || ''}"`;
  document.getElementById("flowPieRoot").innerText = entry.pie_root || "*PIE";
  document.getElementById("flowPieMeaning").innerText = `รากเหง้า: "${entry.pie_meaning || ''}"`;

  const flowEnList = document.getElementById("flowEnglishList");
  flowEnList.innerHTML = "";
  (entry.english_cognates || []).forEach(cog => {
    const pill = document.createElement("span");
    pill.className = "cog-pill";
    pill.innerText = cog.word;
    flowEnList.appendChild(pill);
  });

  // Phonological Law & Drift
  document.getElementById("entrySoundLaw").innerText = entry.sound_change_law || "สืบทอดตามสายตระกูลภาษาอินโด-ยูโรเปียน";
  document.getElementById("entryDriftScore").innerText = entry.semantic_drift_score || "Low";
  document.getElementById("entryDriftNote").innerText = entry.semantic_drift_note || "ความหมายใกล้เคียงกับรากเดิม";

  // Detailed Cognates Cards
  const cogGrid = document.getElementById("cognatesGrid");
  cogGrid.innerHTML = "";
  (entry.english_cognates || []).forEach(cog => {
    const card = document.createElement("div");
    card.className = "cognate-card";
    card.innerHTML = `
      <div>
        <div class="cog-card-header">
          <span class="cog-card-word">${cog.word}</span>
          <span class="cog-card-diff">${cog.difficulty || 'General'}</span>
        </div>
        <div class="cog-card-origin">${cog.origin_language || 'English'}</div>
        <div class="cog-card-path">${cog.derivation_path || ''}</div>
      </div>
      <div class="cog-card-note">💡 ${cog.usage_note || ''}</div>
    `;
    cogGrid.appendChild(card);
  });

  // Specialized Terms (if any)
  const specSection = document.getElementById("specializedSection");
  const specGrid = document.getElementById("specializedTermsGrid");
  if (entry.specialized_terms && entry.specialized_terms.length > 0) {
    specSection.style.display = "block";
    specGrid.innerHTML = "";
    entry.specialized_terms.forEach(t => {
      const card = document.createElement("div");
      card.className = "spec-term-card";
      card.innerHTML = `
        <div class="spec-domain">${t.domain}</div>
        <div class="spec-en">${t.english_term}</div>
        <div class="spec-th">${t.thai_term}</div>
      `;
      specGrid.appendChild(card);
    });
  } else {
    specSection.style.display = "none";
  }

  // Timeline
  renderTimeline(entry.timeline || []);
}

// Render Timeline
function renderTimeline(timeline) {
  const track = document.getElementById("timelineTrack");
  track.innerHTML = "";
  timeline.forEach(item => {
    const node = document.createElement("div");
    node.className = "timeline-node";
    node.innerHTML = `
      <div class="timeline-era">${item.era}</div>
      <div class="timeline-stage">${item.stage}</div>
      <div class="timeline-form">${item.form}</div>
      <div class="timeline-desc">${item.meaning}</div>
    `;
    track.appendChild(node);
  });
}

// Fetch D3 Graph Data
async function fetchGraph(word) {
  try {
    const res = await fetch(`/api/graph/${encodeURIComponent(word)}`);
    if (res.ok) {
      const graphData = await res.json();
      renderD3Graph(graphData);
    }
  } catch (err) {
    console.error("Fetch graph error:", err);
  }
}

// Render Categories
function renderCategoryFilters(cats) {
  const filterRow = document.getElementById("categoryPillFilters");
  filterRow.querySelectorAll(".cat-pill:not([data-cat='ALL'])").forEach(b => b.remove());

  cats.forEach(c => {
    const btn = document.createElement("button");
    btn.className = "cat-pill";
    btn.setAttribute("data-cat", c.category);
    btn.innerText = `${c.category} (${c.count})`;
    btn.onclick = () => {
      filterRow.querySelectorAll(".cat-pill").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");
      filterCatalogue(c.category);
    };
    filterRow.appendChild(btn);
  });

  const allBtn = filterRow.querySelector("[data-cat='ALL']");
  allBtn.onclick = () => {
    filterRow.querySelectorAll(".cat-pill").forEach(p => p.classList.remove("active"));
    allBtn.classList.add("active");
    renderCatalogueGrid(allWordsCache);
  };
}

function filterCatalogue(category) {
  const filtered = allWordsCache.filter(w => w.category === category);
  renderCatalogueGrid(filtered);
}

function renderCatalogueGrid(words) {
  const grid = document.getElementById("catalogueGrid");
  grid.innerHTML = "";

  words.forEach(w => {
    const card = document.createElement("div");
    card.className = "catalogue-card";
    const cogs = (w.cognates_sample || []).map(c => `<span class="cog-tag">${c}</span>`).join("");
    card.innerHTML = `
      <div>
        <div class="cat-card-top">
          <span class="cat-card-word">${w.thai_word}</span>
          <span class="cat-card-pie">${w.pie_root || ''}</span>
        </div>
        <p class="cat-card-def">${w.orst_definition || 'คำบาลี-สันสกฤตในภาษาไทย'}</p>
      </div>
      <div class="cat-card-cogs">${cogs}</div>
    `;
    card.onclick = () => {
      document.querySelector("[data-tab='tab-explorer']").click();
      document.getElementById("searchInput").value = w.thai_word;
      loadWord(w.thai_word);
      window.scrollTo({ top: 0, behavior: "smooth" });
    };
    grid.appendChild(card);
  });
}
