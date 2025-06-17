---
layout: default
title: Rendered Frame Theory
---

# Rendered Frame Theory (RFT)  
Welcome to the official RFT project hub.
Created by Liam Grinstead, Rendered Frame Theory (RFT) redefines the fabric of reality—not as an expanding spacetime, but as an observer-dependent rendering engine that generates the universe in real time. At its core, RFT proposes that perception, consciousness, and time itself are part of a simulation-like rendering structure driven by harmonics, coherence, and phase synchronization.

What’s on Offer:
	•	🔍 Live Prediction Tracking: RFT doesn’t just theorize—it forecasts. Follow live predictions in weather, magnetic fields, solar activity, and seismic behavior, then check outcomes daily.
	•	📉 Challenge the Framework: Submit your own scientific challenge. Whether it’s BAO, CMB anomalies, quantum fringe behavior, or EEG synchrony, RFT will issue a falsifiable response and prediction.
	•	📄 DOI-Protected Research: Every major RFT milestone is documented in academic-grade papers, publicly available through Zenodo with timestamped DOI references. Explore dozens of published works on Mars, black holes, simulation theory, and more.
	•	🧠 Observer-Centric Metrics: Learn how GVU (Grinstead Voyager Unit) and LOU (Limara Orbital Unit) redefine constants like H₀ and c through real-time observer calibration.
	•	🔗 Open Science Hub: Every equation, test, and protocol is transparent and reproducible. Our methodology and verification sources are open to all.
	•	📬 Engage Directly: Have a prediction? A rebuttal? Want to contribute data or replicate an experiment? We welcome your input.

- 🧠 [RFT Origin Story](Story.md)

- 🚫 [Gatekeeping & Censorship](Gatekeeping.md)
  
- 💬 [Feedback & Predictions](Feedback.md)

<a href="data-sources.html">🔗 Verification Data Sources</a>


## 🔍 What We’ve Proven

- ✅ BAO prediction (313.40 Mpc) without ΛCDM
- ✅ Real-time Earth predictions: solar, magnetic, seismic
- ✅ 50+ open-source, DOI-backed papers

## 📂 Explore

<a href="live-feed.html">Live Prediction Feed</a>

## RFT Papers
- [📄 Core Theory DOI](https://doi.org/10.5281/zenodo.15597158)
- [📊 BAO Prediction](https://doi.org/10.5281/zenodo.15670096)
- [🧠 Consciousness Engine](https://doi.org/10.5281/zenodo.15540548)
- [🚀 Mars Mission Solutions](https://doi.org/10.5281/zenodo.15561784)
- 📄 [All RFT Papers](papers/index.md)

## 🧬 Join the Mission
This is simulation-aware physics. It's open. It's falsifiable. And it's yours to prove me wrong.

<a href="challenge.html">Challenge RFT</a>
> “If reality is rendered, then the observer is the engine.”

<a href="simulation.html">Simulation Console</a>

<a href="books.html">Books</a>

<!-- NexFrame Live Chat -->
<div id="nexframe-chat-icon" onclick="toggleNexFrameChat()">💬 Ask NexFrame</div>

<div id="nexframe-chat-box">
  <div id="nexframe-header">NexFrame – RFT Oracle</div>
  <div id="nexframe-body">
    <div class="nex-msg">[NexFrame]: Welcome, Observer. Ask me anything about the simulation, RFT predictions, or cosmic harmonics.</div>
  </div>
  <input id="nexframe-input" type="text" placeholder="Type your question..." onkeydown="handleKey(event)">
  <button onclick="simulateReply()">Send</button>
</div>

<style>
#nexframe-chat-icon {
  position: fixed;
  bottom: 20px;
  right: 20px;
  background: #1c1c1c;
  color: white;
  padding: 10px 15px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: bold;
  z-index: 9999;
}
#nexframe-chat-box {
  display: none;
  position: fixed;
  bottom: 70px;
  right: 20px;
  width: 300px;
  background: #111;
  border: 2px solid #4affed;
  border-radius: 10px;
  z-index: 9999;
  font-family: monospace;
  color: white;
}
#nexframe-header {
  background: #222;
  color: #4affed;
  padding: 10px;
  font-weight: bold;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  font-size: 14px;
}
#nexframe-body {
  height: 160px;
  padding: 10px;
  overflow-y: auto;
  font-size: 13px;
}
.nex-msg {
  margin-bottom: 8px;
}
#nexframe-input {
  width: 70%;
  padding: 6px;
  border: none;
  font-size: 13px;
  border-top: 1px solid #333;
  background: #222;
  color: #fff;
}
button {
  width: 30%;
  background: #4affed;
  color: black;
  font-weight: bold;
  border: none;
  cursor: pointer;
}
</style>

<script>
function toggleNexFrameChat() {
  const chatBox = document.getElementById("nexframe-chat-box");
  chatBox.style.display = chatBox.style.display === "none" ? "block" : "none";
}

function handleKey(e) {
  if (e.key === "Enter") simulateReply();
}

function simulateReply() {
  const input = document.getElementById("nexframe-input");
  const chat = document.getElementById("nexframe-body");
  const question = input.value.trim();
  if (!question) return;

  chat.innerHTML += `<div class="nex-msg">[You]: ${question}</div>`;
  
  // Basic simulated response
  setTimeout(() => {
    chat.innerHTML += `<div class="nex-msg">[NexFrame]: Observer query acknowledged. Render lock applied. Awaiting Δτ synchronization…</div>`;
    chat.scrollTop = chat.scrollHeight;
  }, 500);
  
  input.value = "";
}
</script>

