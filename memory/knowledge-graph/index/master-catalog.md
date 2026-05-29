# MASTER CATALOG — Knowledge Graph Index
*Elite-grade knowledge base with 85+ sources, 1.68M words, 161+ hours*

---

## Quick Stats

| Metric | Value |
|--------|-------|
| **Total Sources** | 106 |
| **Total Words** | ~1,831,400 |
| **Total Duration** | ~319 hours |
| **Concepts Mapped** | 42+ |
| **Last Updated** | 2026-03-31 |

---

## Domain Taxonomy

```
knowledge-graph/
├── 📊 MATHEMATICS & ML
│   ├── Neural Networks (3Blue1Brown series)
│   ├── Markov Chains
│   ├── Linear Algebra (implied)
│   └── Probability Theory
│
├── 💻 COMPUTER SCIENCE
│   ├── CS50 (Full, Python, Flask)
│   ├── Stanford CS106A (28 lectures)
│   ├── Java Full Course
│   └── C++ Programming
│
├── 🔐 CYBERSECURITY
│   ├── Bug Bounty Methodology (Jason Haddix)
│   ├── OSINT (The Cyber Mentor, Loi Liang Yang)
│   ├── AI/LLM Security (HexStrike, AI Hacker)
│   ├── Microsoft/Azure Exploitation (GraphSpy)
│   └── Malware Analysis (NetworkChuck, CyberFlow)
│
├── 🤖 AI & AUTOMATION
│   ├── OpenClaw Mastery (Multiple sources)
│   ├── n8n Workflows
│   ├── Claude Code Mastery
│   └── Local LLMs (Ollama)
│
└── 🔮 ESOTERIC & RESEARCH
    ├── Numerology (2 sources)
    └── CIA Document (Reality)
```

---

## Source Registry (by Category)

### 🧠 NEURAL NETWORKS & DEEP LEARNING (3Blue1Brown Complete)

| ID | Title | Duration | Words | Difficulty |
|----|-------|----------|-------|------------|
| 3b1b-ch1-neural-network | What is a Neural Network? | 18 min | 2,869 | Beginner |
| 3b1b-ch2-gradient-descent | Gradient Descent | 21 min | 3,100 | Intermediate |
| 3b1b-ch3-backprop-intuitive | Backpropagation Intuitively | 13 min | 1,900 | Intermediate |
| 3b1b-ch4-backprop-calculus | Backpropagation Calculus | 11 min | 1,600 | Advanced |
| 3b1b-ch5-llms-explained | LLMs Explained Briefly | 6 min | 1,100 | Beginner |
| 3b1b-ch6-transformers | Transformers | 26 min | 4,400 | Advanced |
| 3b1b-ch7-attention | Attention in Transformers | 24 min | 4,200 | Advanced |
| 3b1b-ch8-llm-facts | How LLMs Store Facts | 15 min | 4,000 | Advanced |
| 3b1b-ch9-ai-images-videos | AI Images & Videos | 22 min | 6,500 | Intermediate |
| neural-network-scratch | I Built a NN from Scratch | 9 min | 1,600 | Intermediate |

**Prerequisite Chain:** ch1 → ch2 → (ch3 OR ch4) → ch5 → ch6 → ch7 → ch8 → ch9

---

### 🎓 COMPUTER SCIENCE FOUNDATIONS

| ID | Title | Duration | Words | Concepts |
|----|-------|----------|-------|----------|
| cs50-full-course | CS50 Full Computer Science | 24.5 hrs | 289,000 | C, algorithms, memory, data structures |
| cs50-python-2022 | CS50 Python | 16 hrs | 184,000 | Python, APIs, SQL, Flask |
| cs50-flask-web-programming | CS50 Flask Web Programming | 2.5 hrs | 21,000 | Flask, Jinja, sessions |
| stanford-cs106a-lec1-28 | Stanford CS106A (28 lectures) | ~22 hrs | 221,000 | Java, Karel, programming fundamentals |
| java-full-course | Java Full Course | 2.5 hrs | 25,000 | Java basics, OOP |
| cpp-course-beginner-advanced | C++ Programming Course | 31 hrs | 340,000 | **LARGEST SOURCE** — C++ fundamentals to advanced |

