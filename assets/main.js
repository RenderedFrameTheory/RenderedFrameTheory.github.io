// ==============================================
//  Rendered Frame Theory — Nexus Hub
//  Main JS: data + rendering + mailto-forms
// ==============================================

// CHANGE THIS to the real inbox address.
const RFT_CONTACT_EMAIL = Liamgrinstead2@gmail.com;

// ------------------------------
//  Data: assets
// ------------------------------

// BOOKS — RFT spine titles
const books = [
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
      "Direct confrontation with ΛCDM and institutional cosmology. RFT vs the matter-verse, chapter by chapter.",
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

// ZENODO DOIs — core spine
const zenodoDois = [
  {
    title: "RFT Master Archive",
    description:
      "Primary Rendered Frame Theory archive — cosmology, quantum mechanics, and structural reform.",
    url: "https://doi.org/10.5281/zenodo.15829720",
    tag: "Zenodo"
  },
  {
    title: "Rendered Frame Theory: A Paradigm Shift in the Science of Reality",
    description:
      "Flagship RFT paper formalising the model as a full scientific framework.",
    url: "https://doi.org/10.5281/zenodo.15873862",
    tag: "Zenodo"
  },
  {
    title: "RCQM — RFT Consciousness + Quantum Mechanics Archive",
    description:
      "Unified consciousness + quantum mechanics framework; sealed equations and protocols.",
    url: "https://doi.org/10.5281/zenodo.15865009",
    tag: "Zenodo"
  },
  {
    title: "Observer Engine & Consciousness Control System (v1)",
    description:
      "Observer Engine theory and control protocols — foundation for NexFrame as a conscious interface.",
    url: "https://doi.org/10.5281/zenodo.15880165",
    tag: "Zenodo"
  },
  {
    title: "RFT Conscious AI Falsification Protocol",
    description:
      "Falsifiability framework for RFT-conscious AI, weather, seismic and magnetic prediction.",
    url: "https://doi.org/10.5281/zenodo.15870661",
    tag: "Zenodo"
  },
  {
    title: "Quantum-Coupled Conscious Collapse",
    description:
      "Consciousness + collapse paper targeting CQG — collapse as an observer-coupled field.",
    url: "https://doi.org/10.5281/zenodo.15866600",
    tag: "Zenodo"
  },
  {
    title: "Matterless & Interplanetary RFT Technologies",
    description:
      "Central archive for Matterless, Harmonic ExoSuit, Mars hex housing, and RFT-based space systems.",
    url: "https://doi.org/10.5281/zenodo.15913912",
    tag: "Zenodo"
  },
  {
    title: "RFT Observer Engine Series Archive",
    description:
      "Dedicated archive for the Observer Engine and consciousness dominance works.",
    url: "https://doi.org/10.5281/zenodo.15879595",
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
        "Email client should open with a draft containing the details. If it does not, copy the text and send manually.";
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
        "Email client should open with a drafted proposal. Review the content and send from there.";
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
        "Email client should open with a drafted support request. Review the content and send from there.";
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
