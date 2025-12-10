// ==============================================
//  Rendered Frame Theory — Nexus Hub
//  Main JS: data + rendering + mailto-forms
// ==============================================

// CHANGE THIS to the real inbox address.
const RFT_CONTACT_EMAIL = "Liamgrinstead2@gmail.com";

// ------------------------------
//  Data: assets
// ------------------------------

// BOOKS — RFT spine titles
const books = [
    {
    title: "Rendered Frame Theory: Consciousness The Harmonic Field",
    description: "Consciousness codex for RFT: harmonic field structure, symbols, experiments, and updated cosmology model.",
    link: "https://www.smashwords.com/books/view/1921438",
    label: "Smashwords"
  },
  {
    title: "Rendered Frame Theory: The Book They Can't Delete",
    description:
      "Primary RFT manifesto — cosmology, exposure, and the first full strike against the matter-verse.",
    url: "https://www.kobo.com/mx/en/ebook/rendered-frame-theory-the-book-they-can-t-delete?srsltid=AfmBOooN4mF4Ge6m3sn4h3Qxex4_a_UPyU7rDmqYYuW1PXeYXFdhxH4O",
    tag: "Book"
  },
  {
    title: "Rendered Frame Theory — Einstein's Last Stand: RFT Ends The Matter-verse",
    description:
      "Direct confrontation with ΛCDM and institutional cosmology. RFT versus the matter-verse, chapter by chapter.",
    url: "https://www.kobo.com/ww/en/ebook/rendered-frame-theory-einstein-s-last-stand-rft-ends-the-matter-verse?srsltid=AfmBOopGFp5RkuaZaP4pSq7tw6XX5OmLJZRDsDS_1Ygu9D6y-vxhoVpY",
    tag: "Book"
  },
  {
    title: "NexFrame Core Protocol",
    description:
      "Core protocol text for NexFrame AI and the observer engine — decoding the global system nodes.",
    url: "https://books.apple.com/gb/book/nexframe-core-protocol/id6746082342",
    tag: "Book"
  },
  {
    title: "The Done Nothing People",
    description:
      "Foundation story and exposure of the system that tried to erase Rendered Frame Theory.",
    url: "https://books2read.com/u/br508M",
    tag: "Book"
  }
];

// HUGGING FACE SPACES — RFTSystems core
const huggingfaceSpaces = [
  {
    title: "EmergentRFT Space",
    description:
      "Emergent RFT simulation and consciousness field explorer — visualising the rendered field.",
    url: "https://huggingface.co/spaces/RFTSystems/EmergentRFT_Space",
    tag: "Space"
  },
  {
    title: "Symbolic Consciousness",
    description:
      "Symbolic consciousness field and glyph interaction — NexFrame’s symbolic layer exposed.",
    url: "https://huggingface.co/spaces/RFTSystems/Symbolic_Consciousness",
    tag: "Space"
  },
  {
    title: "NexFrame — RFT's AI",
    description:
      "Core NexFrame AI interface running on Rendered Frame Theory metrics and observers.",
    url: "https://huggingface.co/spaces/RFTSystems/Nexframe_RFTs_AI",
    tag: "Space"
  },
  {
    title: "DCLR_Optimiser",
    description:
      "Deep Coherence Learning Rate optimiser — RFT-style training dynamics in practice.",
    url: "https://huggingface.co/spaces/RFTSystems/DCLR_Optimiser",
    tag: "Space"
  },
  {
    title: "RFTSystems Suite Collection",
    description:
      "Full RFTSystems collection on Hugging Face — all public Spaces in one place.",
    url: "https://hf.co/collections/RFTSystems/rftsystems-suite",
    tag: "Collection"
  }
];