**Prerequisite Chain:** cs50-full → (cs50-python OR stanford-cs106a) → cs50-flask

---

### 🎯 BUG BOUNTY & SECURITY METHODOLOGY

| ID | Title | Duration | Words | Instructor |
|----|-------|----------|-------|------------|
| bug-hunter-methodology | The Bug Hunter's Methodology | 1h 54m | 12,600 | **Jason Haddix** |
| bug-hunter-app-analysis | Application Analysis | 47 min | 7,000 | Jason Haddix |
| live-recon-snapchat | Live Recon on Snapchat | 1h 42m | 12,900 | @ITSecurityGuard |
| manual-hacking-guide | Manual Hacking Full Guide | 1h 26m | 13,700 | JakSec |

**Cross-References:** All reference `recon-methodology`, `subdomain-enumeration`, `scope-expansion`

---

### 🕵️ OSINT (Open Source Intelligence)

| ID | Title | Duration | Words | Instructor |
|----|-------|----------|-------|------------|
| osint-5hr-course | OSINT in 5 Hours — Full Course | 4.5 hrs | 45,200 | **The Cyber Mentor** |
| osint-beginners-find-anyone | OSINT for Beginners | 14 min | 2,400 | Loi Liang Yang |
| osint-5min-overview | Every OSINT Technique in 5 Min | 4 min | 677 | Mr Ethical Hacker |

---

### 🤖 OPENCLAW & AI AUTOMATION

| ID | Title | Duration | Words | Creator |
|----|-------|----------|-------|---------|
| openclaw-master-10hr | Master OpenClaw in 10 Hours | 10 hrs | 64,300 | **Mani Kanasani** |
| openclaw-6hour-course | OpenClaw AI Full 6 Hour Course | 6 hrs | 61,900 | Julian Goldie |
| agentic-workflows-course | Agentic Workflows 6 Hour Course | 5.7 hrs | 66,200 | **Nick Saraev** |
| claude-code-course | CLAUDE CODE Full Course 4 Hours | 4 hrs | 56,300 | Nick Saraev |
| openclaw-army-agents | Build an Army of OpenClaw Agents | 18 min | 3,500 | Alex Finn |
| openclaw-condensed-lessons | 100 Hours of Lessons in 35 Min | 35 min | 6,700 | Alex Finn |
| openclaw-fixed-setup | I Fixed OpenClaw (Full Setup) | 1h 4m | 8,500 | Greg Isenberg |
| openclaw-making-money | Making $$$ with OpenClaw | 52 min | 8,000 | Greg Isenberg |
| n8n-tutorial-zero-to-hero | n8n Tutorial — Zero to Hero | 3.5 hrs | 35,400 | freeCodeCamp |

---

### 🔓 SECURITY TOOLS & EXPLOITATION

| ID | Title | Duration | Words | Focus |
|----|-------|----------|-------|-------|
| graphspy-john-hammond | GraphSpy Deep Dive | 42 min | 8,100 | **Microsoft/Azure/Entra ID exploitation** |
| hexstrike-mcp-hacking | HexStrike AI MCP for Hacking | 14 min | 2,200 | AI-powered CTF solving |
| hacker101-javascript | JavaScript for Hackers | 24 min | 3,900 | JS security analysis |
| android-hacking-workshop | Android Hacking Workshop | 18 min | 1,800 | Mobile app security |
| networkchuck-mitm-attack | MiTM Attack (Polish) | 19 min | 436 | Packet sniffing |
| malware-creation-cyberflow | How To Make Your OWN Malware | 7 min | 1,300 | Educational malware |
| python-malware-networkchuck | Python Malware (Ransomware) | 25 min | 5,300 | Python Fernet encryption |
| darkweb-exposed | Dark Web Exposed | 20 min | 3,800 | Dark web exploration |

---

### 🏢 POWER PLATFORM & BUSINESS APPLICATIONS

