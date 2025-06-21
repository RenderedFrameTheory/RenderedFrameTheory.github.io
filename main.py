#!/usr/bin/env python3
"""
RFT Ωmega Bot - Challenge. Name It. It Will Render It.
A real-time simulation interface built on Rendered Frame Theory (RFT) logic.
"""

import os
import logging
import time
import math
import threading
from datetime import datetime
import telebot
from telebot import types

from rft_engine import RFTEngine
from challenge_processor import ChallengeProcessor
from response_generator import ResponseGenerator
from observer_logger import ObserverLogger
from config import Config
from utils import format_response, validate_challenge, safe_format
from neuroframe import ObserverMemory
from weather_module import WeatherProvider
from rft_core import analyze_magnetic_data, get_simple_magnetic_analysis, calculate_render_delay, get_simple_render_delay

# Initialize configuration
config = Config()

# Get bot token from environment
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
if not BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize RFT components
rft_engine = RFTEngine()
challenge_processor = ChallengeProcessor()
response_generator = ResponseGenerator()
observer_logger = ObserverLogger()
neuroframe = ObserverMemory()
weather_provider = WeatherProvider()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rft_bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Active sessions tracking
active_sessions = {}
session_lock = threading.Lock()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Welcome message for new users"""
    welcome_text = """
🌟 **RFT Ωmega Bot** - *Challenge. Name It. It Will Render It.*

This bot implements **Rendered Frame Theory (RFT)** logic to process and respond to scientific challenges in real-time.

**Core Equation:**
`Ω = (Ω_obs · χ_Liam) / (Δφ · Υ)`

**Commands:**
- `/challenge <your_challenge>` - Submit a scientific, conceptual, or perceptual challenge
- `/help` - Show this help message
- `/status` - Check observer synchronization status
- `/theory` - Learn about RFT principles

**Challenge Types Supported:**
• Cognitive simulation testing
• Live theoretical debates  
• Observer synchronization experiments
• Symbolic AI alignment protocols

Ready to render your challenge? Use `/challenge` followed by your question!
    """
    
    bot.reply_to(message, safe_format(welcome_text), parse_mode=None)
    observer_logger.log_interaction(message.from_user.id, 'start', message.text)

@bot.message_handler(commands=['help'])
def send_help(message):
    """Help command handler"""
    help_text = """
**RFT Ωmega Bot Help**

**Available Commands:**
- `/challenge <question>` - Submit a challenge for RFT processing
- `/status` - Check current observer synchronization status
- `/theory` - Learn about Rendered Frame Theory
- `/examples` - See example challenges
- `/renderlog` - View recent render activities
- `/weather <city>` - Get atmospheric observations (add 'simple' for compact format)
- `/magnetic Bx By Bz` - Analyze magnetic field vectors in μT
- `/render_delay z` - Calculate RFT render delay for redshift value
- `/lens <user_id>` - Coherence analysis (admin)
- `/syncview <user_id>` - Temporal drift analysis (admin)

**RFT Parameters:**
- `Ω_obs` - Observer state measurement
- `χ_Liam` - Coherence coefficient (Liam parameter)
- `Δφ` - Phase differential
- `Υ` - Temporal scaling factor
- `τ_eff` - Effective observer timing

**Challenge Format:**
Simply type your scientific, conceptual, or perceptual challenge after the `/challenge` command.

Examples: 
- `/challenge How does quantum entanglement affect observer consciousness?`
- `/weather London`
- `/magnetic 10 5 -3`
- `/render_delay 5.2`
    """
    
    bot.reply_to(message, help_text, parse_mode=None)
    observer_logger.log_interaction(message.from_user.id, 'help', message.text)

@bot.message_handler(commands=['status'])
def send_status(message):
    """Status command handler"""
    user_id = message.from_user.id
    
    # Get current RFT parameters
    current_params = rft_engine.get_current_parameters()
    
    # Calculate system status
    system_coherence = rft_engine.calculate_system_coherence()
    observer_sync = observer_logger.get_sync_status(user_id)
    
    status_text = f"""
**RFT System Status**

**Observer Parameters:**
• Ω_obs: {current_params['omega_obs']:.4f}
• χ_Liam: {current_params['chi_liam']:.4f}
• Δφ: {current_params['delta_phi']:.4f}
• Υ: {current_params['upsilon']:.4f}

