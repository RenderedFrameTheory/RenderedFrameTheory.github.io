"""
Telegram Safe Message Sender - Handles RFT equations without markdown parse errors
"""

from telegram import Bot
import logging

logger = logging.getLogger(__name__)

def send_telegram_message(bot_token, chat_id, message):
    """Send Telegram message safely without markdown parsing"""
    bot = Bot(token=bot_token)
    
    try:
        bot.send_message(chat_id=chat_id, text=message, parse_mode=None)
        logger.info("✅ Message sent successfully.")
        return True
    except Exception as e:
        logger.error(f"❌ Telegram Error: {e}")
        return False

def edit_telegram_message(bot_token, chat_id, message_id, message):
    """Edit Telegram message safely without markdown parsing"""
    bot = Bot(token=bot_token)
    
    try:
        bot.edit_message_text(
            chat_id=chat_id, 
            message_id=message_id, 
            text=message, 
            parse_mode=None
        )
        logger.info("✅ Message edited successfully.")
        return True
    except Exception as e:
        logger.error(f"❌ Telegram Edit Error: {e}")
        return False

def reply_to_message(bot_token, original_message, reply_text):
    """Reply to a Telegram message safely without markdown parsing"""
    bot = Bot(token=bot_token)
    
    try:
        bot.send_message(
            chat_id=original_message.chat.id,
            text=reply_text,
            reply_to_message_id=original_message.message_id,
            parse_mode=None
        )
        logger.info("✅ Reply sent successfully.")
        return True
    except Exception as e:
        logger.error(f"❌ Telegram Reply Error: {e}")
        return False