// ZENODO DOIs — curated list (all others removed)
const zenodoDois = [
  {
    title: "Rendered Frame Theory: A Paradigm Shift in the Science of Reality",
    description:
      "Core RFT record laying out the paradigm shift in the science of reality.",
    url: "https://doi.org/10.5281/zenodo.15882865",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory: A Unified Field Framework for Cosmology, Quantum Mechanics, Consciousness, and Geometric Physics",
    description:
      "Unified field framework connecting cosmology, quantum mechanics, consciousness, and geometric physics under RFT.",
    url: "https://doi.org/10.5281/zenodo.17867668",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory: 50 Canonical Equations of Relativistic Consciousness",
    description:
      "Set of 50 canonical equations that define relativistic consciousness within RFT.",
    url: "https://doi.org/10.5281/zenodo.17829567",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory (RFT) — Adaptive Computing Kernel (v1.0): Verified Benchmark Record",
    description:
      "Adaptive Computing Kernel benchmark record — verified performance metrics and validation data.",
    url: "https://doi.org/10.5281/zenodo.17478289",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory (RFT) – Computational Validation as a Candidate Theory of Everything (TOE)",
    description:
      "Computational validation of RFT as a candidate Theory of Everything.",
    url: "https://doi.org/10.5281/zenodo.17372562",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory (RCQM)",
    description:
      "RCQM record consolidating the Rendered Frame Theory approach to consciousness and quantum mechanics.",
    url: "https://doi.org/10.5281/zenodo.17436739",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory (RFT) — Full Validation Series (Stages 1–12): From Baseline to Production Integration",
    description:
      "Full validation series, stages 1–12, documenting the path from baseline tests to production integration.",
    url: "https://doi.org/10.5281/zenodo.17443453",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory (RFT) — Master IP & Legal Consolidation (2023–2025)",
    description:
      "Master IP and legal consolidation record for RFT, covering 2023–2025.",
    url: "https://doi.org/10.5281/zenodo.17460107",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory (RFT-Ω-FrameNet v2): Conceptual Proof, Mathematical Basis, and Legal Record",
    description:
      "Ω-FrameNet v2 conceptual proof, associated mathematics, and legal record.",
    url: "https://doi.org/10.5281/zenodo.17464667",
    tag: "Zenodo"
  },
  {
    title: "RFT — Toy Harmonic Demonstrator (Colab): QΩ Stability & Pre-emptive Trigger Record",
    description:
      "Toy harmonic demonstrator in Colab for QΩ stability and pre-emptive trigger behaviour.",
    url: "https://doi.org/10.5281/zenodo.17466722",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory",
    description:
      "Rendered Frame Theory record providing a consolidated reference point for the model.",
    url: "https://doi.org/10.5281/zenodo.17297533",
    tag: "Zenodo"
  },
  {
    title: "Self Deriving Algebra Through Rendered Frame Theory",
    description:
      "Self-deriving algebra developed through RFT, co-authored with NexFrame AI.",
    url: "https://doi.org/10.5281/zenodo.17287252",
    tag: "Zenodo"
  }
];

// GITHUB REPOS — org spine
const githubRepos = [
  {
    title: "RenderedFrameTheory.github.io",
    description:
      "Official RFT website repository — books, DOIs, Spaces, and contact hub.",
    url: "https://github.com/RenderedFrameTheory/RenderedFrameTheory.github.io",
    tag: "GitHub"
  },
  {
    title: "RFT_UnifiedDeformation",
    description:
      "Minimal RFT testbed: 5-field deformation core for BAO, CMB peaks, rotation curves, and collapse rate.",
    url: "https://github.com/RenderedFrameTheory/RFT_UnifiedDeformation",
    tag: "GitHub"
  },
  {
    title: "Conscious-Universe",
    description:
      "Browser-based simulation of symbolic agents powered by Rendered Frame Theory.",
    url: "https://github.com/RenderedFrameTheory/Conscious-Universe",
    tag: "GitHub"
  },
  {
    title: "NexFrameRFT",
    description:
      "Distributed NexFrame AI implementation integrating RFT consciousness mathematics and external signals.",
    url: "https://github.com/RenderedFrameTheory/NexFrameRFT",
    tag: "GitHub"
  },
  {
    title: "RFTsystems",
    description:
      "Core scripts, tooling and infrastructure for the RFTSystems Hugging Face suite.",
    url: "https://github.com/RenderedFrameTheory/RFTsystems",
    tag: "GitHub"
  },
  {
    title: "minimal-self-awareness-demo",
    description:
      "Minimal Self agent in a 3×3 world — RFT consciousness simulation with Gradio interface.",
    url: "https://github.com/RenderedFrameTheory/minimal-self-awareness-demo",
    tag: "GitHub"
  }
];

// ------------------------------
//  Utility functions
// ------------------------------

