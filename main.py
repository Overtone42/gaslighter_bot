import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

GASLIGHT_REPLIES = [
    "Chart’s not down — you're just holding it wrong.",
    "Those red candles? Emotional support indicators.",
    "$GAS isn’t dumping — reality is coping.",
    "You're not rekt — you're early to the next run.",
    "That wasn’t a rug, it was a surprise airdrop.",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Welcome to the $GAS Gaslighter Bot!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from random import choice
    reply = choice(GASLIGHT_REPLIES)
    await update.message.reply_text(reply)

async def main():
    print("Starting bot with token:", TOKEN is not None)

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
