import os
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    MessageHandler,
    CommandHandler,
    filters,
)

# Load bot token from Railway / GitHub Environment Variables
TOKEN = os.getenv("BOT_TOKEN")

# Gaslighting replies for $GAS bot
GASLIGHT_REPLIES = [
    "Chart’s not down — you’re just holding it wrong. 📉➡️📈",
    "That wasn’t a rug, it was a surprise floor adjustment. 🧼",
    "You're not rekt — you're early to the comeback arc. 🔥",
    "Those red candles? Emotional support lighting.",
    "$GAS isn’t dumping — reality is coping.",
    "It’s not low volume; it's *exclusive entry conditions*.",
    "We didn’t lose liquidity — we released it back into the wild.",
    "No, YOU'RE down bad, not the chart. 😌",
    "That dip wasn’t real. You hallucinated it.",
    "Selling? Couldn’t be me. Couldn't be you either. Deny everything.",
]

# Words that trigger the bot to gaslight
TRIGGERS = ["dump", "down", "red", "rug", "rekt", "scam", "panic", "sell", "dip", "wtf"]


def should_reply(text: str) -> bool:
    """Returns True if message contains a trigger word."""
    text = text.lower()
    return any(t in text for t in TRIGGERS)


# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 I am Lighter — the official $GAS gaslighting bot.\n"
        "Complain about the chart and I’ll fix your reality."
    )


# /gaslight command (manual trigger)
async def gaslight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(GASLIGHT_REPLIES))


# Automatic message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    msg = update.message.text

    if should_reply(msg):
        # 40% chance to fire to avoid spamming every message
        if random.random() < 0.40:
            await update.message.reply_text(random.choice(GASLIGHT_REPLIES))


# Main bot function
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gaslight", gaslight))

    # Auto-response
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🔥 GASLIGHTER BOT RUNNING…")
    app.run_polling()


if __name__ == "__main__":
    main() 
