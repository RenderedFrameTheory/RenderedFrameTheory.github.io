# RenderedFrameTheory.github.io

Official Rendered Frame Theory hub — books, Zenodo archives, Hugging Face Spaces, consciousness work, AI systems, and now an open, no-gatekeeping science space.

This repository powers the public RFT Nexus Hub:  
https://renderedframetheory.github.io/

The site exists for one purpose: to give a clean, central access point to everything in the Rendered Frame Theory ecosystem — books, core Zenodo DOIs, Hugging Face Spaces, GitHub repos, and direct channels for feedback, partnerships, support, and collaboration.

---

## 🔭 What this hub actually does

### 1. RFT asset directory (Nexus Hub)

The homepage (`index.html`) shows curated grids:

- **Books**  
  Core RFT titles (the spine of the theory), including for example:
  - *Rendered Frame Theory: The Book They Can't Delete*
  - *Rendered Frame Theory — Einstein's Last Stand: RFT Ends The Matter-verse*
  - *Rendered Frame Theory: Consciousness The Harmonic Field*
  - *The Done Nothing People*
  - *NexFrame Core Protocol*

- **Hugging Face Spaces**  
  Direct links to public `RFTSystems` Spaces, e.g.:
  - **Cosmology & Gravity Lab (RFT)** — interactive cosmology/gravity comparison against FRW/ΛCDM  
    `https://huggingface.co/spaces/RFTSystems/Cosmology_Gravity_Lab`
  - EmergentRFT
  - Symbolic Consciousness
  - NexFrame RFT’s AI
  - DCLR Optimiser  
  - The wider `RFTSystems` collection

- **Zenodo DOIs**  
  Featured core archives, for example:
  - **Unified field framework** — *Rendered Frame Theory: A unified field framework for cosmology, quantum mechanics, consciousness, and geometric physics*  
    `10.5281/zenodo.17867668`
  - **Paradigm shift / master archive** — *Rendered Frame Theory: A paradigm shift in the science of reality* (concept DOI)  
    `10.5281/zenodo.15829720`
  - **RCQM archive** — *RCQM—RFT Consciousness + Quantum Mechanics Archive*  
    `10.5281/zenodo.15865009`
  - **Master IP & legal consolidation** (linked from the Legal section)  
    `10.5281/zenodo.17460107`
  - Plus other RFT archives (Observer Engine, falsification protocols, space tech, etc.)

- **GitHub repositories**  
  Main codebases and demos, e.g.:
  - RFT deformation / cosmology code
  - Conscious-Universe / Observer Engine work
  - NexFrame-related experiments
  - RFTSystems-adjacent repos
  - This website repo itself

Most cards are driven by configuration in `assets/main.js`; key DOIs and the Cosmology & Gravity Lab are also pinned directly in `index.html` for visibility.

---

### 2. Open Science Lab (no gatekeeping)

The **Open Science Lab** (`open-science.html`) is an internal page linked from the main nav and “Internal Pages” grid. It is:

- An **independent, no-gatekeeping hub** for serious work in:
  - Cosmology & gravity
  - Quantum mechanics
  - Consciousness / mind–measurement
  - Geometric physics and related fields
- A curated list of:
  - RFT core archives (Unified Field Framework, Paradigm Shift archive, RCQM, etc.)
  - Key external records (books, labs)
- Governed by a very simple rule set:
  - Respect
  - Clear claims
  - Methods/evidence where possible
  - No spam

Submissions are via GitHub issues or email; inclusion is decided purely on content quality and clarity, not institutional status.

---

### 3. RFT Collaboration Lab — “Help RFT’s Work”

The **Help RFT’s Work / Collaboration Lab** page (`help-rft.html`) is the working floor:

- Documents **live RFT experiments**, starting with the **Mutation Agent / Self-Deciding Brain**:
  - Symbolic civilisation agent
  - Resource limits, mutation, coherence (`kappa`), awakening phases
  - Linked to RFT quantities such as τ_eff and P_max
- Defines a **simple pipeline**:
  1. Publish the active experiment spec (what is being tested).
  2. Take **community parameter sets / ideas / critiques** via GitHub or email.
  3. Run **weekly demo batches** using selected inputs.
  4. Publish outcomes in a public log table on the page.

The page explains exactly what kind of input is useful (parameter ranges, mutation rules, hypotheses) and records demo runs as a permanent log.

---

### 4. Asynchronous “chat” / feedback

The site has a **Feedback** section:

- Users fill in name, email, topic, and message.
- Their **local email client opens** with a fully composed email to the RFT inbox.
- Replies stay in email threads — effectively becoming an ongoing, slow “chat log”.

There is no database, no third-party SaaS, and no backend; everything is handled through email.

---

### 5. Partnership channel

The **Partnerships & Deals** section handles:

- Research collaborations  
- Funding / investment  
- Licensing / commercial use  
- Media / interviews  
- “Other” serious proposals

The form collects:

- Name/organisation  
- Contact email  
- Proposal type  
- Short structured summary  

It simply composes an email with a clear subject,filter, sort, and il respond via email.

---

### 6. Support / orientation channel

The **Support** section is for people who:

- Don’t know where to start with RFT  
- Need code / repo help  
- Are trying to understand a specific paper or Zenodo record  
- Are attempting to reproduce an RFT experiment (e.g. cosmology runs, NexFrame/Observer Engine tests)

Users describe what they’re stuck on; the form creates a support-tagged email so you can triage and reply cleanly.

---

## 🧱 Tech stack

Minimal on purpose:

- **Static HTML**: `index.html` plus internal pages (`ai.html`, `books.html`, `consciousness.html`, `open-science.html`, `help-rft.html`, etc.)
- **CSS**: `assets/styles.css`
- **Vanilla JavaScript**: `assets/main.js` (nav, basic stats, and most of the card data for books/spaces/DOIs/repos)
- **Hosting**: GitHub Pages directly from this repo

No frameworks, no server-side code, no build step.

---

## 📁 Repository structure

High-level layout (only the relevant bits shown):

```text
/
├── index.html              # RFT Nexus Hub (main landing page)
├── open-science.html       # RFT Open Science Lab (no-gatekeeping science hub)
├── help-rft.html           # RFT Collaboration Lab (“Help RFT’s Work”)
├── ai.html                 # AI / NexFrame focused layout
├── books.html              # Extended book information
├── consciousness.html      # Consciousness / codex layout
├── README.md               # This file
└── assets/
    ├── styles.css          # Hub styling (layout, cards, forms, responsive nav)
    └── main.js             # Data (books/spaces/DOIs/repos) + forms + nav + stats
