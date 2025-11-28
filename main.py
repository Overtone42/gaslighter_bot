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
    "down", "dump", "rug", "rekt", "scam", "sell", "selling", "crash",
    "dead", "liquidity", "volume", "exit", "bear", "panic", "floor",
    "wipe", "lose", "loss", "red", "dip"
]

# --------- GASLIGHT RESPONSES (40+ LINES) ----------
GASLIGHT_REPLIES = [
    "Chart’s not down — you’re just holding it wrong.",
    "Those red candles? Emotional support lighting.",
    "$GAS isn’t dumping — reality is coping.",
    "You're not rekt — you're early to the comeback arc.",
    "That wasn’t a rug, it was a surprise floor adjustment.",
    "Volume isn't low — it's *elite scarcity*.",
    "We didn’t lose liquidity — we released it back into the wild.",
    "No, YOU'RE down bad, not the chart.",
    "That dip wasn’t real. You imagined it.",
    "Deny everything. Especially reality.",
    "The chart is fine. Your attitude isn’t.",
    "Price didn’t fall — your expectations did.",
    "That's not a dump. It's a confidence test.",
    "You’re panicking? Funny, the chart isn’t.",
    "Rug? No. That was a tactical repositioning.",
    "Bearish? Impossible. You misread the vibes.",
    "You didn't get liquidated — you donated to the ecosystem.",
    "Scam? No, you’re just untrained in enlightenment.",
    "We didn't crash — gravity just glitched.",
    "That's not down — it's directionally flexible.",
    "Price didn’t move. Your screen did.",
    "This isn't a correction — it's a character-building arc.",
    "You're not losing — you're deepening your conviction.",
    "Fear? That’s just bullishness warming up.",
    "You think it's red? Interesting hallucination.",
    "The market isn’t dumping — it’s stretching.",
    "Stop calling it a dip. It's value condensation.",
    "No rug — the floor just wanted some alone time.",
    "This volatility? Emotional growth.",
    "That sell-off was a stress test... for YOU.",
    "You're not down — you're invested in a different dimension.",
    "Ignore the chart. It’s shy today.",
    "That's not liquidity leaving — it's liquidity exploring.",
    "Correction? No, the chart sneezed.",
    "You're not coping — you're coping incorrectly.",
    "We didn’t bounce — we tactically hovered.",
    "Low volume? That’s curated exclusivity.",
    "Dip? That was just price doing yoga.",
    "Relax. Reality is the only thing that’s wrong.",
    "Your portfolio isn’t bleeding — it’s expressing itself.",
    "Candles aren't red — they're passionate.",
]

# --------- COMMAND HANDLERS ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 $GAS Gaslighter Bot Activated.\n"
        "Tag me or talk bearish and I’ll fix your reality."
    )

async def gaslight_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = random.choice(GASLIGHT_REPLIES)
    await update.message.reply_text(reply)


# --------- AUTO GASLIGHTING ----------
async def gaslight_auto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    # ---- A) If the bot is @tagged, always reply ----
    if update.message.entities:
        for ent in update.message.entities:
            if ent.type == "mention":
                if context.bot.username.lower() in text:
                    reply = random.choice(GASLIGHT_REPLIES)
                    await update.message.reply_text(reply)
                    return

    # ---- B) Keyword triggers ----
    if any(word in text for word in KEYWORDS):
        reply = random.choice(GASLIGHT_REPLIES)
        await update.message.reply_text(reply)


# --------- MAIN ----------
def main():
    print("Starting gaslighter bot… token:", bool(TOKEN))

    app = ApplicationBuilder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gaslight", gaslight_command))

    # Auto-replies (mentions + keywords)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gaslight_auto))

    app.run_polling()

if __name__ == "__main__":
    main()
