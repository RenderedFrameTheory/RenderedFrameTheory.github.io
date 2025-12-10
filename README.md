# RenderedFrameTheory.github.io

Official Rendered Frame Theory hub — books, Zenodo, Hugging Face Spaces, consciousness work, and AI systems.

This repository powers the public RFT Nexus Hub:

> https://renderedframetheory.github.io/

The site exists for one purpose: to give a clean, central access point to everything in the Rendered Frame Theory ecosystem — books, core Zenodo DOIs, Hugging Face Spaces, GitHub repos, and direct channels for feedback, partnerships, and support.

---

## 🔭 What this hub actually does

**1. RFT asset directory**

The homepage shows four curated grids:

- **Books**  
  Core RFT titles (the spine of the theory):
  - *Rendered Frame Theory: The Book They Can't Delete*
  - *Rendered Frame Theory — Einstein's Last Stand: RFT Ends The Matter-verse*
  - *NexFrame Core Protocol*
  - *The Done Nothing People*

- **Hugging Face Spaces**  
  Direct links to public `RFTSystems` spaces (EmergentRFT, Symbolic Consciousness, NexFrame AI, DCLR Optimiser, and the RFTSystems collection).

- **Zenodo DOIs**  
  The key archives: master RFT, RCQM, Observer Engine, falsification protocol, Quantum-Coupled collapse, Matterless/space tech, and Observer Engine series.

- **GitHub repositories**  
  The main codebases: unified deformation, Conscious-Universe, NexFrameRFT, RFTsystems, minimal self demo, and this website.

All of those are rendered automatically from configuration in `assets/main.js`.

---

**2. Asynchronous “chat” / feedback**

The site has a **Feedback** section:

- Users fill in name, email, topic, and message.
- Their local email client opens with a fully composed email to your inbox.
- Replies stay in email threads — effectively becoming an ongoing, slow “chat log”.

No third-party services, no databases, no random SaaS in the middle. Just email.

---

**3. Partnership channel**

Dedicated **Partnerships & Deals** section:

- Name/organisation
- Contact email
- Proposal type (research, funding, licensing, media, other)
- Short summary

Again, this composes an email to your inbox with a clear subject line so you can filter and respond properly. This separates serious offers from random questions.

---

**4. Support / help channel**

**Support** section for people who:

- Don’t know where to start
- Need code / repo help
- Are trying to understand a specific paper
- Are attempting to reproduce an RFT experiment

They describe what they’re stuck on; the email comes through with a clean support subject line so you can triage.

---

## 🧱 Tech stack

Minimal on purpose:

- **Static HTML**: `index.html`
- **CSS**: `assets/styles.css`
- **Vanilla JavaScript**: `assets/main.js`
- Served via **GitHub Pages** from this repo.

---

## 📁 Repository structure

repo is:

```text
/
├── index.html          # RFT Nexus Hub (main landing page)
├── README.md           # This file
└── assets/
    ├── styles.css      # Hub styling (layout, cards, forms, responsive nav)
    └── main.js         # Data (books/spaces/DOIs/repos) + forms + nav + stats