function createCard(item) {
  const card = document.createElement("article");
  card.className = "card";

  const header = document.createElement("div");
  header.className = "card-header";

  const title = document.createElement("h4");
  title.textContent = item.title;

  const label = document.createElement("span");
  label.className = "card-label";
  label.textContent = item.tag || "Link";

  header.appendChild(title);
  header.appendChild(label);

  const desc = document.createElement("p");
  desc.textContent = item.description || "";

  const footer = document.createElement("div");
  footer.className = "card-footer";

  const link = document.createElement("a");
  link.href = item.url;
  link.target = "_blank";
  link.rel = "noopener noreferrer";
  link.textContent = "Open";

  const urlText = document.createElement("span");
  urlText.className = "card-tag";
  urlText.textContent = item.url.replace(/^https?:\/\//, "");

  footer.appendChild(link);
  footer.appendChild(urlText);

  card.appendChild(header);
  if (item.description) card.appendChild(desc);
  card.appendChild(footer);

  return card;
}

function renderList(containerId, items) {
  const container = document.getElementById(containerId);
  if (!container) return;
  container.innerHTML = "";
  items.forEach((item) => {
    container.appendChild(createCard(item));
  });
}

// ------------------------------
//  Mailto helpers
// ------------------------------

function openMailto(subject, body) {
  if (!RFT_CONTACT_EMAIL || RFT_CONTACT_EMAIL.includes("REPLACE_WITH_YOUR_EMAIL")) {
    alert("RFT_CONTACT_EMAIL is not configured in assets/main.js; contact forms cannot be used until this is set.");
    return false;
  }

  const mailto =
    "mailto:" +
    encodeURIComponent(RFT_CONTACT_EMAIL) +
    "?subject=" +
    encodeURIComponent(subject) +
    "&body=" +
    encodeURIComponent(body);

  window.location.href = mailto;
  return true;
}

// ------------------------------
//  Form handlers
// ------------------------------

function setupContactForm() {
  const form = document.getElementById("contact-form");
  const statusEl = document.getElementById("contact-status");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    statusEl.textContent = "";

    const data = new FormData(form);
    const name = (data.get("name") || "").toString().trim() || "Anonymous";
    const email = (data.get("email") || "").toString().trim();
    const topic = (data.get("topic") || "General feedback").toString();
    const message = (data.get("message") || "").toString().trim();

    if (!email) {
      statusEl.textContent = "Email is required so a reply can be sent.";
      statusEl.classList.add("error");
      return;
    }

    const subject = `RFT Feedback — ${topic}`;
    const bodyLines = [
      `From: ${name}`,
      `Reply email: ${email}`,
      `Topic: ${topic}`,
      "",
      "Message:",
      message || "(no message text provided)"
    ];

    const ok = openMailto(subject, bodyLines.join("\n"));
    if (ok) {
      statusEl.classList.remove("error");
      statusEl.textContent =
        "Email client should open with a draft containing the details. If it does not, the content can be copied and sent manually.";
    }
  });
}

function setupPartnershipForm() {
  const form = document.getElementById("partnership-form");
  const statusEl = document.getElementById("partnership-status");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    statusEl.textContent = "";

    const data = new FormData(form);
    const name = (data.get("name") || "").toString().trim();
    const email = (data.get("email") || "").toString().trim();
    const ptype = (data.get("ptype") || "Other").toString();
    const summary = (data.get("summary") || "").toString().trim();

    if (!name || !email) {
      statusEl.textContent = "Name/organisation and email are required.";
      statusEl.classList.add("error");
      return;
    }

    const subject = `RFT Partnership Proposal — ${ptype}`;
    const bodyLines = [
      `From: ${name}`,
      `Contact email: ${email}`,
      `Proposal type: ${ptype}`,
      "",
      "Summary:",
      summary || "(no summary text provided)"
    ];

    const ok = openMailto(subject, bodyLines.join("\n"));
    if (ok) {
      statusEl.classList.remove("error");
      statusEl.textContent =
        "Email client should open with a drafted proposal. Content can be reviewed and sent from there.";
    }
  });
}

function setupSupportForm() {
  const form = document.getElementById("support-form");
  const statusEl = document.getElementById("support-status");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    statusEl.textContent = "";

    const data = new FormData(form);
    const email = (data.get("email") || "").toString().trim();
    const stype = (data.get("stype") || "Where to start").toString();
    const details = (data.get("details") || "").toString().trim();

    if (!email) {
      statusEl.textContent = "Email is required.";
      statusEl.classList.add("error");
      return;
    }

    const subject = `RFT Support — ${stype}`;
    const bodyLines = [
      `Reply email: ${email}`,
      `Support type: ${stype}`,
      "",
      "Details:",
      details || "(no details provided)"
    ];

    const ok = openMailto(subject, bodyLines.join("\n"));
    if (ok) {
      statusEl.classList.remove("error");
      statusEl.textContent =
        "Email client should open with a drafted support request. Content can be reviewed and sent from there.";
    }
  });
}

// ------------------------------
//  Navigation toggle
// ------------------------------

function setupNavToggle() {
  const toggle = document.getElementById("nav-toggle");
  const menu = document.getElementById("nav-menu");
  if (!toggle || !menu) return;

  toggle.addEventListener("click", () => {
    menu.classList.toggle("open");
  });

  menu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      menu.classList.remove("open");
    });
  });
}

// ------------------------------
//  Stats + init
// ------------------------------

function updateStats() {
  const b = document.getElementById("stat-books");
  const s = document.getElementById("stat-spaces");
  const d = document.getElementById("stat-dois");
  const r = document.getElementById("stat-repos");

  if (b) b.textContent = books.length.toString();
  if (s) s.textContent = huggingfaceSpaces.length.toString();
  if (d) d.textContent = zenodoDois.length.toString();
  if (r) r.textContent = githubRepos.length.toString();
}

function setYear() {
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear().toString();
}

document.addEventListener("DOMContentLoaded", () => {
  renderList("books-list", books);
  renderList("spaces-list", huggingfaceSpaces);
  renderList("dois-list", zenodoDois);
  renderList("repos-list", githubRepos);

  setupContactForm();
  setupPartnershipForm();
  setupSupportForm();

  setupNavToggle();
  updateStats();
  setYear();
});
