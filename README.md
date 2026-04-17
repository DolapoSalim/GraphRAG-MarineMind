# 🌊 GraphRAG-MarineMind

A lightweight **GraphRAG-based ecological reasoning system** for analyzing marine ecosystem dynamics using structured knowledge graphs, statistical ecological indicators, and local LLM reasoning.

---

## 🧠 Overview

GraphRAG-MarineMind is a multi-layer retrieval-augmented generation system designed for **marine ecology analysis**, combining:

- 🟢 Knowledge Graph (structured ecological relationships)
- 🟡 Statistical Layer (ecological trends & drivers)
- 🧠 Local LLM reasoning (Phi-3 via Ollama)

The system enables grounded ecological Q&A using structured environmental knowledge.

---

## 🏗️ System Architecture
User Query
↓
Graph Retrieval (Tier 1)
↓
Statistical Lookup (Tier 2)
↓
Context Builder (Fusion Layer)
↓
Phi-3 Mini (Local LLM)
↓
Scientific Answer


---

## 📊 System Components

### 🟢 Tier 1 — Knowledge Graph
Captures ecological relationships such as:

- Sentinel-2 → detects → seagrass_extent  
- Seagrass_loss → reduces → biodiversity  
- Satellite_imagery → estimates → benthic_cover  

---

### 🟡 Tier 2 — Ecological Statistics Layer
Represents ecological trends and drivers:

- seagrass_extent → declining  
- drivers: temperature increase, eutrophication, human activity  
- indicators: NDVI change, habitat fragmentation  

---

### 🧠 LLM Layer (Phi-3 via Ollama)
Used to:
- interpret retrieved ecological knowledge
- generate structured scientific explanations
- avoid hallucination using context grounding

---

## ⚙️ Features

- Fully local LLM inference (Ollama + Phi-3)
- Graph-based ecological reasoning
- Statistical ecological indicator layer
- Context fusion between structured data sources
- Lightweight CLI query engine

---

## 🔬 Example Query

**Input:**
> What methods estimate seagrass extent?

**Output (example):**
- Sentinel-2 satellite imagery  
- Multitemporal remote sensing analysis  
- Benthic cover estimation from satellite data  

---

## 🛠️ Tech Stack

- Python
- Ollama (Phi-3 Mini)
- JSON-based Knowledge Graph
- Rule-based statistical inference layer

---

## 🎯 Purpose

This project demonstrates:
- Hybrid Graph + Statistical RAG design
- Ecological knowledge representation
- Local LLM integration for scientific reasoning
- Early-stage research prototype for marine AI systems

---

## 🚀 Future Improvements

- Vector-based document retrieval (Tier 3)
- FastAPI deployment
- Evaluation framework for retrieval accuracy
- Integration with real Sentinel-2 datasets

---

## 📌 Status

This is an **active research prototype**, designed for experimentation in ecological AI systems and GraphRAG architectures.

## Architecture
                        ┌────────────────────────────┐
                        │        User Query          │
                        └────────────┬───────────────┘
                                     │
                                     ▼
                        ┌────────────────────────────┐
                        │      Query Router          │
                        │ (Intent Detection Layer)   │
                        └────────────┬───────────────┘
                                     │
            ┌────────────────────────┼────────────────────────┐
            │                        │                        │
            ▼                        ▼                        ▼
┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐
│   Tier 1: Graph    │   │   Tier 2: Stats    │   │  Tier 3: Documents │
│  Knowledge Engine  │   │  Statistical Layer │   │  (Future Vector DB)│
│                    │   │                    │   │                    │
│ - Relationships    │   │ - Trends           │   │ - PDFs             │
│ - Methods          │   │ - Drivers          │   │ - Literature       │
│ - Ecological Links │   │ - Indicators       │   │ - Embeddings       │
└─────────┬──────────┘   └─────────┬──────────┘   └─────────┬──────────┘
          │                        │                        │
          └──────────────┬─────────┴──────────────┬─────────┘
                         ▼                        ▼
                ┌────────────────────────────────────┐
                │     Context Aggregation Layer      │
                │ (Unified Ecological Knowledge)     │
                └────────────────────────────────────┘
                                   │
                                   ▼
                ┌────────────────────────────────────┐
                │     Local LLM (Phi-3 / Ollama)     │
                │  Grounded Scientific Explanation   │
                └────────────────────────────────────┘
                                   │
                                   ▼
                        ┌────────────────────────────┐
                        │       Final Answer         │
                        │  (Structured + Grounded)   │
                        └────────────────────────────┘