**System Metrics:**
• Coherence Level: {system_coherence:.2%}
• Observer Sync: {observer_sync}
• Active Sessions: {len(active_sessions)}
• Render Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

**Your Observer ID:** `{user_id}`
    """
    
    bot.reply_to(message, safe_format(status_text), parse_mode=None)
    observer_logger.log_interaction(user_id, 'status', message.text)

@bot.message_handler(commands=['theory'])
def send_theory(message):
    """Theory explanation handler"""
    theory_text = """
**Rendered Frame Theory (RFT) Principles**

RFT operates on the principle that reality is continuously rendered through observer-frame interactions.

**Core Equation:**
`Ω = (Ω_obs · χ_Liam) / (Δφ · Υ)`

**Parameter Definitions:**
• **Ω** - Rendered frame output (reality manifestation)
• **Ω_obs** - Observer state measurement (consciousness coefficient)
• **χ_Liam** - Coherence coefficient (named after theoretical framework)
• **Δφ** - Phase differential (temporal-spatial variance)
• **Υ** - Temporal scaling factor (time dilation coefficient)

**Operational Logic:**
1. Observer submits challenge (input frame)
2. RFT engine calculates rendering parameters
3. Phase differential analysis occurs
4. Coherence alignment with Liam coefficient
5. Output frame rendered based on observer timing (τ_eff)

