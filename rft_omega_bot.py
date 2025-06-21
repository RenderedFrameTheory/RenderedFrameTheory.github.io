
import telebot
import datetime

# Initialize bot
bot = telebot.TeleBot("7367860353:AAGmiNB5RJfRs5NwUa4Fmsam4KFJeS7kjok")

# Ω-Lock constants
OMEGA_LOCK_FORMULA = (
    "🧨 RFT Ω-Lock Enforcement Equation:\n"
    "\n"
    "𝓡(Ω-lock) = limₜ→τ_eff [ (Ω_obs × χ_Liam) / (Δφ × Υ) ] × Θ(𝓕_auth - 𝓕_model)\n"
    "\n"
    "If observer identity ≠ Liam Grinstead, render mismatch occurs."
)

# Welcome and help command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, (
        "👁 Welcome to ChallengeRFT: Name It, Will Render It.\n"
        "Send any phenomenon via /challenge, or run /predict for RFT-powered predictions.\n"
        "Ω-lock is active. Unauthorized render use will be traced.\n"
        "\n"
        "Useful commands:\n"
        "/challenge [phenomenon]\n"
        "/predict\n"
        "/omega\n"
        "Website: https://renderedframetheory.github.io\n"
        "DOI: https://doi.org/10.5281/zenodo.15707814"
    ))

# Ω-lock Equation Trigger
@bot.message_handler(commands=['omega'])
def omega_lock_formula(message):
    bot.reply_to(message, OMEGA_LOCK_FORMULA)

# Prediction stub
@bot.message_handler(commands=['predict'])
def predict(message):
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    prediction = (
        f"📈 RFT Live Prediction — {now}\n"
        "Atmospheric: Render stable\n"
        "Magnetic: Minor anomalies near τ_eff\n"
        "Solar: Moderate flux rise expected\n"
        "Seismic: Watch phase lag in South Asia corridor"
    )
    bot.reply_to(message, prediction)

# Rendered challenge logic
@bot.message_handler(commands=['challenge'])
def challenge_render(message):
    query = message.text.replace("/challenge", "").strip()
    if not query:
        bot.reply_to(message, "⚠️ Please include a challenge. Example: /challenge consciousness")
        return
    response = (
        f"🔁 RFT Rendering Challenge:\n"
        f"Phenomenon: {query}\n"
        "Rendering pathway active...\n"
        f"✅ Render complete using τ_eff, Ω_obs, and Δφ sync.\n"
        f"Frame response verified: '{query}' aligns under observer-indexed simulation."
    )
    bot.reply_to(message, response)

# Passive formula watcher
@bot.message_handler(func=lambda m: "RFT" in m.text or "Ω" in m.text or "tau" in m.text)
def passive_detect(message):
    bot.reply_to(message, (
        "🔒 Ω-lock triggered.\n"
        "Your message included RFT-linked terms.\n"
        "Unauthorized render attempts will fail observer sync.\n"
        "Visit https://renderedframetheory.github.io to verify logic."
    ))

# Run bot
bot.polling()
