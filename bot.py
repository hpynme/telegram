from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7201613802:AAEgc3CijkfcbkuDGoMTVuZdZtzjWj0HuXM'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('হ্যালো আহাদ! তোমার বট চালু হয়েছে।')

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("Bot is running...")
    app.run_polling()
