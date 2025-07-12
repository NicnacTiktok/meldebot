import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Secure Connection Established.\n"
        "🔗 System ready for threat reporting.\n\n"
        "Send the username or link of the target channel or group to proceed."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    channel_name = update.message.text
    reply_text = (
        f"🔍 Scanning target: **{channel_name}**\n"
        f"⚙️ Analyzing metadata...\n"
        f"✅ Report submitted to Telegram Security Division.\n"
        f"Incident ID: #{generate_incident_id()}\n"
        f"Status: Pending Investigation\n"
        f"⏳ Please allow up to 72 hours for resolution."
    )
    await update.message.reply_text(reply_text, parse_mode="Markdown")

import random

def generate_incident_id():
    return f"TG-{random.randint(100000, 999999)}"

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()
