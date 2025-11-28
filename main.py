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

# -----------------------------------------
# Load Bot Token from Railway Environment
# -----------------------------------------
TOKEN = os.getenv("BOT_TOKEN")

print("Starting gaslighter bot...")
print("Token present:", bool(TOKEN))

if not TOKEN:
    raise RuntimeError("ERROR: BOT_TOKEN is missing in Railway variables!")

# -----------------------------------------
# Gaslighting Replies for $GAS
# -----------------------------------------
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
    "Selling? Couldn't be me. Deny everything.",
]

# -----------------------------------------
# /start command
# -----------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Welcome to the $GAS Gaslighter Bot!\n"
        "Type anything and I'll gaslight you immediately."
    )

# -----------------------------------------
# Manual gaslight command for fun
# -----------------------------------------
async def gaslight_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = random.choice(GASLIGHT_REPLIES)
    await update.message.reply_text(reply)

# -----------------------------------------
# Automatic gaslighting on every message
# -----------------------------------------
async def gaslight_auto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = random.choice(GASLIGHT_REPLIES)
    await update.message.reply_text(reply)

# -----------------------------------------
# MAIN BOT RUNNER
# -----------------------------------------
async def main():
    print("Building Telegram bot…")

    app = ApplicationBuilder().token(TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gaslight", gaslight_cmd))

    # auto gaslight
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gaslight_auto))

    print("🚀 GASLIGHTER BOT IS LIVE")
    await app.run_polling()

# -----------------------------------------
# ENTRY POINT
# -----------------------------------------
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