| ID | Title | Duration | Words | Instructor |
|----|-------|----------|-------|------------|
| **powerapps-gen-pages-ideas-app-raza** | **Generative Pages - AI Powered App Creation** | **11 min** | **1,397** | **Image-to-UI, Theme Switching, Voting System** |
| **powerapps-gen-pages-ideas-app-raza** | **Generative Pages - AI Powered App Creation** | **11 min** | **1,397** | **Image-to-UI, Theme Switching, Voting System** |
| **powerapps-model-driven-modern-raza** | **How to build Model-Driven Power Apps the Modern Way** | **8 min** | **1,533** | **Copilot, Plan Designer, Generative Pages** |
| powerapps-full-course-pragmaticworks | **Power Apps Full Course** | 3.5 hrs | 45,000 | **Brian Knight (MVP)** |
| powerapps-containers-responsive-design | Power Apps Containers & Layouts | 1 hr | 12,000 | Responsive design series |
| powerapps-charity-hackathon-course | **Charity Hackathon Course** | 4 hrs | 45,000 | **Multi-instructor team** |
| lido-pdf-extraction-automation | Lido - PDF Invoice Extraction | 6 min | 779 | PDF to Excel automation |
| **powerapps-vibe-coding-raza** | **Power Apps Vibe Coding - Order Management** | **32 min** | **3,859** | **AI agents, React, Dataverse, ALM** |
| **powerapps-modern-combo-box-raza** | **Modern Combo Box - Multi-Select People Picker** | **18 min** | **2,700** | **Large datasets, server-side filtering** |
| **powerapps-confirm-function-raza** | **Confirm Function - Native Dialog Boxes** | **11 min** | **1,950** | **Delete confirmation, unsaved changes** |
| **powerapps-responsive-editable-gallery-raza** | **Responsive Editable Gallery - Horizontal/Vertical Scroll** | **24 min** | **2,850** | **CRUD operations, responsive design** |
| **powerapps-navigation-component-raza** | **Navigation Component - Two-Level Expandable Menu** | **21 min** | **2,800** | **Security trimming, responsive** |
| **powerapps-modern-card-control-raza** | **Modern Card Control - Dynamic Responsive Cards** | **12 min** | **1,900** | **Gallery, thumbnails, SVG icons** |
| **powerapps-grid-container-raza** | **Grid Container Control - Responsive Grid Layouts** | **13 min** | **2,100** | **Rows/columns, form design** |
| **powerapps-tools-ecosystem-raza** | **Power Apps Tools Ecosystem - No-Code to Pro-Code** | **16 min** | **2,700** | **App Builder, Vibe coding, Code Apps** |
| **powerapps-dataverse-mcp-raza** | **Dataverse MCP Server - Copilot Studio & Power Apps** | **14 min** | **2,300** | **SQL queries, CRUD, MCP tools** |
| **powerapps-sort-filter-delegation-raza** | **Sort & Filter Multiple Columns - Delegation** | **23 min** | **3,150** | **SharePoint, SortByColumns, dynamic filters** |
| **powerapps-gallery-tabbed-filters-raza** | **Gallery with Tabbed Filters - Step-by-Step** | **18 min** | **2,600** | **Horizontal gallery, named formulas, Lookup** |
| **powerapps-excel-to-powerapp-raza** | **Excel to Power App - Multi-Sheet, Pivot Tables** | **22 min** | **2,850** | **Dataverse, lookups, calculated columns** |
| **powerapps-quiz-app-raza** | **Complete Quiz App - React Pages, Security Roles** | **11 min** | **2,300** | **Plan Designer, generative pages, timer** |
| **powerapps-kudo-board-raza** | **Kudo Board - Team Celebration Platform** | **7 min** | **1,750** | **Generative pages, rich text, board locking** |