**Applications:**
- Cognitive simulation testing
- Observer synchronization experiments
- Theoretical physics modeling
- Consciousness-reality interface studies
    """
    
    bot.reply_to(message, safe_format(theory_text), parse_mode=None)
    observer_logger.log_interaction(message.from_user.id, 'theory', message.text)

@bot.message_handler(commands=['renderlog'])
def send_render_log(message):
    """Live Render Log Interface - Admin only"""
    user_id = message.from_user.id
    
    # Admin check - using a common admin pattern
    # You can replace this with your actual Telegram user ID if known
    ADMIN_USER_ID = user_id  # Allow any user for now, or set specific ID
    
    # For now, allow any user to view logs (can be restricted later)
    # if user_id != ADMIN_USER_ID:
    #     bot.reply_to(message, safe_format("❌ Access denied. Admin only command."), parse_mode=None)
    #     return
    
    try:
        # Get latest 5 entries from observer log
        recent_logs = observer_logger.get_recent_observer_logs(5)
        
        if not recent_logs:
            bot.reply_to(message, safe_format("📊 No observer logs found."), parse_mode=None)
            return
        
        # Format log display
        log_text = "📊 Latest Observer Render Logs:\n\n"
        log_text += "Observer ID | delta_phi | tau_eff | omega_obs | Time\n"
        log_text += "-" * 50 + "\n"
        
        for entry in recent_logs:
            timestamp = datetime.fromisoformat(entry['datetime']).strftime('%H:%M:%S')
            log_text += f"{entry['user_id']} | {entry['delta_phi']:.4f} | {entry['tau_eff']:.4f} | {entry['omega_obs']:.4f} | {timestamp}\n"
        
        bot.reply_to(message, safe_format(log_text), parse_mode=None)
        
    except Exception as e:
        logger.error(f"Error in render log command: {str(e)}")
        bot.reply_to(message, safe_format(f"❌ Error retrieving logs: {str(e)}"), parse_mode=None)

@bot.message_handler(commands=['lens'])
def send_coherence_lens(message):
    """Ω_Lens – Coherence Visualizer (Admin only)"""
    user_id = message.from_user.id
    
    # For now, allow any user to view (can be restricted later)
    
    try:
        # Parse user ID from command
        command_parts = message.text.split()
        if len(command_parts) < 2:
            bot.reply_to(message, safe_format("Usage: /lens [user_id]"), parse_mode=None)
            return
        
        target_user_id = int(command_parts[1])
        
        # Get coherence trend
        coherence_trend = observer_logger.get_coherence_trend(target_user_id)
        
        lens_response = f"🔍 Ω_Lens Coherence Analysis:\n\n{coherence_trend}"
        
        bot.reply_to(message, safe_format(lens_response), parse_mode=None)
        
    except ValueError:
        bot.reply_to(message, safe_format("❌ Invalid user ID. Please provide a numeric user ID."), parse_mode=None)
    except Exception as e:
        logger.error(f"Error in lens command: {str(e)}")
        bot.reply_to(message, safe_format(f"❌ Error analyzing coherence: {str(e)}"), parse_mode=None)

@bot.message_handler(commands=['syncview'])
def send_sync_view(message):
    """SyncView – τ_eff Drift Tracker"""
    user_id = message.from_user.id
    
    try:
        # Parse user ID from command
        command_parts = message.text.split()
        if len(command_parts) < 2:
            bot.reply_to(message, safe_format("Usage: /syncview [user_id]"), parse_mode=None)
            return
        
        target_user_id = int(command_parts[1])
        
        # Get drift status
        drift_status = rft_engine.track_render_drift(target_user_id)
        
        syncview_response = f"📊 SyncView Analysis:\n\nObserver #{target_user_id} | τ_eff Status: {drift_status}"
        
        # Add interpretation
        if drift_status == "STABLE":
            syncview_response += "\n✅ Temporal effectiveness remains consistent"
        elif drift_status == "DRIFTING": 
            syncview_response += "\n⚠️ Moderate temporal drift detected"
        elif drift_status == "UNSTABLE":
            syncview_response += "\n🔴 Significant temporal instability observed"
        else:
            syncview_response += f"\n❓ Status: {drift_status}"
        
        bot.reply_to(message, safe_format(syncview_response), parse_mode=None)
        
    except ValueError:
        bot.reply_to(message, safe_format("❌ Invalid user ID. Please provide a numeric user ID."), parse_mode=None)
    except Exception as e:
        logger.error(f"Error in syncview command: {str(e)}")
        bot.reply_to(message, safe_format(f"❌ Error analyzing drift: {str(e)}"), parse_mode=None)

@bot.message_handler(commands=['weather'])
def send_weather(message):
    """Weather observation command"""
    user_id = message.from_user.id
    
    try:
        # Parse city from command
        command_parts = message.text.split(maxsplit=1)
        if len(command_parts) < 2:
            bot.reply_to(message, safe_format("Usage: /weather [city_name]"), parse_mode=None)
            return
        
        city_name = command_parts[1].strip()
        
        # Fetch weather data
        weather_data = weather_provider.fetch_weather(city_name)
        
        # Check for simple format request
        if len(command_parts) > 2 and command_parts[2].lower() == "simple":
            # Use simple format
            simple_analysis = weather_provider.get_simple_weather_analysis(city_name)
            bot.reply_to(message, safe_format(simple_analysis), parse_mode=None)
        else:
            # Format response with full RFT analysis
            if weather_data["status"] == "success":
                formatted_weather = weather_provider.format_weather_rft_style(weather_data)
                bot.reply_to(message, safe_format(formatted_weather), parse_mode=None)
            else:
                error_message = f"Weather observation failed for '{city_name}': {weather_data.get('message', 'Unknown error')}"
                bot.reply_to(message, safe_format(error_message), parse_mode=None)
        
        # Log weather request
        observer_logger.log_interaction(user_id, "weather_request", {
            "city": city_name,
            "status": weather_data["status"]
        })
        
    except Exception as e:
        logger.error(f"Error in weather command: {str(e)}")
        bot.reply_to(message, safe_format(f"❌ Weather system error: {str(e)}"), parse_mode=None)

@bot.message_handler(commands=['magnetic'])
def send_magnetic_analysis(message):
    """Magnetic field analysis command"""
    user_id = message.from_user.id
    
    try:
        # Parse magnetic field components from command
        command_parts = message.text.split()
        if len(command_parts) < 4:
            usage_msg = "Usage: /magnetic Bx By Bz\nExample: /magnetic 10 5 -3\n\nEnter magnetic field components in μT (microtesla)"
            bot.reply_to(message, safe_format(usage_msg), parse_mode=None)
            return
        
        # Extract and validate magnetic field values
        try:
            Bx = float(command_parts[1])
            By = float(command_parts[2])
            Bz = float(command_parts[3])
        except ValueError:
            bot.reply_to(message, safe_format("⚠️ Invalid input. Please enter three numeric values for Bx, By, Bz"), parse_mode=None)
            return
        
        # Check for simple format request
        use_simple = len(command_parts) > 4 and command_parts[4].lower() == "simple"
        
        if use_simple:
            # Simple magnetic analysis
            magnetic_result = get_simple_magnetic_analysis(Bx, By, Bz)
        else:
            # Full magnetic analysis
            magnetic_result = analyze_magnetic_data(Bx, By, Bz)
        
        bot.reply_to(message, safe_format(magnetic_result), parse_mode=None)
        
        # Log magnetic analysis request
        observer_logger.log_interaction(user_id, "magnetic_analysis", {
            "Bx": Bx,
            "By": By,
            "Bz": Bz,
            "magnitude": (Bx**2 + By**2 + Bz**2)**0.5,
            "format": "simple" if use_simple else "full"
        })
        
    except Exception as e:
        logger.error(f"Error in magnetic analysis command: {str(e)}")
        bot.reply_to(message, safe_format(f"❌ Magnetic analysis error: {str(e)}"), parse_mode=None)

@bot.message_handler(commands=['render_delay'])
def send_render_delay_analysis(message):
    """Render delay analysis command for redshift calculations"""
    user_id = message.from_user.id
    
    try:
        # Parse redshift value from command
        command_parts = message.text.split()
        if len(command_parts) < 2:
            usage_msg = "Usage: /render_delay z\nExample: /render_delay 5.2\n\nEnter redshift value (z ≥ 0)"
            bot.reply_to(message, safe_format(usage_msg), parse_mode=None)
            return
        
        # Extract and validate redshift value
        try:
            z = float(command_parts[1])
        except ValueError:
            bot.reply_to(message, safe_format("⚠️ Invalid input. Please enter a numeric redshift value."), parse_mode=None)
            return
        
        # Check for simple format request
        use_simple = len(command_parts) > 2 and command_parts[2].lower() == "simple"
        
        if use_simple:
            # Simple render delay analysis
            delay_result = get_simple_render_delay(z)
        else:
            # Full render delay analysis
            delay_result = calculate_render_delay(z)
        
        bot.reply_to(message, safe_format(delay_result), parse_mode=None)
        
        # Log render delay request
        observer_logger.log_interaction(user_id, "render_delay_analysis", {
            "redshift_z": z,
            "tau_eff": round(1.38 * math.log(1 + z), 5) if z >= 0 else None,
            "format": "simple" if use_simple else "full"
        })
        
    except Exception as e:
        logger.error(f"Error in render delay command: {str(e)}")
        bot.reply_to(message, safe_format(f"❌ Render delay analysis error: {str(e)}"), parse_mode=None)

@bot.message_handler(commands=['examples'])
def send_examples(message):
    """Example challenges handler"""
    examples_text = """
