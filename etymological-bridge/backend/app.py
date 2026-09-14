# -*- coding: utf-8 -*-
"""
FastAPI REST API Server for Etymological Bridge
Serves REST endpoints for data traversal and hosts the interactive frontend UI.
"""

import os
import sys
from typing import Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from engine import EtymologyEngine

app = FastAPI(
    title="Etymological Bridge API",
    description="ระบบเชื่อมโยงคำยืมบาลี-สันสกฤตในภาษาไทย ↔ Cognates ภาษาอังกฤษ ผ่าน Proto-Indo-European (PIE)",
    version="1.0.0"
)

# Enable CORS for local web development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = EtymologyEngine()
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))


@app.get("/api/stats")
def get_stats():
    """Returns general statistics about the knowledge graph and ORST official coverage."""
    return engine.get_stats()


@app.get("/api/words")
def get_words(category: Optional[str] = None):
    """Returns a list of indexed Thai words with metadata."""
    return engine.list_all(category=category)


@app.get("/api/categories")
def get_categories():
    """Returns distinct categories with word counts."""
    cat_counts = {}
    for entry in engine.entries:
        cat = entry.get("category", "ทั่วไป")
        cat_counts[cat] = cat_counts.get(cat, 0) + 1
    return [{"category": k, "count": v} for k, v in sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)]


@app.get("/api/search")
def search_words(q: str = Query(..., description="Query in Thai, English, PIE root, or category")):
    """Searches words across Thai headwords, English cognates, and PIE roots."""
    return engine.search(q)


@app.get("/api/classify")
def classify_word(word: str = Query(..., description="Thai word to classify")):
    """Classifies if a word is Indic (Sanskrit/Pali) or Native Thai (Kra-Dai)."""
    return engine.classify(word)


@app.get("/api/etymology/{word}")
def get_etymology(word: str):
    """Retrieves full etymological evolution chain for a word."""
    entry = engine.lookup(word)
    classification = engine.classify(word)
    if not entry and not classification.get("entry"):
        return {
            "found": False,
            "classification": classification,
            "message": f"คำว่า '{word}' อยู่นอกขอบเขตคลังข้อมูลสาธิตปัจจุบัน"
        }

    active_entry = entry or classification.get("entry")
    return {
        "found": True,
        "entry": active_entry,
        "classification": classification
    }


@app.get("/api/graph/{word}")
def get_graph(word: str):
    """Returns graph nodes and links formatted for D3.js visualization."""
    graph_data = engine.get_d3_graph(word)
    if not graph_data:
        raise HTTPException(status_code=404, detail="Word not found in etymology graph")
    return graph_data


@app.get("/api/quiz")
def get_quiz(count: int = Query(5, ge=1, le=20)):
    """Generates dynamic quiz questions for educational mode."""
    return engine.generate_quiz(count)


# Serve frontend — index first, then static assets
@app.get("/")
def index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# Mount at root AFTER API routes so /api/* takes priority
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="static")


if __name__ == "__main__":
    import uvicorn
    print("Starting Etymological Bridge API server at http://127.0.0.1:8089 ...")
    uvicorn.run(app, host="127.0.0.1", port=8089)

