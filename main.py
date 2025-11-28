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
        "Type anything and I'll gaslight you."
    )

async def gaslight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = random.choice(GASLIGHT_REPLIES)
    await update.message.reply_text(reply)

# --------- MAIN (NO asyncio.run HERE) ----------
def main() -> None:
    print("Starting gaslighter bot… token present:", bool(TOKEN))

    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gaslight", gaslight))

    # Auto-gaslight every text message
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gaslight))

    # This manages its own event loop internally
    app.run_polling()

if __name__ == "__main__":
    main()