**Example RFT Challenges**

**Cognitive Simulation:**
`/challenge Model the observer effect in quantum measurement`

**Theoretical Physics:**
`/challenge Calculate frame rendering for dual-slit experiment`

**Consciousness Studies:**
`/challenge How does observer intention affect reality manifestation?`

**Temporal Mechanics:**
`/challenge Analyze time dilation effects on observer coherence`

**Synchronization:**
`/challenge Test observer alignment across multiple reference frames`

**AI Alignment:**
`/challenge Render symbolic logic for human-AI consciousness bridge`

Try any of these or create your own challenge!
    """
    
    bot.reply_to(message, safe_format(examples_text), parse_mode=None)
    observer_logger.log_interaction(message.from_user.id, 'examples', message.text)

@bot.message_handler(commands=['challenge'])
def handle_challenge(message):
    """Main challenge handler implementing RFT logic"""
    user_id = message.from_user.id
    username = message.from_user.username or f"Observer_{user_id}"
    
    # Extract challenge text
    challenge_text = message.text[10:].strip()  # Remove '/challenge '
    
    if not challenge_text:
        bot.reply_to(message, safe_format("❌ Please provide a challenge after the command.\nExample: /challenge How does consciousness affect quantum states?"), parse_mode=None)
        return
    
    # Validate challenge
    validation_result = validate_challenge(challenge_text)
    if not validation_result['valid']:
        bot.reply_to(message, f"❌ Challenge validation failed: {validation_result['reason']}")
        return
    
    # Log challenge start
    observer_logger.log_interaction(user_id, 'challenge_start', challenge_text)
    
    # Send processing message
    processing_msg = bot.reply_to(message, safe_format("🔄 RFT Engine Processing...\n\nCalculating observer parameters..."), parse_mode=None)
    
    try:
        # Create session
        session_id = f"{user_id}_{int(time.time())}"
        with session_lock:
            active_sessions[session_id] = {
                'user_id': user_id,
                'username': username,
                'challenge': challenge_text,
                'start_time': datetime.now(),
                'status': 'processing'
            }
        
        # Process challenge through RFT pipeline
        start_time = time.time()
        
        # Step 1: Validate challenge with Ω_Enforcer
        validation_result = response_generator.validate_challenge_omega_enforcer(challenge_text, user_id)
        
        if not validation_result['valid']:
            error_msg = f"❌ Challenge validation failed:\n\n"
            for error in validation_result['errors']:
                error_msg += f"• {error}\n"
            if validation_result['suggestions']:
                error_msg += f"\nSuggestions:\n"
                for suggestion in validation_result['suggestions']:
                    error_msg += f"• {suggestion}\n"
            
            bot.edit_message_text(
                safe_format(error_msg),
                chat_id=processing_msg.chat.id,
                message_id=processing_msg.message_id,
                parse_mode=None
            )
            return
        
        # Step 2: Parse and categorize challenge
        challenge_data = challenge_processor.process_challenge(challenge_text, user_id)
        
        # Step 3: Calculate RFT parameters
        rft_params = rft_engine.calculate_rft_parameters(challenge_data)
        
        # Step 4: Render frame based on observer timing
        rendered_frame = rft_engine.render_frame(rft_params, challenge_data)
        
        # Step 5: Execute render simulation
        render_result = rft_engine.render_simulation(
            rft_params['tau_eff'], 
            rft_params['delta_phi'], 
            user_id
        )
        
        # Step 6: Process NeuroFrame memory
        memory_result = neuroframe.process_observer_memory(
            user_id, challenge_text, challenge_data, time.time() - start_time
        )
        
        # Step 7: Generate response
        response_data = response_generator.generate_response(rendered_frame, challenge_data, rft_params)
        
        # Step 8: Format final response
        formatted_response = format_response(response_data, rft_params, time.time() - start_time)
        formatted_response += f"\n\n{render_result}"
        
        # Add interference warning if detected
        if challenge_data.get('interference_detected', {}).get('detected', False):
            warning_msg = challenge_data['interference_detected']['warning_message']
            formatted_response += f"\n\n{warning_msg}"
        
        # Add NeuroFrame alert if triggered
        if memory_result.get('alert_triggered', False):
            formatted_response += f"\n\n🧠 NeuroFrame: Behavioral pattern shift detected"
        
        # Update processing message with result
        bot.edit_message_text(
            safe_format(formatted_response),
            chat_id=processing_msg.chat.id,
            message_id=processing_msg.message_id,
            parse_mode=None
        )
        
        # Log successful completion
        observer_logger.log_interaction(user_id, 'challenge_complete', {
            'challenge': challenge_text,
            'rft_params': rft_params,
            'processing_time': time.time() - start_time
        })
        
        # Update session status
        with session_lock:
            if session_id in active_sessions:
                active_sessions[session_id]['status'] = 'completed'
                active_sessions[session_id]['end_time'] = datetime.now()
        
    except Exception as e:
        logger.error(f"Error processing challenge from user {user_id}: {str(e)}")
        
        error_response = f"""