**Covers:** Canvas apps, Dataverse, Model-Driven apps, Power Pages, formulas, galleries, forms, containers, responsive design, charity projects, end-to-end builds, PDF extraction, Vibe coding, AI agents, modern controls, combo box, people picker, confirm function, dialog boxes, editable gallery, horizontal/vertical scroll, navigation component, card control, grid container, app builder, code apps, Dataverse MCP, SQL queries, sort, filter, delegation, tabbed filters, Excel import, quiz application, Kudo board

---

### 🧠 AI & MACHINE LEARNING

| ID | Title | Duration | Words | Focus |
|----|-------|----------|-------|-------|
| generative-ai-full-course | Generative AI Full Course | 30 hrs | 292,000 | **LARGEST ML SOURCE** |
| ai-hard-way-networkchuck | You've Been Using AI the Hard Way | 33 min | 6,400 | AI workflow optimization |
| prompting-ai-networkchuck | You SUCK at Prompting AI | 23 min | 4,500 | Prompt engineering |
| mcp-networkchuck | Learn MCP Right Now | 38 min | 6,700 | Model Context Protocol |
| free-ai-coders-2026 | 8 Secret Fully Free AI Coders | 11 min | 2,300 | Free AI tools |
| ollama-uncensored-zade | Run YOUR own UNCENSORED AI | 26 min | 5,000 | Local LLM deployment |
| ollama-claude-code | Free Unlimited Cloud LLM Tool | 15 min | 2,200 | Ollama + Claude Code |
| **networkchuck-openclaw-review-2026** | **OpenClaw: Full Review + Setup** | **47 min** | **6,859** | **Complete setup, security, demos** |

**Covers:** OpenClaw setup, Telegram bot, VPS deployment, security hardening, crons, heartbeats, skills, sub-agents, IT team automation

---

### 📚 ADDITIONAL SOURCES

| ID | Title | Duration | Words | Category |
|----|-------|----------|-------|----------|
| numerology-beginners | Numerology For Beginners | 3.3 hrs | 35,000 | Esoteric |
| numerology-divine-triangle-1979 | Numerology and the Divine Triangle | 11 hrs | 102,000 | Esoteric |
| cia-reality-document | CIA Document: How Reality Works | 45 min | 7,000 | Research |
| free-ebooks-audiobooks-libby-hoopla | Free Ebooks & Audiobooks Guide | 13 min | 2,800 | Resources |
| manim-3b1b-demo | How I Animate 3Blue1Brown | 53 min | 11,100 | Visualization |

---

## Concept Index

### Mathematics
- [neural-networks](corpus/by-concept/syntheses/neural-networks.md) — Architecture, forward/backward pass, training
- [markov-chains](corpus/by-concept/markov-chains.json) — Stochastic processes, memoryless property
- [gradient-descent](corpus/by-concept/syntheses/gradient-descent.md) — Optimization, learning rates, convergence
- [backpropagation](corpus/by-concept/syntheses/backpropagation.md) — Chain rule, gradient flow
- [transformers](corpus/by-concept/syntheses/transformers.md) — Attention mechanism, self-attention

### Cybersecurity
- [reconnaissance](corpus/by-concept/syntheses/reconnaissance.md) — OSINT, subdomain enumeration, scope expansion
- [bug-bounty-methodology](corpus/by-concept/syntheses/bug-bounty-methodology.md) — Haddix methodology, live recon
- [microsoft-entra-exploitation](corpus/by-concept/syntheses/microsoft-entra-exploitation.md) — GraphSpy, device code phishing
- [malware-development](corpus/by-concept/syntheses/malware-development.md) — Python Fernet, persistence

### AI/Automation
- [openclaw-mastery](corpus/by-concept/syntheses/openclaw-mastery.md) — Multi-agent workflows, tool calling
- [openclaw-setup-security](corpus/by-concept/openclaw-setup-security.json) — VPS setup, Telegram bot, security hardening
- [claude-code-optimization](corpus/by-concept/syntheses/claude-code-optimization.md) — Local models, GLM-4.7
- [n8n-workflows](corpus/by-concept/syntheses/n8n-workflows.md) — Automation, triggers, nodes
- [mcp-protocol](corpus/by-concept/syntheses/mcp-protocol.md) — Model Context Protocol, tool integration

