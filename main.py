import os
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# --------- ENV TOKEN ----------
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("ERROR: BOT_TOKEN is missing in Railway variables!")

# --------- KEYWORDS THAT TRIGGER GASLIGHTING ----------
KEYWORDS = [
    "down",
    "dump",
    "rug",
    "rekt",
    "scam",
    "sell",
    "selling",
    "crash",
    "dead",
    "liquidity",
    "volume",
    "exit",
    "bear",
    "panic",
]

# --------- GASLIGHT LINES ----------
GASLIGHT_REPLIES = [
    "Chart’s not down — you’re just holding it wrong. 📉➡️📈",
    "Those red candles? Emotional support lighting.",
    "$GAS isn’t dumping — reality is coping.",
    "You're not rekt — you're early to the comeback arc. 🔥",
    "That wasn’t a rug, it was a surprise floor adjustment. 🧼",
    "It’s not low volume; it's *exclusive entry conditions*.",
    "We didn’t lose liquidity — we released it back into the wild.",
    "No, YOU'RE down bad, not the chart. 😌",
    "That dip wasn’t real. You hallucinated it.",
    "Selling? Couldn’t be me. Deny everything.",
]

# --------- HANDLERS ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to the $GAS Gaslighter Bot!\n"
        "I only show up when you start talking bearish."
    )

async def gaslight_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manual /gaslight command."""
    reply = random.choice(GASLIGHT_REPLIES)
    await update.message.reply_text(reply)

async def gaslight_on_keywords(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Auto-gaslight only when certain words are in the message."""
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # Check if any keyword appears in the message
    if any(word in text for word in KEYWORDS):
        reply = random.choice(GASLIGHT_REPLIES)
        await update.message.reply_text(reply)
    else:
        # No keywords → stay silent
        return

# --------- MAIN (SYNC ENTRYPOINT) ----------
def main() -> None:
    print("Starting gaslighter bot… token present:", bool(TOKEN))

    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gaslight", gaslight_command))

    # Auto-gaslight only when keywords appear
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gaslight_on_keywords))

    app.run_polling()

if __name__ == "__main__":
    main()