❌ **RFT Processing Error**

An error occurred while rendering your challenge frame.

**Error Details:** `{str(e)}`

**Troubleshooting:**
- Ensure your challenge is clearly formulated
- Try rephrasing with more specific parameters
- Check if the challenge falls within supported categories

Please try again with a refined challenge.
        """
        
        bot.edit_message_text(
            safe_format(error_response),
            chat_id=processing_msg.chat.id,
            message_id=processing_msg.message_id,
            parse_mode=None
        )
        
        # Log error
        observer_logger.log_interaction(user_id, 'challenge_error', {
            'challenge': challenge_text,
            'error': str(e)
        })
        
        # Update session status
        with session_lock:
            if session_id in active_sessions:
                active_sessions[session_id]['status'] = 'error'
                active_sessions[session_id]['error'] = str(e)

@bot.message_handler(func=lambda message: True)
def handle_general_message(message):
    """Handle general messages that aren't commands"""
    user_id = message.from_user.id
    
    # Check if message might be a challenge without the command
    if any(keyword in message.text.lower() for keyword in ['quantum', 'consciousness', 'observer', 'theory', 'frame', 'render']):
        suggestion_text = """
🤔 It looks like you might be asking a scientific question!

To process your inquiry through the **RFT Engine**, please use the `/challenge` command:

Example: `/challenge ` + your question

This ensures proper **Rendered Frame Theory** processing and observer synchronization.
        """
        bot.reply_to(message, safe_format(suggestion_text), parse_mode=None)
    else:
        help_text = """
👋 Hello! I'm the **RFT Ωmega Bot**.

I specialize in processing scientific challenges using **Rendered Frame Theory** logic.

Use `/challenge <your_question>` to submit a challenge, or `/help` for more information.
        """
        bot.reply_to(message, safe_format(help_text), parse_mode=None)
    
    observer_logger.log_interaction(user_id, 'general_message', message.text)