### Business Automation
- [pdf-extraction-automation](corpus/by-concept/pdf-extraction-automation.json) — PDF to Excel, invoice processing, Lido

### Power Platform
- [powerapps-gen-pages-advanced](corpus/by-concept/powerapps-gen-pages-advanced.json) — **Advanced generative pages: image-to-UI, theme switching, voting, Excel export** | Image reference design, Interactive charts, Dark/light mode, Flyout forms, Command threads | Model-driven apps with Gen Pages
- [powerapps-model-driven-modern](corpus/by-concept/powerapps-model-driven-modern.json) — **Modern approach using Copilot, Plan Designer, and Generative Pages** | Copilot data modeling, Plan Designer AI agents, Generative Pages (React), In-App Agents, Data Exploration/Visualization | Model-driven apps
- [powerapps-vibe-coding](corpus/by-concept/powerapps-vibe-coding.json) — AI agents, React apps, Dataverse, natural language development
- [powerapps-modern-controls](corpus/by-concept/powerapps-modern-controls.json) — Modern combo box, people picker, large datasets, server-side filtering
- [powerapps-confirm-function](corpus/by-concept/powerapps-confirm-function.json) — Native dialog boxes, delete confirmation, unsaved changes
- [powerapps-responsive-gallery](corpus/by-concept/powerapps-responsive-gallery.json) — Responsive galleries, horizontal/vertical scroll, editable grids, CRUD
- [powerapps-navigation-component](corpus/by-concept/powerapps-navigation-component.json) — Two-level navigation, expandable menus, security trimming
- [powerapps-card-control](corpus/by-concept/powerapps-card-control.json) — Dynamic responsive cards, thumbnails, gallery integration
- [powerapps-grid-container](corpus/by-concept/powerapps-grid-container.json) — Grid layouts, rows/columns, form positioning
- [powerapps-ecosystem](corpus/by-concept/powerapps-ecosystem.json) — No-code to pro-code spectrum, App Builder, Plan Designer, Code Apps
- [dataverse-mcp](corpus/by-concept/dataverse-mcp.json) — Model Context Protocol, SQL queries, AI agent data access
- [powerapps-delegation](corpus/by-concept/powerapps-delegation.json) — Sort, Filter, multiple columns, delegable queries, SharePoint
- [powerapps-tabbed-filters](corpus/by-concept/powerapps-tabbed-filters.json) — Horizontal gallery tabs, named formulas, Lookup, visual filtering
- [excel-to-powerapp](corpus/by-concept/excel-to-powerapp.json) — Excel import, Dataverse tables, lookups, calculated columns, pivot tables
- [quiz-application](corpus/by-concept/quiz-application.json) — Complete quiz app, Plan Designer, generative pages, React, security roles, timer
- [kudo-board](corpus/by-concept/kudo-board.json) — Team celebration board, generative pages, rich text, image upload, board locking

---

## Query Protocol

**When user asks a question:**

1. **Check sources FIRST** — Search knowledge base before general knowledge
2. **Cross-reference** — Pull related concepts across multiple sources
3. **Cite exact quotes** — Use verbatim text with source attribution
4. **Flag gaps** — If library is silent on topic, explicitly state this
5. **Synthesize** — Combine insights from multiple sources when applicable

**Prerequisites Enforced:**
- Complex neural network math → Requires Linear Algebra 101
- Transformer architecture → Requires neural-networks + attention
- Advanced recon → Requires OSINT fundamentals

---

## File Locations

```
memory/knowledge-graph/
├── corpus/
│   ├── by-source/{source-id}/
│   │   ├── metadata.json
│   │   └── chunks/chunk_001.txt
│   └── by-concept/
│       ├── {concept-id}.json
│       └── syntheses/{concept-id}.md
├── ontology/
│   ├── prerequisites.json
│   └── domains.json
└── index/
    └── master-catalog.md  ← YOU ARE HERE
```

---

*Built to elite-grade standards. 1.68M words. Zero shortcuts.*