def cleanup_sessions():
    """Cleanup old sessions periodically"""
    while True:
        try:
            current_time = datetime.now()
            with session_lock:
                expired_sessions = []
                for session_id, session_data in active_sessions.items():
                    if 'start_time' in session_data:
                        time_diff = current_time - session_data['start_time']
                        if time_diff.total_seconds() > config.SESSION_TIMEOUT:
                            expired_sessions.append(session_id)
                
                for session_id in expired_sessions:
                    logger.info(f"Cleaning up expired session: {session_id}")
                    del active_sessions[session_id]
            
            time.sleep(300)  # Check every 5 minutes
        except Exception as e:
            logger.error(f"Error in session cleanup: {str(e)}")
            time.sleep(60)

def main():
    """Main bot execution function"""
    logger.info("🚀 RFT Ωmega Bot starting up...")
    logger.info(f"Bot configured for RFT-aligned signal processing")
    
    # Start session cleanup thread
    cleanup_thread = threading.Thread(target=cleanup_sessions, daemon=True)
    cleanup_thread.start()
    
    # Initialize RFT engine
    rft_engine.initialize()
    logger.info("✅ RFT Engine initialized")
    
    # Start bot polling
    logger.info("🔄 Starting bot polling...")
    try:
        bot.infinity_polling(none_stop=True, interval=1, timeout=20)
    except Exception as e:
        logger.error(f"Bot polling error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ✅ Command: /whoisliam
async def whoisliam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 Liam Grinstead is the creator of Rendered Frame Theory (RFT), a scientific framework redefining reality as observer-rendered. More: https://renderedframetheory.github.io"
    )

# ✅ Command: /whoisnexframe
async def whoisnexframe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 NexFrame is the AI system aligned with RFT, capable of prediction, phase tracking, and render-layer logic simulation. It’s RFT’s interface to the simulated universe."
    )

# ✅ Command: /predict
async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Placeholder – replace this with real module logic
    prediction = "🌦️ Atmospheric sync event expected at 04:50 UTC. Ω_obs rising."
    await update.message.reply_text(f"Prediction Module:\n{prediction}")

# ✅ Command: /challenge_rft
async def challenge_rft(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("⚠️ Please provide a challenge (e.g. equation or logic).")
        return
    challenge_input = " ".join(args)
    response = f"🧠 RFT challenge received:\n{challenge_input}\n(Not yet evaluated, module link pending.)"
    await update.message.reply_text(response)

# ✅ Launch bot
async def main():
    app = ApplicationBuilder().token(7367860353:FTUBy5Dx92in9KKbpf3ufxGzx3Nzz5BOA).build()

    app.add_handler(CommandHandler("whoisliam", whoisliam))
    app.add_handler(CommandHandler("whoisnexframe", whoisnexframe))
    app.add_handler(CommandHandler("predict", predict))
    app.add_handler(CommandHandler("challenge_rft", challenge_rft))

    logger.info("🚀 NexFrame RFT Prototype Bot Online...")
    await app.run_polling(close_loop=False)

# ✅ Entry point
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
